#!/usr/bin/python
# -*- coding: UTF-8 -*-
# array 로 구현
import sys

cnt, gap = map(int, sys.stdin.readline().strip().split())
 
tarList = []

for i in range(1, cnt+1):
  tarList.append(str(i))

remove_index = gap-1
result_list = []

while not len(tarList) == 0:
  result_list.append(str(tarList.pop(remove_index)))
  if not len(tarList) == 0:
    remove_index += (gap-1)
    remove_index = remove_index % len(tarList)

result = ", ".join(map(str, result_list))
sys.stdout.write("<{}>".format(result))