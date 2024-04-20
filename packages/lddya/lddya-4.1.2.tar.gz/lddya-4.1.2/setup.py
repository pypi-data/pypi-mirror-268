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
    version = "4.1.2",
    keywords = {"pip", "license","licensetool", "tool", "gm"},
    description = "*给Clock添加delta_t的变量。改一下AStar算法的start跟end的数据类型为np.array",
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
