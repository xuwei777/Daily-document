#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
info = {}
name = input("请输入你的名字:")
age = input("请输入你的年龄:")
info["name"] = name
info["age"] = age
#print(info.items())
for i,n in info.items():
    print("%s--->%s" %(i,n))

