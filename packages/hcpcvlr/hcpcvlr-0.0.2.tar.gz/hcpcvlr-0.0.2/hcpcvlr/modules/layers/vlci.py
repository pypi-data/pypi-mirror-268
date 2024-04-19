import torch
import torch.nn as nn
import torch.nn.functional as F
from modules.backbones.transformer import EncoderLayer, SublayerConnection, MultiHeadedAttention, LayerNorm, PositionwiseFeedForward, clones
import math
from einops.layers.torch import Rearrange
from einops import rearrange


class AF(nn.Module):
    """
    Attention Fuse Module
    """
    def __init__(self, embed_dim):
        super(AF, self).__init__()
        self.embed_dim = embed_dim
        self.q = nn.Linear(embed_dim, embed_dim)
        self.out = nn.Linear(embed_dim, embed_dim)

    def forward(self, q, k, v, proj=False):
        if proj:
            q = self.q(q)
            qk = torch.matmul(q, k.transpose(-1, -2)) / math.sqrt(self.embed_dim)
            score = qk.softmax(dim=-1)
            out = score.matmul(v)
            out = self.out(out)
        else:
            qk = torch.matmul(q, k.transpose(-1, -2))
            score = qk.softmax(dim=-1)
            out = score.matmul(v)
        return out


class FDIntervention(nn.Module):
    """
    Front-Door Intervention Module
    """
    def __init__(self, embed_dim):
        super(FDIntervention, self).__init__()
        self.embed_dim = embed_dim
        self.af_1 = AF(embed_dim)
        self.af_2 = AF(embed_dim)

    def forward(self, feature, mediator, proj=False):
        v = self.af_1(mediator, feature, feature, proj)
        out = self.af_2(feature, mediator, v, proj)
        return out


class LGFM(nn.Module):
    """
    Local-Global Fuse Module
    """
    def __init__(self, embed_dim):
        super(LGFM, self).__init__()
        self.embed_dim = embed_dim
        self.norm_l = LayerNorm(embed_dim)
        self.norm_g = LayerNorm(embed_dim)
        self.gelu = nn.GELU()
        self.llf = MultiHeadedAttention(8, embed_dim)
        self.lgf = MultiHeadedAttention(8, embed_dim)
        self.proj = nn.Linear(embed_dim * 2, embed_dim)
        self.norm = LayerNorm(embed_dim)
        self.fc = nn.Sequential(
            nn.Linear(embed_dim, embed_dim * 4),
            nn.Linear(embed_dim * 4, embed_dim),
        )

    def forward(self, fl, fg):
        fl = self.norm_l(fl)
        fg = self.norm_g(fg)
        fll = fl + self.llf(fl, fl, fl)
        flg = fl + self.lgf(fl, fg, fg)
        out = self.proj(torch.cat([fll, flg], dim=-1))
        out = self.norm(out)
        out = out + self.fc(out)
        return out


class CrossLayer(EncoderLayer):
    """
    composed by a cross-attention layer and feed-forward network
    """
    def __init__(self, embed_dim, num_heads, ff_dim, dropout):
        super(CrossLayer, self).__init__(embed_dim, num_heads, ff_dim, dropout)

    def forward(self, x, y):
        x = self.sublayer_attn(x, lambda x: self.attn(x, y, y, None))
        x = self.sublayer_ff(x, self.feed_forward)
        return x


class PartAttention(nn.Module):
    """
    @article{he2021transfg,
    title={TransFG: A Transformer Architecture for Fine-grained Recognition},
    author={He, Ju and Chen, Jie-Neng and Liu, Shuai and Kortylewski, Adam and Yang, Cheng and Bai, Yutong and Wang, Changhu and Yuille, Alan},
    journal={arXiv preprint arXiv:2103.07976},
    year={2021}
    }
    """
    def __init__(self):
        super(PartAttention, self).__init__()

    def forward(self, x, k=6):
        """
        x -> list: the attention list from the encoder
        k: select the top k attention score and their index from each head
        """
        length = len(x)
        last_map = x[0]
        for i in range(1, length):
            last_map = torch.matmul(x[i], last_map)
        last_map = last_map[:, :, 0, 1:]
        max_attn, max_inx = last_map.sort(2, descending=True)
        max_inx = max_inx[:, :, :k].reshape([last_map.size(0), -1])
        max_attn = max_attn[:, :, :k].reshape([last_map.size(0), -1])
        return max_attn, max_inx


class RelativeAttention2D(nn.Module):
    def __init__(self, inp, oup, image_size, heads=8, dim_head=32, dropout=0.):
        super().__init__()
        inner_dim = dim_head * heads
        project_out = not (heads == 1 and dim_head == inp)

        self.ih, self.iw = image_size

        self.heads = heads
        self.scale = dim_head ** -0.5

        # parameter table of relative position bias
        self.relative_bias_table = nn.Parameter(
            torch.zeros((2 * self.ih - 1) * (2 * self.iw - 1), heads))

        coords = torch.meshgrid((torch.arange(self.ih), torch.arange(self.iw)))
        coords = torch.flatten(torch.stack(coords), 1)
        relative_coords = coords[:, :, None] - coords[:, None, :]

        relative_coords[0] += self.ih - 1
        relative_coords[1] += self.iw - 1
        relative_coords[0] *= 2 * self.iw - 1
        relative_coords = rearrange(relative_coords, 'c h w -> h w c')
        relative_index = relative_coords.sum(-1).flatten().unsqueeze(1)
        self.register_buffer("relative_index", relative_index)

        self.attend = nn.Softmax(dim=-1)
        self.to_qkv = nn.Linear(inp, inner_dim * 3, bias=False)

        self.to_out = nn.Sequential(
            nn.Linear(inner_dim, oup),
            nn.Dropout(dropout)
        ) if project_out else nn.Identity()

    def forward(self, x):
        qkv = self.to_qkv(x).chunk(3, dim=-1)
        q, k, v = map(lambda t: rearrange(
            t, 'b n (h d) -> b h n d', h=self.heads), qkv)

        dots = torch.matmul(q, k.transpose(-1, -2)) * self.scale

        # Use "gather" for more efficiency on GPUs
        relative_bias = self.relative_bias_table.gather(
            0, self.relative_index.repeat(1, self.heads))
        relative_bias = rearrange(
            relative_bias, '(h w) c -> 1 c h w', h=self.ih * self.iw, w=self.ih * self.iw)
        dots = dots + relative_bias

        attn = self.attend(dots)
        out = torch.matmul(attn, v)
        out = rearrange(out, 'b h n d -> b n (h d)')
        out = self.to_out(out)
        return out


class LocalSample(nn.Module):
    def __init__(self, embed_dim, num_heads, ff_dim, dropout=0.):
        super(LocalSample, self).__init__()
        self.part_select = PartAttention()
        self.causal_layer = CaaM(embed_dim, num_heads, ff_dim, dropout)

    def forward(self, x, attn, k):
        """
        x: all visual tokens
        attn: attention from encoder
        k: select k local feature

        fl: k local feature without [CLS] token
        """
        part_attn, part_inx = self.part_select(attn, k)
        part_inx = part_inx + 1
        parts = []
        B, num = part_inx.shape
        for i in range(B):
            parts.append(x[i, part_inx[i, :]])
        fl = torch.stack(parts).squeeze(1)
        fl = torch.cat([x[:, :1], fl], dim=1)
        fl = self.causal_layer(fl)[:, 1:]
        return fl


class PreNorm(nn.Module):
    def __init__(self, dim, fn, norm):
        super().__init__()
        self.norm = norm(dim)
        self.fn = fn

    def forward(self, x, **kwargs):
        return self.fn(self.norm(x), **kwargs)


class DownSamplingTrans(nn.Module):
    """
    @article{dai2021coatnet,
    title={CoAtNet: Marrying Convolution and Attention for All Data Sizes},
    author={Dai, Zihang and Liu, Hanxiao and Le, Quoc V and Tan, Mingxing},
    journal={arXiv preprint arXiv:2106.04803},
    year={2021}
    }
    """
    def __init__(self, inp, oup, image_size, heads=8, dim_head=32, downsample=False, dropout=0.):
        super().__init__()
        hidden_dim = int(inp * 4)

        self.ih, self.iw = image_size
        self.downsample = downsample

        if self.downsample:
            self.pool1 = nn.MaxPool2d(3, 2, 1)
            self.pool2 = nn.MaxPool2d(3, 2, 1)
            self.proj = nn.Conv2d(inp, oup, 1, 1, 0, bias=False)

        self.attn = RelativeAttention2D(inp, oup, image_size, heads, dim_head, dropout)
        self.ff = PositionwiseFeedForward(oup, hidden_dim, dropout)

        self.attn = nn.Sequential(
            Rearrange('b c ih iw -> b (ih iw) c'),
            PreNorm(inp, self.attn, nn.LayerNorm),
            Rearrange('b (ih iw) c -> b c ih iw', ih=self.ih, iw=self.iw)
        )

        self.ff = nn.Sequential(
            Rearrange('b c ih iw -> b (ih iw) c'),
            PreNorm(oup, self.ff, nn.LayerNorm),
            Rearrange('b (ih iw) c -> b c ih iw', ih=self.ih, iw=self.iw)
        )

    def forward(self, x):
        if self.downsample:
            x = self.proj(self.pool1(x)) + self.attn(self.pool2(x))
        else:
            x = x + self.attn(x)
        x = x + self.ff(x)
        return x


class GlobalSample(nn.Module):
    def __init__(self, embed_dim, num_heads, ff_dim, dropout):
        super(GlobalSample, self).__init__()
        self.global_sample = DownSamplingTrans(embed_dim, embed_dim, (7, 7), downsample=True)

    def forward(self, x):
        img = x[:, 1:, :]
        B, L, N = img.size()
        img = img.reshape([-1, 14, 14, N])

        img = img.permute(0, 3, 1, 2)
        img = self.global_sample(img)
        img = img.permute(0, 2, 3, 1)

        fg = img.reshape([B, -1, N])
        return fg


class CausalAttention(nn.Module):
    def __init__(self, h, d_model, dropout=0.1):
        super(CausalAttention, self).__init__()
        assert d_model % h == 0
        self.d_k = d_model // h
        self.h = h
        self.linears = clones(nn.Linear(d_model, d_model), 4)
        self.attn = None
        self.dropout = nn.Dropout(p=dropout)

    def forward(self, x):
        q = x
        k = x
        v = x

        nbatches = q.size(0)
        q, k, v = \
            [l(x).view(nbatches, -1, self.h, self.d_k).transpose(1, 2)
             for l, x in zip(self.linears, (q, k, v))]

        d_k = q.size(-1)

        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(d_k)
        p_attn = F.softmax(-scores, dim=-1)
        p_attn_comp = F.softmax(scores, dim=-1)

        self.attn = p_attn
        p_attn = self.dropout(p_attn)
        p_attn_comp = self.dropout(p_attn_comp)
        out = torch.matmul(p_attn, v)
        out = out.transpose(1, 2).contiguous().view(nbatches, -1, self.h * self.d_k)
        out = self.linears[-1](out)
        out_comp = torch.matmul(p_attn_comp, v)
        out_comp = out_comp.transpose(1, 2).contiguous().view(nbatches, -1, self.h * self.d_k)
        out_comp = self.linears[-1](out_comp)
        return out, out_comp


class CaaMSublayerConnection(nn.Module):
    def __init__(self, embed_dim, dropout):
        super(CaaMSublayerConnection, self).__init__()
        self.norm = LayerNorm(embed_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, sublayer):
        attn, attn_comp = sublayer(self.norm(x))
        attn = self.dropout(attn)
        attn_comp = self.dropout(attn_comp)
        return x + attn, attn_comp


class CaaM(nn.Module):
    """
    @inproceedings{wang2021causal,
    title={Causal Attention for Unbiased Visual Recognition},
    author={Wang, Tan and Zhou, Chang and Sun, Qianru and Zhang, Hanwang},
    booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    year={2021}
    }
    """
    def __init__(self, embed_dim, num_heads, ff_dim, dropout):
        super(CaaM, self).__init__()
        self.attn = CausalAttention(num_heads, embed_dim, dropout)
        self.feed_forward = PositionwiseFeedForward(embed_dim, ff_dim, dropout)
        self.sublayer_attn = CaaMSublayerConnection(embed_dim, dropout)
        self.sublayer_ff = SublayerConnection(embed_dim, dropout)

    def forward(self, x, mask=None):
        x, x_comp = self.sublayer_attn(x, lambda x: self.attn(x))
        x = self.sublayer_ff(x, self.feed_forward)
        x = x + self.sublayer_ff(x_comp, self.feed_forward)
        return x


class VDM(nn.Module):
    def __init__(self, embed_dim, num_heads, ff_dim, dropout=.1):
        super(VDM, self).__init__()
        self.fuse = LGFM(embed_dim)
        self.intervene = FDIntervention(embed_dim)

    def forward(self, x, fl=None, fg=None, mode=True, proj=False):
        """
        fl: local feature
        fg: global feature
        """
        if mode:
            mt = self.fuse(fl, fg)
            out = self.intervene(x, mt, proj)
        else:
            out = 0
        return out + x


class LDM(nn.Module):
    def __init__(self, embed_dim):
        super(LDM, self).__init__()
        self.embed_dim = embed_dim
        self.fuse_v = CrossLayer(embed_dim, 8, 4*embed_dim, .1)
        self.fuse_t = CrossLayer(embed_dim, 8, 4*embed_dim, .1)
        self.norm = LayerNorm(embed_dim)
        self.intervene = FDIntervention(embed_dim)

    def forward(self, x, text, vis, mode=True, proj=False):
        if mode:
            mediator = self.fuse_t(vis, text)
            mediator = self.fuse_v(mediator, vis) + mediator
            mediator = self.norm(mediator)
            out = self.intervene(x, mediator, proj)
        else:
            out = 0
        return out + x
