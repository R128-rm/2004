# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:day01
# File_name:jiu.py
# Author: xin
# Time:2020年09月04日

九九乘法表
for l in range(1,10):
    for y in range(1, l + 1):
        print(f'{y}*{l}={y*l}',end="\t")
    print()
