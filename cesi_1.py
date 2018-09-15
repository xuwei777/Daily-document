#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
cj = int(input("请输入成绩："))
if cj >= 90:
    print("A")
    print("好成绩")
elif cj >= 80:
    print("B")
    print("不错")
elif cj >= 70:
    print("C")
    print("努力")
else:
    print("D")
    print("不及格")