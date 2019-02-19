from abc import ABCMeta, abstractclassmethod

class SimpleQueue:
    def __init__(self):
        self._list = []
    
    def dequeue(self, value):
        self._list.append(value)
    
    def enqueue(self):
        return self._list.pop(0)

    def peek(self):
        return self._list[0]
    
    def is_empty(self):
        return not self._list


class AbstractQueue(metaclass=ABCMeta):
    @classmethod
    def enqueue(self, value):
        pass

    @classmethod
    def dequeue(self):
        pass
    
    @classmethod
    def peek(self):
        pass


class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue(AbstractQueue):
    def __init__(self):
        super().__init__()
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        node = QueueNode(value)
        self.size += 1
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        ret = self.front
        self.front = self.front.next
        self.size -= 1
        return ret

    def peek(self):
        return self.front