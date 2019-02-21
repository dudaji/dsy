#!/usr/bin/python
# -*- coding: UTF-8 -*-
# LinkedList 에서 delete를 주어진 값만큼 건너 뛰어서 함
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


  def list_count(self):
    return self.count


  def delete_next(self, next_cnt):

    tar_node = self.current

    for i in range(next_cnt-1):
      tar_node = tar_node.next

    prev_node = tar_node.prev
    next_node = tar_node.next

    prev_node.next = next_node
    next_node.prev = prev_node

    self.current = next_node
    self.count -= 1

    return tar_node.data

 
cnt, gap = map(int, sys.stdin.readline().strip().split())
 
linked_list = LinkedList()

for i in range(1, cnt+1):
  linked_list.insert(str(i))


result_list = []
while not linked_list.list_count() == 0 :
  result_list.append(str(linked_list.delete_next(gap)))

result = ", ".join(map(str, result_list))
sys.stdout.write("<{}>".format(result))