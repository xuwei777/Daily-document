#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
try:
    with open("xxx","r") as f1:
        for i in f1.readlines():
            print(i)
except FileNotFoundError as w:
    print(w,"文件路径错误，文件不存在")
