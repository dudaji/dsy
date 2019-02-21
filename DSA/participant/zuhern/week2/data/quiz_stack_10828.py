#!/usr/bin/python
# -*- coding: UTF-8 -*-
# https://www.acmicpc.net/problem/10828

import sys

class ArrayStack():

  def __init__(self):
    self.data = {}
    self.last = 0

  def push(self, data):
    self.last += 1 
    self.data[self.last] = data

  def pop(self):
    if (self.last == 0):
      return -1

    return_data = self.data[self.last]
    self.last -= 1 
    return return_data

  def size(self):
    return self.last

  def empty(self):
    return 1 if self.last == 0 else 0

  def top(self):    
    if (self.last == 0):
      return -1
    return_data = self.data[self.last]
    return -1 if self.empty() else return_data


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