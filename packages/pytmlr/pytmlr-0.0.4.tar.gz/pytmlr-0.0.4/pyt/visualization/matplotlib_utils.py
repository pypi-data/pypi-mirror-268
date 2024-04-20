import numpy as np, os.path as osp, seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

from matplotlib.colorbar import Colorbar
from matplotlib.colors import Normalize, LogNorm
from matplotlib.axes import Axes
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mmengine import mkdir_or_exist
from pyt.data import is_num

sns.set_theme(style="whitegrid", rc={"grid.linestyle": "--"}, font_scale=1.8)

# color settings are from https://matplotlib.org/stable/tutorials/colors/colors.html
DEFAULT_COLORS = ["#d62728", "#ff7f0e", "#1f77b4", "#2ca02c", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]


def recover_default_sns_theme():
    sns.set_theme(style="whitegrid", rc={"grid.linestyle": "--"}, font_scale=1.8)


def build_figs(
    nrows=1, ncols=None, *, sharex=False, sharey=False, width_ratios=None, height_ratios=None, subplot_kw=None, gridspec_kw=None, **kwargs
):
    if ncols is None:
        squeeze = True
        nrows, ncols = 1, nrows
    else:
        squeeze = False
    fig, axes = plt.subplots(
        nrows,
        ncols,
        sharex=sharex,
        sharey=sharey,
        squeeze=squeeze,
        width_ratios=width_ratios,
        height_ratios=height_ratios,
        subplot_kw=subplot_kw,
        gridspec_kw=gridspec_kw,
        **kwargs,
    )
    return fig, axes


def build_figs_same(nrows=1, ncols=None, *, width_ratio=1.2, height=7, **kwargs):
    shape = (1, nrows) if ncols is None else (nrows, ncols)
    fig, axes = build_figs(
        nrows,
        ncols,
        figsize=(width_ratio * height * shape[1], height * shape[0]),
        gridspec_kw={"width_ratios": [1 for _ in range(shape[1])]},
        **kwargs,
    )
    return fig, axes


def plot_show(fig=None, filename=None):
    fig = plt.gcf() if fig is None else fig
    fig.tight_layout()
    if filename is None:
        fig.show()
    else:
        mkdir_or_exist(osp.dirname(filename))
        fig.savefig(filename, bbox_inches="tight")


def build_shared_legend(fig=None, bottom=None, **kwargs):
    fig = plt.gcf() if fig is None else fig
    lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
    lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
    fig.legend(lines, labels, **kwargs)
    if bottom is not None:
        fig.subplots_adjust(bottom=bottom)


def set_plot_legend(ax=None, **kwargs):
    ax = plt.gca() if ax is None else ax

    # title = kwargs.get("title", None)
    # if title is not None:
    #     if isinstance(title, dict):
    #         ax.set_title(**title)
    #     else:
    #         ax.set_title(title)

    for kwargs_name in ["title", "xticks", "yticks", "xlim", "ylim", "xlabel", "ylabel"]:
        item = kwargs.get(kwargs_name, None)
        if item is None:
            continue
        func = getattr(ax, f"set_{kwargs_name}")
        if isinstance(item, dict):
            func(**item)
        else:
            func(item)

    #     if item is not None:
    #         (**item)

    # for arg_name in ["xlim", "ylim", "xlabel", "ylabel"]:
    #     item = kwargs.get(arg_name, None)
    #     if item is not None:
    #         getattr(ax, f"set_{arg_name}")(item)


def plot_line(x, y, std=None, label=None, color=None, ax=None, alpha=0.1, **kwargs):
    ax.plot(x, y, color=color, label=label, **kwargs)
    if std is not None:
        x = np.array(x)
        y = np.array(y)
        std = np.array(std)
        ax.fill_between(x, y - std, y + std, color=color, alpha=alpha)


"""
def plot_lines(
    xs,
    ys,
    stds=None,
    labels=None,
    colors=None,
    alpha=0.1,
    ax=None,
    line_kwargs=None,
):
    if is_num(xs[0]):
        xs, ys = [xs], [ys]
        if stds is not None:
            stds = [stds]
        if colors is not None:
            colors = [colors]
        if labels is not None:
            labels = [labels]
    assert len(xs) == len(ys)
    if stds is not None:
        assert len(xs) == len(stds)
    if colors is not None:
        assert len(xs) == len(colors)
    if labels is not None:
        assert len(labels) == len(xs)

    if colors is None:
        colors = DEFAULT_COLORS[: len(xs)]
    assert len(colors) >= len(xs), f"You need to provide colors for so many curves! {len(colors)} < {len(xs)}."

    if ax is None:
        ax = plt.gca()

    for i, (x, y) in enumerate(zip(xs, ys)):
        kwargs = {}
        if labels is not None and labels[i] != None:
            kwargs["label"] = labels[i]
        if line_kwargs is not None:
            if isinstance(line_kwargs, dict):
                kwargs.update(line_kwargs)
            else:
                kwargs.update(line_kwargs[i])
        ax.plot(x, y, color=colors[i], **kwargs)
        if stds is not None:
            std = stds[i]
            ax.fill_between(x, y - std, y + std, color=colors[i], alpha=alpha)
"""


def plot_show_image(image, filepath=None, color_bar=False, ax=None, show=False, log_scale=False, **kwargs):
    if ax is None:
        ax = plt
    ax.clf()
    ax.cla()
    # print(image.shape, dict(kwargs), image[~np.isnan(image)].min(), image[~np.isnan(image)].max())
    if log_scale:
        kwargs["norm"] = LogNorm()
    elif "vmin" in kwargs and "vmax" in kwargs:
        kwargs["norm"] = Normalize(kwargs.pop("vmin"), kwargs.pop("vmax"))
    title = kwargs.pop("title", None)
    img = ax.imshow(image, **kwargs)
    if color_bar:
        if isinstance(ax, Axes):
            divider = make_axes_locatable(ax)
            # cbar.set_clim(-2.0, 2.0)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            ax.colorbar(img, cax=cax)
        else:
            ax.colorbar()
    if title is not None:
        ax.set_title(title)
    if show or filepath:
        plot_show(filepath, ax)
    return img


def add_color_bar(fig, ax, img):
    fig.colorbar(img, ax=ax.ravel().tolist())


def process_input(x, value=None, xrange=None):
    if x.ndim == 2 and x.shape[-1] == 1:
        x = x[:, 0]
    # assert x.ndim == 2 and x.shape[-1] <= 2, f"Input points have shape {x.shape}, but we only support 1D or 2D function recently"
    if value is not None and value.ndim == 2:
        value = value[:, 0]
    if xrange is None:
        x_min = np.min(x, axis=0)
        x_max = np.max(x, axis=0) + 1e-6
        xrange = np.stack([x_min, x_max], axis=-1)
    return x, value, xrange


def plot_scatter(x, colors=None, range=None, file_name=None, s=10, ax=None, show=True):
    if ax is None:
        ax = plt
    img = ax.scatter(x[:, 0], x[:, 1], c=colors, s=s)

    if range is not None:
        assert list(range.shape) == [2, 2]
        ax.xlim(range[0])
        ax.ylim(range[1])
    if show or file_name:
        plot_show(file_name, ax)
    return img


def plot_func_2d(
    x, value=None, bins=128, xrange=None, vrange=None, normalize=None, ax=None, log_scale=False, show=True, color_bar=True, file_name=None, eps=1e-9
):
    x, value, xrange = process_input(x, value, xrange)
    if normalize is None:
        normalize = value is None
    if value is not None:
        from scipy.stats import binned_statistic_2d

        map = binned_statistic_2d(x[:, 0], x[:, 1], value, bins=bins, range=xrange).statistic
        if normalize:
            map_max = np.max(map[~np.isnan(map)])
            map = map / map_max
    else:
        map = np.histogram2d(x[:, 0], x[:, 1], bins, range=xrange)[0]
        if normalize:
            map_sum = np.sum(map[~np.isnan(map)])
            map = map / map_sum
    if vrange is None:
        vrange = [map[~np.isnan(map)].min() + eps, map[~np.isnan(map)].max()]
    map = map.T[::-1]
    return plot_show_image(
        map,
        color_bar=color_bar,
        vmin=vrange[0],
        vmax=vrange[1],
        file_name=file_name,
        extent=xrange.reshape(-1),
        ax=ax,
        show=show,
        log_scale=log_scale,
    )


def plot_func_1d(x, value=None, bins=128, xrange=None, vrange=None, normalize=None, ax=None, log_scale=False, show=True, file_name=None):
    x, value, xrange = process_input(x, value, xrange)
    if normalize is None:
        normalize = value is None
    if value is not None:
        from scipy.stats import binned_statistic

        map = binned_statistic(x, value, bins=bins, range=xrange).statistic
        if normalize:
            map_max = np.max(map[~np.isnan(map)])
            map = map / map_max
    else:
        map = np.histogram(x, bins, range=xrange)[0]
        if normalize:
            map_sum = np.sum(map[~np.isnan(map)])
            map = map / map_sum
    if vrange is None:
        vrange = [map[~np.isnan(map)].min() + 1e-20, map[~np.isnan(map)].max()]

    if ax is None:
        ax = plt
    # print(vrange, bins)
    x = np.arange(bins) / bins
    x = x * xrange[1] + (1 - x) * xrange[0]

    img = ax.bar(x, map, width=0.1, align="edge", log=log_scale)
    if show or file_name:
        plot_show(file_name, ax)
    return img
