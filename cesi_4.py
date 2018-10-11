#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
import random
l1 = ['石头','剪刀','布']
l2 = ['石头','剪刀'],['剪刀','布'],['布','石头']
tishi ="""(0)石头
(1)剪刀
(2)布
请选择(0/1/2):"""
cwin = 0
pwin = 0
while cwin < 2 and pwin < 2:
    sr = input(tishi)
    while sr != "2" and sr != "1" and sr != "0":
        sr = input(tishi)
    xb = l1[int(sr)]
    dn = random.choice(l1)
    print("我选了：%s,电脑选了：%s" %(xb,dn))
    if xb == dn:
        print("\033[34;45;1m平局！\033[0m")
    elif [xb,dn] in l2:
        pwin = pwin + 1
        print("\033[34;45;1m你赢了1局！\033[0m")
    elif [xb,dn] not in l2:
        print("\033[34;45;1m你输了1局！\033[0m")
        cwin = cwin + 1


if pwin == 2:
    print("\033[38;46;1m你赢了!\033[0m")
else:
    print("\033[38;46;1m你输了!\033[0m")
