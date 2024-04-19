#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @time:2024/3/27 17:02
# Author:Zhang HongTao
# @File:setup.py

from setuptools import setup, find_packages

setup(
    name='python-core-ai-bnq',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        # 依赖项列表
        'structlog==23.1.0',
        'concurrent-log-handler==0.9.22',
        'nacos-sdk-python==0.1.12'
    ],
    # 其他元数据，如作者、描述等
    author='BNQ',
    description='Python core AI module for BNQ',
    url='',
)
