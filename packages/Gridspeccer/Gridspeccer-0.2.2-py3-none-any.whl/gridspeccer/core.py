#!/usr/bin/env python
# encoding: utf-8

"""
    Core utils for all figures.
"""

import importlib
import logging
import matplotlib as mpl
from matplotlib import gridspec as gs
import os
import os.path as osp
import string
import sys
import numpy as np
import pylab as p

from pathlib import Path

np.random.seed(424242)


def make_log(name):
    "create logger"
    tmp_log = logging.Logger(name)
    if "DEBUG" in os.environ:
        log_level = logging.DEBUG
        log_formatter = logging.Formatter(
            "%(asctime)s %(levelname)s: " "%(message)s", datefmt="%y-%m-%d %H:%M:%S"
        )
    else:
        log_level = logging.INFO
        log_formatter = logging.Formatter(
            "%(asctime)s %(levelname)s: " "%(message)s", datefmt="%y-%m-%d %H:%M:%S"
        )
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(log_formatter)
    tmp_log.addHandler(log_handler)
    tmp_log.setLevel(log_level)
    return tmp_log


log = make_log("gridspeccer")

# in order to have consistent coloring, please have all colors be defined here
label_to_color = {
    # preliminary:
    "sw": "k",
    "sw+hw": "m",  # "r",
    "hw_all": "g",
    "hw_single": "b",
}

layer_to_color = {
    "hidden": "orange",
    "label": "blue",
    "bad": "red",
}

dataset_to_color = {
    "train": "g",
    "test": "b",
    "train_theo": "darkgreen",
    "test_theo": "#062A78",
    #  "hw_mean": "deepskyblue",
    #  "hw_span": "aqua",
    "hw_mean": "#A67B5B",
    "hw_span": "wheat",
}


def make_figure(name, folder=Path("../fig"), filetype=".pdf"):
    "start making the figure"
    log.info("--- Creating figure: %s ---", name)

    plotscript = get_plotscript(name)

    try:
        gs_main = plotscript.get_gridspec()
    except AttributeError:
        log.error("Work on %s hasn't even started yet, sheesh!", name)
        return

    try:
        fig_kwargs = plotscript.get_fig_kwargs()
    except AttributeError:
        log.warning("get_fig_kwargs script missing for figure <%s>!", name)
        fig_kwargs = {}

    fig, axes = make_axes(gs_main, fig_kwargs=fig_kwargs)

    # call possible axes adjustment script for figure
    getattr(plotscript, "adjust_axes", lambda x: log.info("No adjust_axes() defines"))(axes)

    for k, axis in list(axes.items()):
        log.info("Plotting subfigure: %s", k)
        plot_function = getattr(plotscript, "plot_{}".format(k), None)
        if plot_function is None:
            log.warning("Plotscript missing for subplot <%s> in figure <%s>!", k, name)
        else:
            plot_function(axis)

    log.info("Plotting labels…")
    try:
        getattr(plotscript, "plot_labels")(axes)
    except AttributeError:
        log.warning("Not plotting labels for figure %s", name)

    save_figure(fig, folder / name, filetype)
    p.close(fig)


def get_plotscript(name):
    "get the script that details the plot"
    try:
        sys.path.append(os.getcwd())
        plotscript = importlib.import_module(name)
    except ImportError:
        log.error("Plotscript for figure %s not found!", name)
        raise
    sys.path.pop(-1)
    return plotscript


def ensure_folder_exists(folder):
    folder = Path(folder)
    if not folder.is_dir():
        folder.mkdir(parents=True)


def save_figure(fig, name, filetype=".pdf"):
    "save figure"
    name = Path(name)
    ensure_folder_exists(name.parent)
    fig.savefig(name.with_suffix(filetype))


def make_axes(gridspec, fig_kwargs=None):
    """
    Turn gridspec information into plots.
    """
    if fig_kwargs is None:
        fig_kwargs = {}

    fig = p.figure(**fig_kwargs)
    axes = {}

    for k, gs_item in list(gridspec.items()):
        # we just add a label to make sure all axes are actually created
        log.debug("Creating subplot: %s", k)
        gs_props = {}
        if isinstance(gs_item, tuple):
            if len(gs_item) != 2 or not isinstance(gs_item[1], dict):
                raise ValueError("Subplots should be specified either as SubplotSpec or (SubplotSpec, dict).")
            gs_props = gs_item[1]
            gs_item = gs_item[0]

        kwargs = {"label": k}
        if gs_props.get('3d', False):
            kwargs['projection'] = '3d'

        axes[k] = fig.add_subplot(gs_item, **kwargs)

    return fig, axes


def get_data(filename):
    "get data (probably deprecated)"
    return np.load(osp.join("..", "data", filename))


def plot_labels(
    axes,
    labels_to_plot,
    xpos_default=0.04,
    ypos_default=0.90,
    zpos_default=0.00,
    label_xpos=None,
    label_ypos=None,
    label_zpos=None,
    label_color=None,
    label_size=None,
    fontdict=None,
    latexformat="\\textbf{{{}}}",
    listoflabels=string.ascii_lowercase,
):
    """plot labels

    Parameters
    ----------
    latexformat: string
        Format string used for setting the labels, allowing arbitrary latex
        formatting. To not use latex formatting, set it to '{}'.
    listoflabels: iterable
        List of labels to be used for labelling. by default lowercase letters,
        but can be any list to accomodate uppercase or b1, b2 like labels.
    """
    label_xpos = label_xpos if label_xpos is not None else {}
    label_ypos = label_ypos if label_ypos is not None else {}
    label_zpos = label_zpos if label_zpos is not None else {}
    label_color = label_color if label_color is not None else {}
    label_size = label_size if label_size is not None else {}

    for label_idx, char in zip(labels_to_plot,
                               listoflabels):
        log.info("Subplot %s receives label %s", label_idx, char)
        plot_caption(
            axes[label_idx],
            latexformat.format(char),
            xpos=label_xpos.get(label_idx, xpos_default),
            ypos=label_ypos.get(label_idx, ypos_default),
            zpos=label_zpos.get(label_idx, zpos_default),
            color=label_color.get(label_idx, "k"),
            size=label_size.get(label_idx, 16) if isinstance(label_size, dict) else label_size,
            fontdict=fontdict,
        )


def plot_caption(axis, caption, xpos=0.04, ypos=0.88, zpos=0.0, color="k", size=16, fontdict=None):
    "plot caption"
    # find out how our caption will look in reality
    caption_args = {
        "ha": "left",
        "va": "bottom",
        # "weight": "bold",
        "style": "normal",
        "size": size,
        "color": color,
        "zorder": 1000,
    }
    # r = get_renderer(axis.figure)
    # bb = t.get_window_extent(renderer=r)

    # if fontdict is None:
    #     fontdict = {"family": "Linux Biolinum Kb"}
    #     size = caption_args["size"]
    #     bbox = mpatches.FancyBboxPatch(axis.transAxes.transform((xpos, ypos)),
    #             size *1.0, size*1.0, zorder=10,
    #             edgecolor="k", facecolor="r", boxstyle="round")
    #     axis.patches.append(bbox)

    if 'zaxis' not in axis.properties():
        # not a 3d projection
        axis.text(
            xpos, ypos, caption, fontdict=fontdict, transform=axis.transAxes, **caption_args,
        )
    else:
        axis.text(
            xpos, ypos, zpos, caption, fontdict=fontdict, transform=axis.transAxes, **caption_args,
        )


def hide_axis(axis):
    "hide axis"
    axis.get_xaxis().set_visible(False)
    axis.get_yaxis().set_visible(False)


def show_axis(axis):
    "show axis"
    axis.get_xaxis().set_visible(True)
    axis.get_yaxis().set_visible(True)


def hide_ticks(axis, axes="both", minormajor="both"):
    "hide ticks"
    axis.tick_params(axis=axes, which=minormajor, length=0)


def make_spines_all(ax):
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()


def make_spines_right(ax):
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_right()


def make_spines(axis):
    "draw spines"
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)

    axis.get_xaxis().tick_bottom()
    axis.get_yaxis().tick_left()


def make_arrow(
    axis,
    pos_from,
    pos_to,
    color="r",
    arrowstyle="<|-|>",
    shrink_a=0.0,
    shrink_b=0.0,
    transform="data",
):
    "make an arrow"
    axis.annotate(
        "",
        xy=pos_to,
        xytext=pos_from,
        xycoords=transform,
        textcoords=transform,
        arrowprops=dict(
            arrowstyle=arrowstyle, color=color, shrinkA=shrink_a, shrinkB=shrink_b
        ),
    )


def make_arrow_lines(
    axis,
    xpos,
    xlength,
    ypos,
    color="r",
    arrowstyle="<|-|>",
    line_alpha=0.75,
    text_ypos_adjustment=0.0,
    text_va="center",
    text="",
):
    "make line of arrow"

    make_arrow(
        axis, (xpos, ypos), (xpos + xlength, ypos), color=color, arrowstyle=arrowstyle
    )

    axis.text(
        xpos + xlength / 2.0,
        ypos - text_ypos_adjustment,
        text,
        va=text_va,
        color="r",
        ha="center",
    )

    axis.axvline(x=xpos, ls="-", alpha=line_alpha, color=color)
    axis.axvline(x=xpos + xlength, ls="-", alpha=line_alpha, color=color)
