#!/bin/bash
find /tmp/zhenbei/ -daystart -type d -mtime +1 rm -rf {} \;
qb=$(find /tmp/quanbei/ -name "`date -d '-1day' '+%F'`*")
qb_yy=$(find /tmp/quanbei/ -type d '*')
innobackupex --incremental --no-timestamp /tmp/zhenbei/`date '+%F'`_zb --incremental-basedir=$qb --user=root --password=123

innobackupex --apply-log --redo-only $qb_yy/ --incremental-dir=/tmp/zhenbei/tmp/zhenbei/`date '+%F'`_zb/
