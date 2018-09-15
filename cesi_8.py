#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
x = """请输入您需要购买的物品编号:
1.水
2.可乐
3.冰红茶
请输入(1/2/3)"""

w = input(x)
while True:
    if w == "1":
        print("您购买了一瓶水")
        break
    elif w == "2":
        print("您购买了一瓶可乐")
        break
    elif w == "3":
        print("您购买了一瓶冰红茶")
        break
    else:
        print("输入错误，请重新输入:")
        w = input(x)