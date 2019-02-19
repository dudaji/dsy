#!/usr/bin/python
# -*- coding: UTF-8 -*-
# https://www.acmicpc.net/problem/4740
# 출령 형식이 잘못되었다고 통과 못함..

import sys

class ArrayStack():

  def __init__(self):
    self.stack = {}
    self.last = 0

  def push(self, data):
    self.stack[self.last] = data
    self.last += 1 

  def pop(self):
    return_data = self.stack[self.last]
    self.last -= 1 
    return_data = None
    return return_data

  def size(self):
    return self.last

  def empty(self):
    return self.last if self.last == 0 else -1

  def top(self):
    return_data = self.stack[self.last]
    return return_data if self.empty() else -1


stack_obj = ArrayStack()

count = int(input())

for i in range(count):
  cmd = input()
    
  if "push" in cmd:
    num = int(cmd[5:])
    stack_obj.push(num)
    continue
  else:
    func = getattr(stack_obj, cmd)
    result = func()
  print(result)





# def call(func_name, value):

#   try:
#     func = getattr(stack_obj, func_name)
#     func(value)
#   except EOFError:
#     return


# while True:
#   try:
#     input_arr = sys.stdin.readline().strip().split()
#     func_name = input_arr[0]
#     value = input_arr[1]
#     call(func_name, value)
#   except EOFError:
#     break
#   input_str = str(sys.stdin.readline().strip())
