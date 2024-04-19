#!/usr/bin/env python
# encoding: utf-8
"""CLI interface to the gridspeccer"""

from . import core
from .core import log
import argparse
import glob
import os
import os.path as osp
import sys
import matplotlib as mpl

from pathlib import Path

sys.path.insert(0, osp.dirname(osp.abspath(__file__)))


def plot():
    """plot a figure"""
    parser = argparse.ArgumentParser(
        prog="gridspeccer",
        description="Plotting tool for easier positioning.",
    )
    parser.add_argument(
        "--filetype",
        help="Filetype suffix for saving, for supported types check matplotlib but certainly .pdf and .png.",
        default=".pdf",
    )
    parser.add_argument(
        "--mplrc",
        help="Location of a matplotlibrc to be used.",
        default=osp.join(
            osp.dirname(osp.abspath(__file__)), "defaults", "matplotlibrc"
        ),
    )
    parser.add_argument(
        "--loglevel",
        help="Display more or less info.",
        type=str,
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        default="INFO",
    )
    parser.add_argument(
        "--output-folder",
        help="Folder to output into, default is `../fig`.",
        type=str,
        default="../fig",
    )
    parser.add_argument(
        "data",
        nargs="*",
        help="files to look at and folders to look through for fig*.py files",
    )
    args = parser.parse_args()
    if not osp.isfile(args.mplrc):
        raise IOError(
            f"The 'mplrc' argument ('{args.mplrc}') has to be an existing file"
        )
    log.setLevel(args.loglevel)

    mpl.rc_file(args.mplrc)

    if len(args.data) == 0:
        print("no data given, looking for all fig*.py files in the working directory")
        args.data = ["."]

    plotscripts = []
    for fname in args.data:
        if osp.isdir(fname):
            plotscripts.extend(glob.glob(osp.join(fname, "fig*.py")))
        elif osp.isfile(fname):
            plotscripts.append(fname)
        else:
            raise IOError(
                f"all data given have to be folder or files that exist, '{fname}' does not"
            )

    main_wd = os.getcwd()
    for name in plotscripts:
        log.info("-- processing file %s --", name)
        # always get back to main working directory
        os.chdir(main_wd)
        if osp.dirname(name) != "":
            os.chdir(osp.dirname(name))
        core.make_figure(
            osp.splitext(osp.basename(name))[0],
            folder=Path(args.output_folder),
            filetype=args.filetype
        )


if __name__ == "__main__":
    from inspect import isfunction, getargspec

    local_globals = list(globals().keys())

    def is_noarg_function(fun):
        "Test if f is valid function and has no arguments"
        func = globals()[fun]
        if isfunction(func):
            argspec = getargspec(func)
            if (
                len(argspec.args) == 0
                and argspec.varargs is None
                and argspec.keywords is None
            ):
                return True
        return False

    def show_functions():
        "show all functions"
        functions.sort()
        for fun in functions:
            print(fun)

    functions = [fun for fun in local_globals if is_noarg_function(fun)]
    if len(sys.argv) <= 1 or sys.argv[1] == "-h":
        show_functions()
    else:
        for launch in sys.argv[1:]:
            if launch in functions:
                run = globals()[launch]
                run()
            else:
                print((launch, "not part of functions:"))
                show_functions()
