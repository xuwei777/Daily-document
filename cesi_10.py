#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
def nc():
    with open("/root/meminfo","r") as f4:
        for i in f4:
            if i.startswith("MemTotal:"):
                yl = int(i.split()[1]) / 1024 / 1024
            if i.startswith("MemFree:"):
                sy = int(i.split()[1]) / 1024 / 1024
    print("%.2fG - %.2fG = %.2fG" %(yl,sy,yl - sy))