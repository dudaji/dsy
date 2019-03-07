import sys
from sys import stdin
sys.setrecursionlimit(1500)

n = stdin.readline()
N, M = int(n.split(" ")[0]), int(n.split(" ")[1])

arr = list()
[arr.append(x+1) for x in range(N)]

print("<", end="")
while len(arr):
    [arr.append(arr.pop(0)) for _ in range(M-1)]
    if len(arr)-1: 
        print(arr.pop(0), end=", ")
    else:
        print(arr.pop(0), end=">")
