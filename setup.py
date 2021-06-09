# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wdiff",
    version="0.0.8",
    author="Mario E. Bermonti Perez",
    author_email="mbermonti1132@gmail.com",
    description="Package for analyzing word difficulty in Spanish",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mario-bermonti/wdiff",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ],
    install_requires=[
            'pandas',
        ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
