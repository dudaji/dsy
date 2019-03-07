# https://www.acmicpc.net/problem/11931
# 시간 초과

import sys
sys.setrecursionlimit(1000000)

n = int(input())
arr = []

for _ in range(0, n):
  arr.append(int(input()))

######################################################################

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


######################################################################

result = sort_quick_start(arr)

for i in result:
    print(i)
