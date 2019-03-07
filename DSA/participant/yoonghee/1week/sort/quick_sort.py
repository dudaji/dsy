'''
quick_sort는 pivot값을 얼마나 잘 고르냐에 따라 성능이 좌우됩니다. (partition)
pivot값보다 작은값과 큰값으로 왼쪽 오른쪽 배열 계속 나눔 (나눌때마다 pivot다시잡음)
partition이 왼쪽 오른쪽 하나씩 남을때 비교 정렬하면서 반환
최악의 경우 pivot이 partition을 너무 많이 나누면 n^2의 복잡도를 가지고
보통 nlogn의 복잡도를 가지는데 그 이유는 BST처럼 나누어 검색 결과가 줄어들기 때문 입니다.
time complexity : O(nlogn)

성능개선

pivot 랜덤값 or 중위값 -> 최악의 경우를 회피
insertion -> 성능개선
'''
import sys
from sys import stdin
sys.setrecursionlimit(1500)

def quick_sort(arr):
    left, right, pivot = [], [], []
    if len(arr) <= 1:
        return arr

    for x in arr:
        if x < arr[len(arr)//2]:
            left.append(x)
        elif x > arr[len(arr)//2]:
            right.append(x)
        else:
            pivot.append(x)
        
    return quick_sort(left) + pivot + quick_sort(right)
    

def sort(arr):
    return quick_sort(arr)

arr = []
N = int(stdin.readline())
for x in range(N):
    arr.append(int(stdin.readline()))

for y in sort(arr):
    print(y)