#!/usr/bin/python
# -*- coding: UTF-8 -*-

# O(nlogn)
def sort_merge_start(arr):
  sort_arr = arr[:]
  sort_merge(sort_arr, 0, len(arr)-1)
  return sort_arr

def sort_merge(sort_arr, start_index, end_index):
  
  # 최소 크기 사이즈가 되면 재귀 멈춤
  if (end_index - start_index) < 1:
    return

  mid_index = (start_index + end_index) // 2     

  sort_merge(sort_arr, start_index, mid_index)
  sort_merge(sort_arr, mid_index+1, end_index)

  merge(sort_arr, start_index, mid_index, end_index)


# 두 array 앞에서 부터 작은 숫자 먼저 꺼내어
# 하나의 array 로 merge
# start_index: 전체 array 기준으로 merge 대상의 start index
# mid_index:   전체 array 기준으로 merge 대상의 두 array 나눈 기준 index
# end_index:   전체 array 기준으로 merge 대상의 end index
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

  # 앞 array 에서 꺼내지지 않은 숫자들은
  # 앞뒤 array 합친 범위내에서
  # 마지막으로 정렬된 index 부터 끝까지 이동
  # 뒤 array가 남았을 경우는 값이 동일하므로 생략
  if (front_index != len(front_arr)) :
    sort_arr[tar_index:end_index+1] = front_arr[front_index:len(front_arr)]

  print(
    "sorted", sort_arr,
    "start_index", start_index,
    "mid_index", mid_index,
    "end_index", end_index,
  )
