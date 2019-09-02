# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xyplot",
    version="0.1.2",
    author="xypnox",
    author_email="xypnox@gmail.com",
    description="Plotting with python made easy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xypnox/xyplot",
    packages=setuptools.find_packages(),
    install_requires=['matplotlib', 'numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
)
