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

if __name__=="__main__":
    s = Stack()

    data = list()
    while True:
        data = stdin.readline(80).strip()
        if data == "***":
            exit()

        [s.push(x) for x in list(data)]
        s.show() 

