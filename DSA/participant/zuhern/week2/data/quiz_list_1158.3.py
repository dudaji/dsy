#!/usr/bin/python
# -*- coding: UTF-8 -*-
# array 로 구현
import sys

cnt, gap = map(int, sys.stdin.readline().strip().split())
 
tarList = []

for i in range(1, cnt+1):
  tarList.append(str(i))

remove_index = gap-1
result = '<'

while not len(tarList) == 0:
  result += str(tarList.pop(remove_index))
  if not len(tarList) == 0:
    result += ', '
    remove_index += (gap-1)
    # print("remove_index", remove_index, "len(tarList)", len(tarList))
    if remove_index > len(tarList)-1 :
      remove_index = remove_index % len(tarList)
  else:
    result += '>'
 
sys.stdout.write(result)