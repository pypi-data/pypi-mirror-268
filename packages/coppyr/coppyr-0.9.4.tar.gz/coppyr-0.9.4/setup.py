#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from coppyr import (__title__, __summary__, __url__, __version__, __author__,
                    __email__, __license__)
from coppyr import package as pkg


setup(
    name=__title__,
    version=__version__,
    description=__summary__,
    long_description=pkg.get_readme("README.rst"),
    long_description_content_type="text/x-rst; charset=UTF-8",
    author=__author__,
    author_email=__email__,
    url=__url__,
    packages=find_packages(exclude=["tests", "tests.*"]),
    license=__license__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    cmdclass={"upload": pkg.UploadCommand},
    install_requires=[],
    extras_require=pkg.parse_extras(
        config="/opt/coppyr/requirements-config.txt",
        daemon="/opt/coppyr/requirements-daemon.txt",
        dev="/opt/coppyr/requirements-dev.txt",
        pkg="/opt/coppyr/requirements-pkg.txt"
    ),
    include_package_data=True  # Read MANIFEST.in
)
