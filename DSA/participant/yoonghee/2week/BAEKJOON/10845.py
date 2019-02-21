# -*- coding:utf-8 -*-
import collections
import sys
from sys import stdin,stdout
sys.setrecursionlimit(1500)
 
d = collections.deque()
data = int(stdin.readline(15)) # 명령의 갯수

for _ in range(data):
    cmd = stdin.readline(25)
    if "push" in cmd:
        val = int(cmd.strip().split(" ")[1])
        d.append(val) # 오른쪽에 추가, 왼쪽에 추가하려면 appendleft()

    elif "pop" in cmd:
        if not d:
            stdout.write(str(-1)+"\n")
        else:
            stdout.write(str(d.popleft())+"\n") # 오른쪽 끝값을 가져오면서 제거, 왼쪽은 popleft()

    elif "size" in cmd:
        stdout.write(str(len(d))+"\n")

    elif "empty" in cmd:
        if not d:
            stdout.write(str(1)+"\n")
        else:
            stdout.write(str(0)+"\n")

    elif "front" in cmd:
        if not d:
            stdout.write(str(-1)+"\n")
        else:
            stdout.write(str(d[0])+"\n") # 가장 왼쪽값, -1 가장 오른쪽값

    elif "back" in cmd:
        if not d:
            stdout.write(str(-1)+"\n")
        else:
            stdout.write(str(d[-1])+"\n")

