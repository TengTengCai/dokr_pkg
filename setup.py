#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-05-25 17:04
# @Author  : TengTengCai
# @File    : setup.py
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dokr',
    version='0.1',
    scripts=['dokr'] ,
    author="TengTengCai",
    author_email="1021766585@qq.com",
    description="A Docker and AWS utility package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TengTengCai/dokr_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)