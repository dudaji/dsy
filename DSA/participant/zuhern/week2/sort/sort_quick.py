#!/usr/bin/python
# -*- coding: UTF-8 -*-

# O(nlogn)
# worst O(n^2)
def sort_quick_start(arr):
  sort_quick(arr, 0, len(arr)-1)
  return arr


def sort_quick(arr, start_index, end_index):
  
  if end_index <= start_index:
    return
  
  partition_index = partition(arr, start_index, end_index)

  if start_index < (partition_index-1):
    sort_quick(arr, start_index, partition_index-1)

  if partition_index < end_index:
    sort_quick(arr, partition_index, end_index)

# 마지막 정렬 지점을 partition 위치로 리턴
# start_index < end_index 이어야한다.
def partition(arr, start_index, end_index):

  pivot_index = (start_index + end_index) // 2
  pivot_value = arr[pivot_index]

  while start_index < end_index:

    while start_index < end_index and arr[start_index] < pivot_value:
      start_index += 1

    while start_index < end_index and pivot_value < arr[end_index]:
      end_index -= 1

    arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
    start_index += 1
    end_index -= 1

  return start_index


