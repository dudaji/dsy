import sys
sys.setrecursionlimit(1500)

n = int(input())
array = []

for _ in range(0, n):
  array.append(int(input()))


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




# array.sort()
# result = sort_bubble_start(array)
# result = sort_select(array)
result = sort_insert(array)

for i in result:
    print(i)
