"""
a monitor to record all info
including metric, loss, generation report, reconstruction image
draw the loss and monitor metric curves
"""
import pandas as pd
import scipy.misc
from datetime import datetime
import os
import matplotlib.pyplot as plt
import numpy as np
import os.path as osp
from collections import defaultdict
from utils import html
import visdom
from numpy import inf
import time


class Monitor(object):
    """
    statistic level:
        level 1 (defalut): simply demonstrate progress, loss and metric
        level 2: draw the curves
    """
    def __init__(self, cfgs):
        self.cfgs = cfgs
        self.statistic_level = cfgs["statistic_level"]
        # init monitor
        self.record_dir = cfgs["record_dir"]
        if not os.path.exists(self.record_dir):
            os.makedirs(self.record_dir)

        self.log_dir = osp.join(self.record_dir, 'record.log')
        with open(self.log_dir, "w") as f:
            t = get_timestamp()
            temp = "=" * 25
            temp_1 = "=" * 65
            f.write(f"{temp} {t} {temp}\n{self.cfgs}\n{temp_1}")

        self.monitor_mode = cfgs["monitor_mode"]
        self.monitor_metric = 'val_' + self.cfgs["monitor_metric"]
        self.monitor_metric_test = 'test_' + self.cfgs["monitor_metric"]
        assert self.monitor_mode in ['min', 'max']

        self.monitor_best = inf if self.monitor_mode == 'min' else -inf
        self.best_recorder = {'val': {self.monitor_metric: self.monitor_best},
                              'test': {self.monitor_metric_test: self.monitor_best}}

        # only record current epoch
        self.name2val = defaultdict(float)
        self.name2cnt = defaultdict(int)

        self.not_improved_count = 0
        # TODO draw the socre curves
        if cfgs["monitor_metric_curves"]:
            self.display_id = 1
            self.use_html = True
            self.win_size = 160
            self.name = cfgs['task_name']
            self.cfgs = cfgs
            self.saved = False
            self.vis = visdom.Visdom(port=cfgs['display_port'])

            if self.use_html:
                self.web_dir = osp.join(self.record_dir, 'web')
                self.img_dir = os.path.join(self.web_dir, 'images')
                if osp.exists(self.web_dir) is False:
                    os.mkdir(self.web_dir)
                    os.mkdir(self.img_dir)
                print('create web directory %s...' % self.web_dir)
                # util.mkdirs([self.web_dir, self.img_dir])
            # self.log_name = os.path.join(opt['path']['checkpoint'], 'loss_log.txt')
            # with open(self.log_name, "a") as log_file:
            #     now = time.strftime("%c")
            #     log_file.write('================ Training Loss (%s) ================\n' % now)

    def _log_mean(self, key, val):
        if key in self.name2val.keys():
            oldval, cnt = self.name2val[key], self.name2cnt[key]
            self.name2val[key] = (oldval * cnt + val) / (cnt + 1)
            self.name2cnt[key] = cnt + 1
        else:
            self.name2val[key] = val
            self.name2cnt[key] = 1

    def log_mean(self, info):
        if isinstance(info, tuple):
            key, val = info
            self._log_mean(key, val)
        elif isinstance(info, dict):
            for key in info.keys():
                self._log_mean(key, info[key])
        else:
            raise ValueError("It should be a dict or a tuple such as (key, val)")

    def dump(self, epoch):
        d = self.name2val
        d["epoch"] = epoch
        out = d.copy()  # Return the dict for unit testing purposes
        arr = dict2str(out)
        with open(self.log_dir, "a") as f:
            f.write(arr)
        self.name2val.clear()
        self.name2cnt.clear()
        return out

    def log(self, info):
        if isinstance(info, tuple):
            key, val = info
            self.name2val[key] = val
        elif isinstance(info, dict):
            self.name2val.update(info)
        else:
            raise ValueError("It should be a dict or a tuple such as (key, val)")
    
    def record_best(self):
        improved_val = (self.monitor_mode == 'min' and self.name2val[self.monitor_metric] <= self.best_recorder['val'][
            self.monitor_metric]) or \
                       (self.monitor_mode == 'max' and self.name2val[self.monitor_metric] >= self.best_recorder['val'][self.monitor_metric])
        if improved_val:
            self.best_recorder['val'].update(self.name2val)

        improved_test = (self.monitor_mode == 'min' and self.name2val[self.monitor_metric_test] <= self.best_recorder['test'][
            self.monitor_metric_test]) or \
                        (self.monitor_mode == 'max' and self.name2val[self.monitor_metric_test] >= self.best_recorder['test'][
                            self.monitor_metric_test])
        if improved_test:
            self.best_recorder['test'].update(self.name2val)

    def check_best(self):
        is_best = False
        early_stop = False
        if self.monitor_mode != 'off':
                try:
                    # check whether model performance improved or not, according to specified metric(mnt_metric)
                    improved = (self.monitor_mode == 'min' and self.name2val[self.monitor_metric] <= self.monitor_best) or \
                               (self.monitor_mode == 'max' and self.name2val[self.monitor_metric] >= self.monitor_best)
                except KeyError:
                    print("Warning: Metric '{}' is not found. " "Model performance monitoring is disabled.".format(
                        self.monitor_metric))
                    self.monitor_mode = 'off'
                    improved = False

                if improved:
                    self.monitor_best = self.name2val[self.monitor_metric]
                    self.not_improved_count = 0
                    is_best = True
                else:
                    self.not_improved_count += 1

                if self.not_improved_count > self.cfgs['early_stop']:
                    print("Validation performance didn\'t improve for {} epochs. " "Training stops.".format(
                        self.cfgs['early_stop']))
                    early_stop = True
        return is_best, early_stop

    def _print_best(self):
        print('Best results (w.r.t {}) in validation set:'.format(self.cfgs["monitor_metric"]))
        for key, value in self.best_recorder['val'].items():
            print('\t{:15s}: {}'.format(str(key), value))

        print('Best results (w.r.t {}) in test set:'.format(self.cfgs["monitor_metric"]))
        for key, value in self.best_recorder['test'].items():
            print('\t{:15s}: {}'.format(str(key), value))

    def print_best_and_save_to_file(self):
        t = get_timestamp()
        temp = "=" * 25
        info = f'{temp} {t} {temp}\n'
        _info = 'Best results (w.r.t {}) in validation set:'.format(self.cfgs["monitor_metric"])
        info += _info + "\n"
        print(_info)

        for key, value in self.best_recorder['val'].items():
            _info = '\t{:15s}: {}'.format(str(key), value)
            info += _info + '\n'
            print(_info)

        _info = 'Best results (w.r.t {}) in test set:'.format(self.cfgs["monitor_metric"])
        info += _info + "\n"
        print(_info)
        for key, value in self.best_recorder['test'].items():
            _info = '\t{:15s}: {}'.format(str(key), value)
            info += _info + '\n'
            print(_info)
        
        self.write(info)

    def write(self, info):
        with open(self.log_dir, "a") as f:
            f.write(info)
        print(info)

    def reset_visdom(self):
        self.saved = False

    def print(self, info, flush=False):
        if flush:
            print('\r'+info, end='', flush=True)
        else:
            print(info)

    # |visuals|: dictionary of images to display or save\

    def display_current_images(self, visuals, epoch, save_result):
        if self.display_id > 0:  # show images in the browser
            ncols = 0  # self.opt.display_single_pane_ncols
            if ncols > 0:
                h, w = next(iter(visuals.values())).shape[:2]
                table_css = """<style>
                        table {border-collapse: separate; border-spacing:4px; white-space:nowrap; text-align:center}
                        table td {width: %dpx; height: %dpx; padding: 4px; outline: 4px solid black}
                        </style>""" % (w, h)
                title = self.name
                label_html = ''
                label_html_row = ''
                nrows = int(np.ceil(len(visuals.items()) / ncols))
                images = []
                idx = 0
                for label, image_numpy in visuals.items():
                    label_html_row += '<td>%s</td>' % label
                    images.append(image_numpy.transpose([2, 0, 1]))
                    idx += 1
                    if idx % ncols == 0:
                        label_html += '<tr>%s</tr>' % label_html_row
                        label_html_row = ''
                white_image = np.ones_like(image_numpy.transpose([2, 0, 1])) * 255
                while idx % ncols != 0:
                    images.append(white_image)
                    label_html_row += '<td></td>'
                    idx += 1
                if label_html_row != '':
                    label_html += '<tr>%s</tr>' % label_html_row
                # pane col = image row
                self.vis.images(images, nrow=ncols, win=self.display_id + 1,
                                padding=2, opts=dict(title=title + ' images'))
                label_html = '<table>%s</table>' % label_html
                self.vis.text(table_css + label_html, win=self.display_id + 2,
                              opts=dict(title=title + ' labels'))
            else:
                idx = 1
                for label, image_numpy in visuals.items():
                    self.vis.image(image_numpy.transpose([2, 0, 1]), opts=dict(title=label),
                                   win=self.display_id + idx)
                    idx += 1

        if self.use_html and (save_result or not self.saved):  # save images to a html file
            self.saved = True
            for label, image_numpy in visuals.items():
                img_path = os.path.join(self.img_dir, 'epoch%.3d_%s.png' % (epoch, label))
                save_image(image_numpy, img_path)
            # update website
            webpage = html.HTML(self.web_dir, 'Experiment name = %s' % self.name, reflesh=1)
            for n in range(epoch, 0, -1):
                webpage.add_header('epoch [%d]' % n)
                ims = []
                txts = []
                links = []

                for label, image_numpy in visuals.items():
                    img_path = 'epoch%.3d_%s.png' % (n, label)
                    ims.append(img_path)
                    txts.append(label)
                    links.append(img_path)
                webpage.add_images(ims, txts, links, width=self.win_size)
            webpage.save()

    def display_current_results(self, visuals, epoch, save_result):
        if self.display_id > 0:  # show report in the browser
            idx = 1
            for label, report in visuals.items():
                self.vis.text(report, opts=dict(title=label), win=self.display_id + idx)
                idx += 1

        """
        if self.use_html:  # save report to a html file
            # update website
            webpage = html.HTML(self.web_dir, 'Experiment name = %s' % self.name, reflesh=1)
            for n in range(epoch, 0, -1):
                webpage.add_header('epoch [%d]' % n)
                ims = []
                txts = []
                links = []

                for label, report in visuals.items():
                    img_path = 'epoch%.3d_%s.png' % (n, label)
                    ims.append(img_path)
                    txts.append(label)
                    links.append(img_path)
                webpage.add_images(ims, txts, links, width=self.win_size)
            webpage.save()
        """

    # errors: dictionary of error labels and values
    def plot_current_metrics(self, epoch, metrics, counter_ratio=None):
        if not hasattr(self, 'plot_data'):
            self.plot_data = {'X': [], 'Y': [], 'legend': list(metrics.keys())}
        if counter_ratio is None:
            self.plot_data['X'].append(epoch)
        else:
            self.plot_data['X'].append(epoch+counter_ratio)
        self.plot_data['Y'].append([metrics[k] for k in self.plot_data['legend']])
        self.vis.line(
            X=np.stack([np.array(self.plot_data['X'])] * len(self.plot_data['legend']), 1),
            Y=np.array(self.plot_data['Y']),
            opts={
                'title': self.name + ' metrics over time',
                'legend': self.plot_data['legend'],
                'xlabel': 'epoch',
                'ylabel': 'loss'},
            win=self.display_id)

    # errors: same format as |errors| of plotCurrentErrors
    def print_current_metrics(self, epoch, metrics, t, mode):
        message = '(%s - epoch: %d | time: %.3f) ' % (mode, epoch, t)
        for k, v in metrics.items():
            message += '%s: %.6f ' % (k, v)

        print(message)
        with open(self.log_name, "a") as log_file:
            log_file.write('%s\n' % message)

        # save image to the disk

    def save_images(self, webpage, visuals, image_path):
        image_dir = webpage.get_image_dir()
        # short_path = ntpath.basename(image_path[0])
        # name = os.path.splitext(short_path)[0]

        short_path = image_path.split('/')
        name = short_path[-1]

        webpage.add_header(name)
        ims = []
        txts = []
        links = []

        for label, image_numpy in visuals.items():
            image_name = '%s_%s.png' % (name, label)
            save_path = os.path.join(image_dir, image_name)
            save_image(image_numpy, save_path)
            ims.append(image_name)
            txts.append(label)
            links.append(image_name)
        webpage.add_images(ims, txts, links, width=self.win_size)

    def save_data_plt(self, webpage, visuals, pred_gt, pred, image_path):
        image_dir = webpage.get_image_dir()
        short_path = image_path.split('/')
        name = short_path[-1]

        webpage.add_header(name)
        ims = []
        txts = []
        links = []

        for label, image_numpy in visuals.items():
            image_name = '%s_%s.png' % (name, label)
            save_path = os.path.join(image_dir, image_name)
            img = image_numpy[0].cpu().float().numpy()
            fig = plt.imshow(img[0, ...])
            fig.set_cmap('gray')
            plt.axis('off')
            plt.savefig(save_path)
            plt.close()
            ims.append(image_name)
            txts.append(label)
            links.append(image_name)

        image_name = '%s_%s.png' % (name, 'pred_gt')
        save_path = os.path.join(image_dir, image_name)
        img = pred_gt.astype(float)
        fig = plt.imshow(img)
        fig.set_cmap('gray')
        plt.axis('off')
        plt.savefig(save_path)
        plt.close()
        ims.append(image_name)
        txts.append('pred_gt')
        links.append(image_name)

        webpage.add_images(ims, txts, links, width=self.win_size)

    def save_result_fig(self, img, imgName, webpage, image_path):
        image_dir = webpage.get_image_dir()
        short_path = image_path.split('/')
        name = short_path[-1]
        image_name = '%s_%s.png' % (name, imgName)
        save_path = os.path.join(image_dir, image_name)
        img = img.astype(float)
        fig = plt.imshow(img)
        fig.set_cmap('gray')
        plt.axis('off')
        plt.savefig(save_path)
        plt.close()


def get_timestamp():
    return datetime.now().strftime('%y%m%d_%H%M%S')


def dict2str(opt, indent_l=1):
    """dict to string for logger"""
    msg = ''
    for k, v in opt.items():
        if isinstance(v, dict):
            msg += ' ' * (indent_l * 2) + k + ':[\n'
            msg += dict2str(v, indent_l + 1)
            msg += ' ' * (indent_l * 2) + ']\n'
        else:
            msg += ' ' * (indent_l * 2) + k + ': ' + str(v) + '\n'
    return msg


def kv2arr(opt):
    arr = '-' * 25
    arr += f'\nstep: {opt["step"]}\n'
    arr += f'samples: {opt["samples"]}\n'
    arr += f'mse: {opt["mse"]:.4f}\n'
    arr += f'mse_4q: [{opt["mse_q0"]:.4f}, {opt["mse_q1"]:.4f}, {opt["mse_q2"]:.4f}, {opt["mse_q3"]:.4f}]\n'
    arr += f'loss: {opt["loss"]:.4f}\n'
    arr += f'loss_4q: [{opt["loss_q0"]:.4f}, {opt["loss_q1"]:.4f}, {opt["loss_q2"]:.4f}, {opt["loss_q3"]:.4f}]\n'
    arr += f'grad_norm: {opt["grad_norm"]}\n'
    arr += f'param_norm: {opt["param_norm"]}'
    return arr


def save_image(image_numpy, image_path):
    # image_pil = Image.fromarray(image_numpy)
    image_pil = scipy.misc.toimage(image_numpy)
    image_pil.save(image_path)
