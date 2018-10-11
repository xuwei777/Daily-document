#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
sum = 0
for i in range(1,10):
    for x in range(1,i+1):
        print("%s x %s = %s" %(x,i,x * i),end = "  ")
    print()

