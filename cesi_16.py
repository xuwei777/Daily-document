#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
def xuwei(x):
    try:
        if type(int(x)) == type(1):
            print("这是一个数字")
    except ValueError as w:
        print("输入的不是纯数字")
    return x

xuwei()