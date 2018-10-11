#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
ywj = '/usr/bin/ls'
mbwj = '/root/list'

r_ywj = open(ywj,'rb')
w_mbwj = open(mbwj,'wb')
buffer_size = 4096

while True:
    sj = r_ywj.read()
    if not sj:
        break
    w_mbwj.write(sj)

r_ywj.close()
w_mbwj.close()
