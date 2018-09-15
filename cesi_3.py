#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
import getpass
#y = input("请输入结果[Yes |No]")
y = getpass.getpass("请输入结果[Yes |No]")
yn = y.lower()
if yn == "y" or yn == "yes":
    print("1")
elif yn  == "n" or yn == "no":
    print("2")
else:
    print("输入错误")
