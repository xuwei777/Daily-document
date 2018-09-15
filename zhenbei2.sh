#!/bin/bash
find /tmp/zhenbei/ -daystart -type d -mtime +1 rm -rf {} \;
zb2=$(find /tmp/zhenbei/ -daystart -name "`date '-d -1day' '+%F'`*")
innobackupex --incremental --no-timestamp /tmp/zhenbei/`date '+%F'`_zb --incremental-basedir=$zb2 --user=admin --password=Admin.1root


#* * */1 * *
