#!/usr/bin/python
# -*- coding: UTF-8 -*-
# bubble
# 1-2 > 2-3 > 3-4
# 1-2 > 2-3
# 1-2

def sort_bubble_start(arr):
  
  return sort_bubble(arr, len(arr))

def sort_bubble(arr, arr_size):

  if arr_size < 2:
    return arr

  for i in range(arr_size-1):
    if arr[i] > arr[i + 1]:
      arr[i], arr[i + 1] = arr[i + 1], arr[i]

  return sort_bubble(arr, arr_size-1)



def sort_select(arr):
  
  arr_size = len(arr)

  for i in range(arr_size):
    
    min_index = i

    for j in range(arr_size - i):
      tar_index = j + i
      if arr[tar_index] < arr[min_index]:
        min_index = tar_index

    if i != min_index:
      arr[i], arr[min_index] = arr[min_index], arr[i]
    
  return arr


def sort_insert(arr):

  arr_size = len(arr) - 1

  for i in range(arr_size):
    
    start_index = i + 1
    tar_val = arr[start_index]
    j = start_index

    while j > 0 and tar_val < arr[j-1]:
      arr[j] = arr[j-1]
      j -= 1

    arr[j] = tar_val
    
  return arr