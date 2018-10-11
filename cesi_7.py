#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
import sys
for i in range(1,10):
    if i == 3:
        continue
    if i == 5:
        pass
    if i == 8:
        sys.exit()
    print(i)
else:
    print("end")
