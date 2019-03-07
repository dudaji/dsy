import sys
from sys import stdin,stdout
sys.setrecursionlimit(1500)

class Stack(list):
    push = list.append   
                         
    def is_empty(self):  
        if not self:
            return True
        else:
            return False

    def peek(self):       
        return self[-1]

    def show(self):
        data = str()
        while self:
            data += self.pop()
        stdout.write(data + "\n")


d = Stack()

data = int(stdin.readline(15))

for _ in range(data):
    cmd = stdin.readline(25)
    if "push" in cmd:
        val = int(cmd.strip().split(" ")[1])
        d.push(val) # 오른쪽에 추가, 왼쪽에 추가하려면 appendleft()

    elif "pop" in cmd:
        if not d:
            stdout.write(str(-1)+"\n")
        else:
            stdout.write(str(d.pop())+"\n") # 오른쪽 끝값을 가져오면서 제거, 왼쪽은 popleft()

    elif "size" in cmd:
        stdout.write(str(len(d))+"\n")

    elif "empty" in cmd:
        if d.is_empty():
            stdout.write(str(1)+"\n")
        else:
            stdout.write(str(0)+"\n")
 
    elif "top" in cmd:
        if not d:
            stdout.write(str(-1)+"\n")
        else:
            stdout.write(str(d.peek())+"\n") # 가장 왼쪽값, -1 가장 오른쪽값


