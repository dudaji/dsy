#!/usr/bin/python
# -*- coding: UTF-8 -*-
# https://www.acmicpc.net/problem/10828

import sys

class ArrayStack():

  def __init__(self):
    self.data = {}
    self.front_index = 0
    self.back_index = 0

  def push(self, data):
    self.back_index += 1 
    self.data[self.back_index] = data

  def pop(self):
    if (self.back_index == 0):
      return -1

    return_data = self.data[self.back_index]
    self.front_index += 1 
    return return_data

  def size(self):
    return self.back_index - self.front_index

  def empty(self):
    return 1 if self.size() == 0 else 0

  def front(self):    
    if (self.size() == 0):
      return -1
    return self.front_index

  def back(self): 
    if (self.size() == 0):
      return -1
    return self.back_index



stack_obj = ArrayStack()

n = int(sys.stdin.readline().strip())

for _ in range(0, n):
  cmd = sys.stdin.readline().strip()
    
  if "push" in cmd:
    num = int(cmd[5:])
    stack_obj.push(num)
    continue
  else:
    func = getattr(stack_obj, cmd)
    result = func()
  print(result)