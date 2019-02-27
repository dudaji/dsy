'''
merge_sort는 길이 n이 1이 될 때까지 2로 나누어주는 BST와 마찬가지로 divide하여
merge하므로 BST와 같은원리로 (logn)만큼 divide 해주고 
merge하면서 값을 비교하여 정렬 하므로 최대 n번 정도의 복잡도로 동작하므로 
안좋아도 nlogn의 성능을 갖게 됩니다.

quick_sort pivot값 잘 골랐을 때와 같은 성능을 나타내고
임시로 저장할 공간을 못쓸 때는 quick_sort를 사용합니다.
time complexity : O(nlogn)

백준에서 compile했을 때 에러남
'''
import sys
from sys import stdin
sys.setrecursionlimit(1500)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = len(arr)//2
    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])
    return merge(left, right)


def merge(left, right):
    l_idx, r_idx, temp = 0, 0, []

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            temp.append(left[l_idx])
            l_idx += 1

        else:
            temp.append(right[r_idx])
            r_idx += 1

    temp += left[l_idx:]
    temp += right[r_idx:]

    return temp


def sort(arr):
    return merge_sort(arr)

'''
arr = []
N = int(stdin.readline())
for x in range(N):
    arr.append(int(stdin.readline()))

for y in sort(arr):
    print(y)
'''