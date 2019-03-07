import heapq as pq


heap = []
pq.heappush(heap, 2)
pq.heappush(heap, 4)
pq.heappush(heap, 1)
pq.heappush(heap, 7)
pq.heappush(heap, 3)
print(heap)
print(pq.heappop(heap)) # O (log N)
print(heap)
print(pq.heappop(heap))
print(heap[0])
print(heap) # 삭제하지 않고 얻기

heap = [4, 1, 7, 3, 8, 5]
pq.heapify(heap) # O (N)
print(heap)

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  pq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(pq.heappop(heap)[1])  # index 1


def kth_smallest(nums, k):
  heap = []
  for num in nums:
    pq.heappush(heap, num)

  kth_min = None
  for _ in range(k):
    kth_min = pq.heappop(heap)
  return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3))

def heap_sort(nums):
  heap = []
  for num in nums:
    pq.heappush(heap, num)
  
  sorted_nums = []
  while heap:
    sorted_nums.append(pq.heappop(heap))
  return sorted_nums



print(heap_sort([4, 1, 7, 3, 8, 5]))