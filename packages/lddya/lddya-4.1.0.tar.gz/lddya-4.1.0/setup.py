#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: lidongdong
# Mail: 927052521@qq.com
# Created Time: 2022.10.21  19.50
############################################


from setuptools import setup, find_packages

setup(
    name = "lddya",
    version = "4.1.0",
    keywords = {"pip", "license","licensetool", "tool", "gm"},
    description = "1.Map添加生成随机地图的功能，仅提供生成，暂不提供验证，也就是可能会产生无路径的极端情况。2.添加动态规划法。",
    long_description = "具体功能，请自行挖掘。",
    license = "MIT Licence",

    url = "https://github.com/not_define/please_wait",
    author = "lidongdong",
    author_email = "927052521@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['numpy','matplotlib','pygame','pandas']
)
