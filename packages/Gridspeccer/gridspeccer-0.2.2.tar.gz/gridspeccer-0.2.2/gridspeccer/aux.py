#!/usr/bin/env python
# encoding: utf-8
"""
This file gathers the auxilliary functions which are repeated over several images
when the plots are created. This should structre the codes and reduce code redundancy.

Use it well!
"""

import sys
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.patches as mpatches
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib import colorbar
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from skimage.transform import resize
from mpl_toolkits import axes_grid1

from . import core


cm_gray_r = plt.get_cmap("gray_r")


def supp_plot_distributions(axis, sampled, target, error_bar=True):
    """
    Keywords:
        -- axis: pointer of the axis object
        -- sampled: numpy matrix with states in columns and repetitions in rows
        -- target: numpy vector of the target distribution
    """

    # Get the medain and the quarters for the emulated distr
    # obtain the data fro the plots
    sampled_median = np.median(sampled, axis=0)
    sampled75 = np.percentile(sampled, 75, axis=0)
    sampled25 = np.percentile(sampled, 25, axis=0)
    err_down = sampled_median - sampled25
    err_up = sampled75 - sampled_median

    xval = np.array(list(range(0, len(sampled_median))))
    # make the bar plots

    axis.bar(xval, target, width=0.35, label="target", bottom=1e-3, color="tab:blue")
    axis.bar(
        xval + 0.35,
        sampled_median,
        width=0.35,
        label="sampled",
        bottom=1e-3,
        color="tab:orange",
    )
    if error_bar:
        axis.errorbar(
            xval + 0.35,
            sampled_median,
            yerr=[err_down, err_up],
            ecolor="black",
            elinewidth=1,
            capthick=1,
            fmt="none",
            capsize=0.0,
            label="IQR",
        )
    # axis.legend()
    # axis.set_yscale('log')
    # axis.set_ylim(5e-2, 3.0001e-1)
    axis.set_xticks([])
    # axis.set_yticks([.05, .1, .2])
    # axis.set_xticklabels(xlabels, rotation='vertical')
    # axis.set_yticklabels(ylabels)
    ylim = axis.get_ylim()
    ylim_new = [0.0, ylim[1]]
    axis.set_ylim(ylim_new)
    axis.set_xlim([min(xval - 0.35), max(xval + 0.35 + 0.35)])

    axis.set_xlabel(r"$\mathbf{z}$")
    axis.set_ylabel(r"$p(\mathbf{z})$")


def supp_plot_three_distributions(axis, sampled_p, sampled_s, target, error_bar=True):
    """
    Keywords:
        -- axis: pointer of the axis object
        -- sampled: numpy matrix with states in columns and repetitions in rows
        -- target: numpy vector of the target distribution
    """

    # Get the medain and the quarters for the emulated distr
    # obtain the data fro the plots
    sampled_median_p = np.median(sampled_p, axis=0)
    errors_p = [
        sampled_median_p - np.percentile(sampled_p, 25, axis=0),
        np.percentile(sampled_p, 75, axis=0) - sampled_median_p,
    ]
    sampled_median_s = np.median(sampled_s, axis=0)
    sampled75_s = np.percentile(sampled_s, 75, axis=0)
    sampled25_s = np.percentile(sampled_s, 25, axis=0)
    err_down_s = sampled_median_s - sampled25_s
    err_up_s = sampled75_s - sampled_median_s

    xval = np.array(list(range(0, len(sampled_median_p))))

    axis.bar(xval, target, width=0.27, label="target", bottom=1e-3, color="tab:olive")
    axis.bar(
        xval + 0.27,
        sampled_median_p,
        width=0.27,
        label="Poisson",
        bottom=1e-3,
        color="tab:blue",
    )
    axis.bar(
        xval + 0.54,
        sampled_median_s,
        width=0.27,
        label="RN",
        bottom=1e-3,
        color="tab:orange",
    )
    if error_bar:
        axis.errorbar(
            xval + 0.27,
            sampled_median_p,
            yerr=errors_p,
            ecolor="black",
            elinewidth=1,
            capthick=1,
            fmt="none",
            capsize=0.0,
        )
        axis.errorbar(
            xval + 0.54,
            sampled_median_s,
            yerr=[err_down_s, err_up_s],
            ecolor="black",
            elinewidth=1,
            capthick=1,
            fmt="none",
            capsize=0.0,
        )
    # axis.legend()
    # axis.set_yscale('log')
    # axis.set_ylim(5e-2, 3.0001e-1)
    axis.set_xticks([])
    # axis.set_yticks([.05, .1, .2])
    # axis.set_xticklabels(xlabels, rotation='vertical')
    # axis.set_yticklabels(ylabels)
    ylim = axis.get_ylim()
    ylim_new = [0.0, ylim[1]]
    axis.set_ylim(ylim_new)
    axis.set_xlim([min(xval - 0.35), max(xval + 0.35 + 0.35)])

    axis.set_xlabel(r"$\mathbf{z}$", fontsize=12)
    axis.set_ylabel(r"$p_\mathrm{joint}(\mathbf{z})$", fontsize=12)


def supp_plot_training(
    axis,
    dkl_iter_value_p,
    dkl_final_p,
    dkl_iter_p,
    dkl_iter_value_s,
    dkl_final_s,
    dkl_iter_s,
):
    """
    Keywords:
        -- axis: axes object of the figure
        -- dkl_iter: x axes, i.e. vector for the iteration values
        -- dkl_iter_value: nupy matrix of the evolution of the DKL in iterations over several repetitions (in rows)
        -- dkl_final: in rows: DKL over time for several repetitions
    """

    # obtain the data fro the plots
    dkl_iter_median_p = np.median(dkl_iter_value_p, axis=0)
    dkl_iter_median_s = np.median(dkl_iter_value_s, axis=0)

    # Obtain the final DKL values
    final_dkl_median_p = np.median(dkl_final_p[:, -1]) * np.ones(len(dkl_iter_p))
    final_dkl_median_s = np.median(dkl_final_s[:, -1]) * np.ones(len(dkl_iter_s))

    # Do the plotting
    linewidth = 2.0
    axis.plot(
        dkl_iter_p,
        dkl_iter_median_p,
        color="tab:blue",
        linewidth=linewidth,
        label="Poisson training",
    )
    axis.fill_between(
        dkl_iter_p,
        np.percentile(dkl_iter_value_p, 25, axis=0),
        np.percentile(dkl_iter_value_p, 75, axis=0),
        color="tab:blue",
        alpha=0.5,
        linewidth=0.0,
    )

    axis.plot(
        dkl_iter_p,
        final_dkl_median_p,
        color="tab:blue",
        linewidth=linewidth,
        label="Poisson test",
        linestyle="--",
    )

    axis.plot(
        dkl_iter_s,
        dkl_iter_median_s,
        color="tab:orange",
        linewidth=linewidth,
        label="RN training",
    )
    axis.fill_between(
        dkl_iter_s,
        np.percentile(dkl_iter_value_s, 25, axis=0),
        np.percentile(dkl_iter_value_s, 75, axis=0),
        color="tab:orange",
        alpha=0.5,
        linewidth=0.0,
    )

    axis.plot(
        dkl_iter_s,
        final_dkl_median_s,
        color="tab:orange",
        linewidth=linewidth,
        label="RN test",
        linestyle="--",
    )

    axis.set_yscale("log")
    axis.set_ylabel(
        r"$\mathregular{D}_\mathregular{KL} \left[ \, p(\mathbf{z}) \, || \, p\!^*(\mathbf{z}) \, \right]$",
        fontsize=12,
    )
    axis.set_xlabel(r"# iteration [1]", fontsize=12)


def supp_plot_dkl_time(
    axis, dkl_time_array_p, dkl_time_value_p, dkl_time_array_s, dkl_time_value_s
):
    """
    Keywords:
        -- dkl_time_value: in rows: dkl_ over time for several repetitions
        -- dkl_time_array: time array corresponding to the dkl_ evaluations
    """

    # obtain the data fro the plots
    dkl_median_p = np.median(dkl_time_value_p, axis=0)
    dkl_75_p = np.percentile(dkl_time_value_p, 75, axis=0)
    dkl_25_p = np.percentile(dkl_time_value_p, 25, axis=0)
    dkl_median_s = np.median(dkl_time_value_s, axis=0)
    dkl_75_s = np.percentile(dkl_time_value_s, 75, axis=0)
    dkl_25_s = np.percentile(dkl_time_value_s, 25, axis=0)

    # Do the plotting
    linewidth = 2.0
    axis.plot(
        dkl_time_array_p,
        dkl_median_p,
        color="tab:blue",
        linewidth=linewidth,
        label="Poisson",
    )
    axis.fill_between(
        dkl_time_array_p, dkl_25_p, dkl_75_p, color="tab:blue", alpha=0.5, linewidth=0.0
    )

    axis.plot(
        dkl_time_array_s,
        dkl_median_s,
        color="tab:orange",
        linewidth=linewidth,
        label="RN",
    )
    axis.fill_between(
        dkl_time_array_s,
        dkl_25_s,
        dkl_75_s,
        color="tab:orange",
        alpha=0.5,
        linewidth=0.0,
    )

    axis.set_yscale("log")
    axis.set_xscale("log")
    axis.set_ylabel(
        r"$\mathregular{D}_\mathregular{KL} \left[ \, p(\mathbf{z}) \, || \, p\!^*(\mathbf{z}) \, \right]$",
        fontsize=12,
    )
    axis.set_xlabel(r"$t$ [ms]", fontsize=12)


def plot_itl_training(axis, abstract_ratio, class_ratio, iter_numb):
    """helper function to plot the in-the-loop training for both cases

    Keywords:
        --- axis: the axes object
        --- abstract_ratio: reference values for classification with abstract RBM in sofware.
        --- class_ratio: matrix with several repetitions, values for inference with hardware
        --- iter_numb: array of the iteration corresponding to the class_ratio

    """

    # Do the plotting
    cr_median = np.median(class_ratio, axis=0)
    cr_75 = np.percentile(class_ratio, 75, axis=0)
    cr_25 = np.percentile(class_ratio, 25, axis=0)
    a_median = np.median(abstract_ratio, axis=0)
    a_75 = np.percentile(abstract_ratio, 75, axis=0)
    a_25 = np.percentile(abstract_ratio, 25, axis=0)

    print(
        (
            "Abstract class ratio is: {0}+{1}-{2}".format(
                a_median, a_75 - a_median, a_median - a_25
            )
        )
    )
    print(
        (
            "Hardware class ratio is: {0}+{1}-{2}".format(
                cr_median[-1], cr_75[-1] - cr_median[-1], cr_median[-1] - cr_25[-1]
            )
        )
    )

    axis.plot(iter_numb, cr_median, linewidth=1.5, color="xkcd:black", label="hardware")
    axis.fill_between(
        iter_numb,
        cr_25,
        cr_75,
        color="xkcd:black",
        alpha=0.2,
        linewidth=0.0,
    )

    axis.set_ylabel("classification ratio [1]")
    axis.set_xlabel("number of iterations [1]")
    # axis.set_ylim([np.min(class_ratio) - 0.05, 1.05])
    axis.set_ylim([0.0, 1.05])
    # axis.grid(True)
    xmin = min(iter_numb)
    xmax = max(iter_numb)
    axis.axhline(
        y=a_median, xmin=xmin, xmax=xmax, linewidth=2, color="r", label="software"
    )
    x_array = np.linspace(xmin, xmax)
    y_array = np.ones(len(x_array))
    axis.fill_between(
        x_array, a_75 * y_array, a_25 * y_array, color="r", alpha=0.2, linewidth=0.0
    )


def plot_itl_training_error(axis, abstract_ratio, class_ratio, iter_numb):
    """helper function to plot the in-the-loop training for both cases

    Keywords:
        --- axis: the axes object
        --- abstract_ratio: reference values for classification with abstract RBM in sofware.
        --- class_ratio: matrix with several repetitions, values for inference with hardware
        --- iter_numb: array of the iteration corresponding to the class_ratio

    """

    # Do the plotting
    error_ratio = 1.0 - class_ratio
    error_abstract = 1.0 - abstract_ratio
    cr_median = np.median(error_ratio, axis=0)
    cr_75 = np.percentile(error_ratio, 75, axis=0)
    cr_25 = np.percentile(error_ratio, 25, axis=0)
    a_median = np.median(error_abstract, axis=0)
    a_75 = np.percentile(error_abstract, 75, axis=0)
    a_25 = np.percentile(error_abstract, 25, axis=0)

    print(
        (
            "Abstract error ratio is: {0}+{1}-{2}".format(
                a_median, a_75 - a_median, a_median - a_25
            )
        )
    )
    print(
        (
            "Hardware error ratio is: {0}+{1}-{2}".format(
                cr_median[-1], cr_75[-1] - cr_median[-1], cr_median[-1] - cr_25[-1]
            )
        )
    )

    axis.plot(iter_numb, cr_median, linewidth=2, color="xkcd:black", label="hardware")
    axis.fill_between(
        iter_numb,
        cr_25,
        cr_75,
        color="xkcd:black",
        alpha=0.2,
        linewidth=0.0,
    )

    axis.set_ylabel("error ratio [1]", fontsize=12)
    axis.set_xlabel("number of iterations [1]", fontsize=12)
    # axis.set_ylim([np.min(class_ratio) - 0.05, 1.05])
    axis.set_ylim([-0.01, 0.25])
    # axis.grid(True)
    xmin = min(iter_numb)
    xmax = max(iter_numb)
    axis.axhline(
        y=a_median,
        xmin=xmin,
        xmax=xmax,
        linewidth=2,
        linestyle="--",
        color="tab:brown",
        label="software",
    )
    # x_array = np.linspace(xmin, xmax)
    # y_array = np.ones(len(x_array))
    # axis.fill_between(x_array, a_75 * y_array, a_25 * y_array,
    #                 color='r', alpha=0.2, linewidth=0.0)


def plot_mixture_matrix(axis, mixture_matrix, labels):
    """
    auxiliary function to plot the mixture matrix

    Keywords:
        --- axis: the axes object
        --- mixture_matrix: the data for the mixture matrix
        --- labels: labels in the mixture matrix corresponding to classes

    """

    # Add a finite number to the otherwise zero values
    # to get around the logarithmic nan values
    # mixture_matrix[np.where(mixture_matrix==0)] += 1
    mixture_matrix = mixture_matrix / float(np.sum(mixture_matrix))

    # disc = np.max(mixture_matrix)
    fonts = {"fontsize": 10}
    tick_size = 8
    cmap = cm.get_cmap("gist_yarg")  # , disc)
    cmap.set_under((0.0, 0.0, 0.0))
    core.show_axis(axis)
    core.make_spines(axis)
    imge = axis.imshow(
        mixture_matrix, cmap=cm_gray_r, aspect=1.0, interpolation="nearest"
    )
    cax = inset_axes(
        axis,
        width="5%",  # width = 10% of parent_bbox width
        height="100%",  # height : 50%
        loc=3,
        bbox_to_anchor=(1.05, 0.0, 1, 1),
        bbox_transform=axis.transAxes,
        borderpad=0,
    )
    # f = ticker.ScalarFormatter(useOffset=False, useMathText=True)
    cbar = colorbar(imge, cax=cax, ticks=[0, 0.1, 0.2, 0.3], extend="both")
    cbar.ax.tick_params(labelsize=9)
    axis.set_ylabel("true label", **fonts)
    axis.set_xlabel("predicted label", **fonts)

    for location in ["top", "bottom", "left", "right"]:
        axis.spines[location].set_visible(True)
        axis.spines[location].set_linewidth(1.0)

    # Change the ticks to labels names
    axis.xaxis.set_major_locator(MaxNLocator(integer=True))
    axis.yaxis.set_major_locator(MaxNLocator(integer=True))
    axis.tick_params(length=0.0, pad=5)
    axis.set_xticks(np.arange(len(labels)))
    axis.set_xticklabels(labels, fontsize=tick_size)
    axis.set_yticks(np.arange(len(labels)))
    axis.set_yticklabels(labels, fontsize=tick_size)
    axis.tick_params(axis="both", which="minor")


def plot_visible(axis, image_vector, pic_size, label):
    """
    plot the visible layer using imshow

    Keywords:
        --- axis: axes object
        --- image_vector: numpy array of the visible units
        --- pic_size: size of the picute, tuple
        --- label: x label for the image

    """

    core.show_axis(axis)
    network = image_vector

    pic = np.reshape(network, pic_size)
    axis.imshow(pic, cmap=cm_gray_r, vmin=0.0, vmax=1.0, interpolation="nearest")
    axis.set_xticks([], [])
    axis.set_yticks([], [])
    axis.set_xlabel(label, labelpad=5)
    axis.set_adjustable("box-forced")


def plot_clamping(axis, clamping_vector, pic_size, label, mode="sandp"):
    """
    plot the clamping layer using imshow

    Keywords:
        --- axis: axes object
        --- clamping_vector: image vector with clampings
        --- pic_size: size of the picute, tuple
        --- label: x label for the image

    """

    core.show_axis(axis)

    clamping = clamping_vector
    clamp_mask = np.resize(clamping, pic_size)

    overlay = np.ma.masked_where((clamp_mask != -1), np.ones(clamp_mask.shape))
    indices = np.where(clamp_mask == -1)
    clamp_mask[indices] = 0.0
    cmap = cm_gray_r
    cmap.set_bad(color="w", alpha=0.0)
    axis.imshow(clamp_mask, cmap=cm_gray_r, vmin=0.0, vmax=1.0, interpolation="nearest")
    if mode == "sandp":
        cmap = plt.get_cmap("rainbow")
    elif mode == "patch":
        cmap = plt.get_cmap("Blues")
    else:
        sys.exit("Unknown mode specified in function plotClamping.")
    axis.imshow(
        overlay, cmap=cmap, vmin=0.0, vmax=1.0, alpha=0.9, interpolation="nearest"
    )
    axis.set_xticks([], [])
    axis.set_yticks([], [])
    axis.set_xlabel(label, labelpad=5)


def plot_label(axis, image_vector, labels, label):
    """
    plot the label layer using imshow

    Keywords:
        --- axis: axes object
        --- iamge_vector: activity of the label units
        --- pic_size: size of the picute, tuple
        --- labels: labels at the classification
        --- label: x label for the image

    """

    core.show_axis(axis)
    label_response = image_vector
    n_labels = len(label_response)
    pic_size_labels = (n_labels, 1)

    pic = np.reshape(label_response, pic_size_labels)
    axis.imshow(
        pic,
        cmap=cm_gray_r,
        vmin=0.0,
        vmax=1.0,
        interpolation="nearest",
        extent=(0.0, 1.0, -0.5, n_labels - 0.5),
    )

    axis.set_yticks(list(range(n_labels)))
    axis.set_yticklabels(labels, fontsize=6)
    axis.tick_params(width=0, length=0)
    axis.set_xticks([], [])
    axis.set_xlabel(label, labelpad=5)
    axis.set_adjustable("box-forced")


def plot_example_pictures(axis, original, pic_size_red, pic_size, grid, indices=None):
    """Plot an example picture"""
    indices = indices if indices is not None else list(range(200))
    # Layout specification
    n_vertical = grid[0]
    n_horizontal = grid[1]
    half = 3
    frame = 1

    # Do the actual plotting
    # create the picture matrix
    pic = (
        np.ones(
            (
                (2 * n_vertical + 1) * frame + 2 * n_vertical * pic_size[0] + half,
                (n_horizontal + 1) * frame + n_horizontal * pic_size[1],
            )
        )
        * 255
    )

    # Plot the upper 8 examples (originals)
    for counter in range(n_vertical * n_horizontal):
        i = counter % n_vertical
        j = int(counter / n_vertical)
        pic_vec = original[indices[counter], 1:]
        pic_counter = np.reshape(pic_vec, pic_size)

        pic[
            (i + 1) * frame + i * pic_size[0] : (i + 1) * frame + (i + 1) * pic_size[0],
            (j + 1) * frame + j * pic_size[1] : (j + 1) * frame + (j + 1) * pic_size[1],
        ] = pic_counter

    # Plot the lower 8 examples (reduced)
    for counter in range(n_vertical * n_horizontal):
        i = counter % n_vertical + 2
        j = int(counter / n_vertical)
        pic_vec = original[indices[counter], 1:]
        pic_counter = np.reshape(pic_vec, pic_size)
        pic_counter = resize(
            pic_counter,
            pic_size_red,
        )  # interp='nearest')
        median = np.percentile(pic_counter, 50)
        pic_counter = ((np.sign(pic_counter - median) + 1) / 2) * 255.0
        pic_counter = resize(
            pic_counter,
            pic_size,
        )  # interp='nearest')

        pic[
            (i + 1) * frame
            + half
            + i * pic_size[0] : (i + 1) * frame
            + (i + 1) * pic_size[0]
            + half,
            (j + 1) * frame + j * pic_size[1] : (j + 1) * frame + (j + 1) * pic_size[1],
        ] = pic_counter

    # Make the half line white
    lower = 3 * frame + 2 * pic_size[0]
    pic[lower : lower + half - 1, :] = 0

    axis.imshow(pic, cmap="Greys", aspect="equal")


def plot_tsne(axis, pics, pos, pic_size):
    """
    Make the tsne plot of pictures on a speicified axes object

        Keywords:
            --- axis: axes object
            --- X: matrix of the data, the images are in rows
            --- Y: position matrix of the data with tsne, the 2d coordinates are in rows
            --- pic_size: 2d Tuple, the size of the pictures
    """
    # Plot the pictures according to the coordinates
    for i, posi in enumerate(pos):
        cmap = cm_gray_r
        pic = np.reshape(pics[i], pic_size)
        img = cmap(np.ma.masked_array(pic, pic < 0.1))
        # img = cmap(pic)
        imagebox = OffsetImage(img, zoom=1.2, interpolation="nearest")
        xy_pos = (posi[0], posi[1])
        an_bo = AnnotationBbox(
            imagebox, xy_pos, boxcoords="data", pad=0.05, frameon=False
        )
        an_bo.zorder = 1
        axis.add_artist(an_bo)

    # make the lines connecting the images
    axis.scatter(pos[:, 0], pos[:, 1], 20, "w", alpha=0)
    axis.set_xticks([])
    axis.set_yticks([])
    axis.plot(
        pos[:, 0],
        pos[:, 1],
        linewidth=0.1,
        linestyle="-",
        color="black",
        alpha=0.45,
        zorder=0,
    )


def plot_mse(axis, time_array, patch, sand_p, patch_abstract, sandp_abstract):
    """
    Convenience function to plot the mse plots

    Keywords:
        --- axis: axes object
        --- time_array: time_array
        --- patch: Mse matrix for the patch occlusion
        --- sand_p: Mse matrix for the salt and pepper occlusion
    """

    # Set up the plot
    core.show_axis(axis)
    core.make_spines(axis)

    # set up the data
    datas = [patch, sand_p, patch_abstract, sandp_abstract]
    labels = ["Patch HW", "S&P HW", "Patch SW", "S&P SW"]
    colors = ["tab:blue", "tab:red", "tab:blue", "tab:red"]
    dash_style = [[], [], (0, [1, 3]), (2, [1, 3])]
    time_array = time_array - 150.0

    # do the plotting
    for index in range(2):
        data = datas[index]

        median = np.median(data, axis=0)
        value75 = np.percentile(data, 75, axis=0)
        value25 = np.percentile(data, 25, axis=0)
        axis.plot(
            time_array, median, linewidth=1.5, color=colors[index], label=labels[index]
        )

        axis.fill_between(
            time_array,
            value25,
            value75,
            color=colors[index],
            alpha=0.2,
            linewidth=0.0,
        )

    for index in range(2, 4):
        data = datas[index]

        median = np.median(data, axis=0)
        value75 = np.percentile(data, 75, axis=0)
        value25 = np.percentile(data, 25, axis=0)
        axis.plot(
            time_array,
            np.ones(len(time_array)) * median,
            linewidth=1.5,
            color=colors[index],
            label=labels[index],
            ls=dash_style[index],
        )

        axis.fill_between(
            time_array,
            value25 * np.ones(len(time_array)),
            value75 * np.ones(len(time_array)),
            color=colors[index],
            alpha=0.2,
            linewidth=0.0,
        )

    # annotate the plot
    axis.set_xlabel(r"$t$ [ms]", labelpad=5, fontsize=12)
    axis.set_ylabel("mean squeared error [1]", fontsize=12)
    axis.set_xlim([-40.0, 140.0])
    axis.set_ylim([0.0, 0.55])
    axis.legend(fontsize=8, loc=1)


def plot_error_time(
    axis, time_array, patch, sand_p, reference, patch_abstract, sandp_abstract
):
    """
    Convenience function to plot the mse plots

    Keywords:
        --- axis: axes object
        --- time_array: time_array
        --- patch: error matrix for the patch occlusion
        --- sand_p: error matrix for the salt and pepper occlusion
    """

    # Set up the plot
    core.show_axis(axis)
    core.make_spines(axis)

    # set up the data
    datas = [patch, sand_p, patch_abstract, sandp_abstract, reference]
    labels = ["Patch HW", "S&P HW", "Patch SW", "S&P SW", "HW ref"]
    colors = ["tab:blue", "tab:red", "tab:blue", "tab:red", "xkcd:black"]
    dash_style = [[], [], (0, [1, 3]), (2, [1, 3])]
    # width = [1., 1., 1.5, 1.5, 1.]
    time_array = time_array - 150.0

    # do the plotting
    for index in range(2):
        data = datas[index]
        error = 1.0 - np.mean(data, axis=0)
        axis.plot(
            time_array, error, linewidth=1.5, color=colors[index], label=labels[index]
        )

    for index in range(2, 4):
        data = datas[index]

        median = 1.0 - np.median(data, axis=0)
        # value75 = 1. - np.percentile(data, 75, axis=0)
        # value25 = 1. - np.percentile(data, 25, axis=0)
        axis.plot(
            time_array,
            np.ones(len(time_array)) * median,
            linewidth=1.5,
            color=colors[index],
            label=labels[index],
            ls=dash_style[index],
        )

    # With the index 4
    data = datas[4]
    error = 1.0 - np.mean(data, axis=0)
    axis.plot(
        time_array,
        error,
        linewidth=1.5,
        color=colors[4],
        label=labels[4],
        linestyle="--",
    )

    # annotate the plot
    axis.set_xlabel(r"$t$ [ms]", labelpad=5, fontsize=12)
    axis.set_ylabel("error ratio [1]", fontsize=12)
    axis.set_xlim([-40.0, 140.0])
    axis.set_ylim([0.0, 0.86])
    axis.legend(fontsize=8, loc=1)


def plot_psps(axis, time_array, v_array, normed=False):
    """
    Plot the measured PSPs

    Keywords:
        --- axis: axes object
        --- time_array: matrix with the time in the rows
        --- v_array: matrix with voltages in the rows
    """

    # Set up the plot
    core.show_axis(axis)
    core.make_spines(axis)

    # do the plotting
    for index in range(len(v_array[:, 0])):
        if normed:
            memb_pot = v_array[index, :] / np.max(v_array[index, :])
            # if np.max(v_array[index,:]) < 0.05:
            #     continue
        else:
            memb_pot = v_array[index, :]
        axis.plot(
            time_array[index, :], memb_pot, linewidth=1.0, alpha=0.2, color="tab:blue"
        )
    axis.set_xlabel(r"t [ms]")
    axis.set_ylabel(r"memb. potential [mV]")
    axis.set_xlim([-10.0, 75.0])


def plot_box_plot(axis, data):
    """plot a box plot"""

    # plot
    datapoints = len(data)
    # b1 = axis.boxplot(data[0],
    #                 sym='x',
    #                 positions=[0],
    #                 widths=0.5,
    #                 boxprops={'facecolor': 'tab:red'},
    #                 patch_artist=True)
    axis.boxplot(data[1:], sym="x", widths=0.5, positions=list(range(1, datapoints)))
    axis.set_xlim([-0.6, datapoints - 0.4])
    axis.set_yscale("log")
    axis.set_ylabel(
        r"$\mathregular{D}_\mathregular{KL} \left[ \, p(\mathbf{z}) \, || \, p\!^*(\mathbf{z}) \, \right]$",
        fontsize=12,
    )
    axis.set_xlabel(r"# Distribution ID", fontsize=12)


def plot_frame(ax,
               extent_left=0.18,
               extent_right=0.10,
               extent_top=0.20,
               extent_bottom=0.25,
               frame_instead_background=False,
               fill_col="#f2f2f2",
               ):
    if frame_instead_background:
        val_fill = False
        val_ec = 'black'
    else:
        val_fill = True
        val_ec = None

    fancybox = mpatches.Rectangle(
        (-extent_left, -extent_bottom),
        1 + extent_left + extent_right, 1 + extent_bottom + extent_top,
        facecolor=fill_col, fill=val_fill, alpha=1.00,  # zorder=zorder,
        transform=ax.transAxes,
        ec=val_ec,
        zorder=-3)
    plt.gcf().patches.append(fancybox)


def add_colorbar(im, label, aspect=15, pad_fraction=1.7, **kwargs):
    """Add a vertical color bar to an image plot."""
    divider = axes_grid1.make_axes_locatable(im.axes)
    width = axes_grid1.axes_size.AxesY(im.axes, aspect=1. / aspect)
    pad = axes_grid1.axes_size.Fraction(pad_fraction, width)
    current_ax = plt.gca()
    cax = divider.append_axes("right", size=width, pad=pad)
    plt.sca(current_ax)
    cb = im.axes.figure.colorbar(im, cax=cax, **kwargs)
    cb.set_label(label)


def add_colorbar_below(im, label, aspect=15, pad_fraction=5.0, **kwargs):
    """Add a vertical color bar to an image plot."""
    divider = axes_grid1.make_axes_locatable(im.axes)
    width = axes_grid1.axes_size.AxesX(im.axes, aspect=1. / aspect)
    pad = axes_grid1.axes_size.Fraction(pad_fraction, width)
    current_ax = plt.gca()
    cax = divider.append_axes("bottom", size=width, pad=pad)
    plt.sca(current_ax)
    cb = im.axes.figure.colorbar(im, cax=cax, orientation='horizontal', **kwargs)
    cb.set_label(label)
