#!/bin/bash
read -p "请输入一个ip地址：" xuwei
echo $xuwei |grep -E "^(([0-9]{1,2}|1[0-9][0-9]|2[0-4][0-9]|25[0-4])\.){3}([1-9]{1,2}|1[0-9][1-9]|2[0-4][1-9]|25[0-4])$" &>/dev/null
[ $? = 0 ] && echo "这个ip合法" || echo "这个ip不合法"
