#!/usr/bin/python
# -*- coding: UTF-8 -*-
# LinkedList 에서 delete를 현재 current 값만 함
import sys

class Node:
  def __init__(self, initdata):
    self.data = initdata
    self.next = None
    self.prev = None


class LinkedList():
  
  def __init__(self):

    self.next = None
    self.last = None
    self.current = None
    self.head = None
    self.count = 0

  def insert(self, value):
    
    new_node = Node(value)

    if self.head is None:
      new_node.prev = new_node
      new_node.next = new_node
      self.head = new_node
      self.current = new_node
    else:
      new_node.next = self.head
      new_node.prev = self.last

      self.head.prev = new_node
      self.last.next = new_node

    self.last = new_node
    self.last = new_node
    self.count += 1

    return self.current
    
  def deleteCurrent(self):

    tar_node = self.current
    prev_node = tar_node.prev
    next_node = tar_node.next

    if self.head is self.current:
      self.head = next_node
    
    if self.last is self.current:
      self.last = prev_node

    prev_node.next = next_node
    next_node.prev = prev_node

    self.current = next_node
    self.count -= 1

    return tar_node

  def getCurrent(self):
    return self.current
  
  def getNext(self):
    self.current = self.current.next
    return self.current

  def listCount(self):
    return self.count
 
cnt, gap = map(int, sys.stdin.readline().strip().split())
 
linked_list = LinkedList()

for i in range(1, cnt+1):
  linked_list.insert(str(i))

result_list = []
while not linked_list.listCount() == 0 :
  for i in range(gap-1):
    linked_list.getNext()
  result_list.append(str(linked_list.deleteCurrent().data))
result = ", ".join(map(str, result_list))
sys.stdout.write("<{}>".format(result))