#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
x = input("请输入用户名:")
w = input("请输入密码:")
s = 1
while s < 3:
    if x == "tom" and w == "123":
        print("登陆成功")
        break
    else:
        print("密码错误，请重新输入:")
        x = input("请输入用户名:")
        w = input("请输入密码:")
        s = s + 1
else:
    print("输入错误3次，登陆失败")
    # if s > 2:
    #     print("密码错3次，登陆失败")
    #     break
