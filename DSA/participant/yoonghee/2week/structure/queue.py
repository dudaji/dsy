# FIFO 구조 list로 구현함
# node로 구현 : https://wayhome25.github.io/cs/2017/04/18/cs-21/

class Queue(list):
    # enqueue == > insert 관용적인 이름
    enqueue = list.append
    # dequeue == > delete
    def dequeue(self):
        return self.pop(0)

    def is_empty(self):
        if not self:
            return True
        else:
            return False

    def peek(self):
        return self[0]

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    while not q.is_empty():
        print(q.peek(), end= ' ')
        print(q.dequeue()) # 1 2 3 4 5