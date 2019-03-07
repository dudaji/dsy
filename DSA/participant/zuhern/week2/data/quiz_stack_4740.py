#!/usr/bin/python
# -*- coding: UTF-8 -*-
# https://www.acmicpc.net/problem/4740
# 출령 형식이 잘못되었다고 통과 못함..

import sys

def printReverse(input_str):
  str_arr = list(input_str)
  result = ""
  while not len(str_arr) == 0:
    result += str(str_arr.pop())
  print(result)

input_str = str(sys.stdin.readline().strip())
while input_str != "***":
  printReverse(input_str)
  input_str = str(sys.stdin.readline().strip())