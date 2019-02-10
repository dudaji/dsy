#!/usr/bin/python
# -*- coding: UTF-8 -*-
# bubble
# 1-2 > 2-3 > 3-4
# 1-2 > 2-3
# 1-2

def sort_bubble_start(arr):
  
  # print arr
  return sort_bubble(arr, len(arr))

def sort_bubble(arr, arr_size):

  if arr_size < 2:
    # print arr
    return arr

  for i in range(arr_size-1):
    if arr[i] > arr[i + 1]:
      arr[i], arr[i + 1] = arr[i + 1], arr[i]
    # print arr 

  return sort_bubble(arr, arr_size-1)



def sort_select(arr):
  
  # print arr
  arr_size = len(arr)

  for i in range(arr_size):
    
    min_index = i

    for j in range(arr_size - i):
      tar_index = j + i
      if arr[tar_index] < arr[min_index]:
        min_index = tar_index

    if i != min_index:
      arr[i], arr[min_index] = arr[min_index], arr[i]
    
    # print arr

  return arr


def sort_insert(arr):

  arr_size = len(arr)
  for i in range(arr_size):
    j = i - 1
    tar_index = i
    while j > -1:
      if arr[j] > arr[tar_index]:
        arr[tar_index], arr[j] = arr[j], arr[tar_index]
        tar_index = j
        print arr
      j -= 1

  return arr