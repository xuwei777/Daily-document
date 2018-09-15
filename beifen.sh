#!/bin/bash
find /tmp/quanbei/ -daystart -mtime +1 -name * -exec rm -rf {} \;

innobackupex --user=root --password=123 --no-timestamp /tmp/quanbei/`date "+%F"`_qb
wait
innobackupex --incremental /tmp/zhenbei/ --incremental-basedir=$qb --user=admin --password=Admin.1root 

nnobackupex --apply-log --redo-only /tmp/quanbei/`date '+%F'`_qb


#* * */3 * *
