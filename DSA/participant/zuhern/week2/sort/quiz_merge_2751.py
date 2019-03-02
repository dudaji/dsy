# https://www.acmicpc.net/problem/2751

import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline().strip())
arr = []

for _ in range(0, n):
  arr.append(int(sys.stdin.readline().strip()))

######################################################################

def sort_merge_start(arr):
  sort_arr = arr[:]
  sort_merge(sort_arr, 0, len(arr)-1)
  return sort_arr

def sort_merge(sort_arr, start_index, end_index):
  
  if len(sort_arr[start_index:end_index+1]) < 2:        
    return

  mid_index = (start_index + end_index) // 2          

  sort_merge(sort_arr, start_index, mid_index)
  sort_merge(sort_arr, mid_index+1, end_index)

  merge(sort_arr, start_index, mid_index, end_index)


def merge(sort_arr, start_index, mid_index, end_index):

  front_arr = sort_arr[start_index:mid_index+1]
  back_arr = sort_arr[mid_index+1:end_index+1]

  front_index = 0
  back_index = 0

  tar_index = start_index

  while front_index < len(front_arr) and back_index < len(back_arr):

    front_val = front_arr[front_index]
    back_val = back_arr[back_index]

    if front_val < back_val:
      front_index += 1
      sort_arr[tar_index] = front_val
    else:
      back_index += 1
      sort_arr[tar_index] = back_val

    tar_index += 1

  if (front_index != len(front_arr)) :
    ## 이부분 시간이 오래 걸림 바꿔야함
    sort_arr[tar_index:end_index+1] = front_arr[front_index:len(front_arr)]


######################################################################

result = sort_merge_start(arr)

for i in result:
    print(i)
