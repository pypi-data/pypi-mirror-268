#!/usr/bin/env python
"""making plotting of multipanel plots easier with dedicated gridspec use"""

from setuptools import setup, find_packages

VERSION = "0.2.2"

setup(
    name="Gridspeccer",
    version=VERSION,
    description="Helper scripts to organize multi-figure plots.",
    author="Oliver Breitwieser",
    author_email="oliver.breitwieser@kip.uni-heidelberg.de",
    url="https://github.com/gridspeccer/gridspeccer",
    #  packages=find_packages(include=['gridspeccer', 'gridspeccer.*']),
    packages=["gridspeccer"],
    entry_points={"console_scripts": ["gridspeccer = gridspeccer.cli:plot"]},
    package_data={
        "gridspeccer": ["defaults/matplotlibrc", "defaults/tex_matplotlibrc"],
    },
    include_package_data=True,
    license="GNUv3",
    zip_safe=True,
    install_requires=["matplotlib", "scikit-image"],
)
