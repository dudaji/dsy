from abc import ABCMeta, abstractmethod

class AbstractStack(metaclass=ABCMeta):
    @abstractmethod
    def push(self, value):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass


class SimpleStack:
    def __init__(self):
        self._list = []
    
    def __str__(self):
        result = " ".join(map(str, self._list[::-1]))
        return "Top -> " + result

    def push(self, value):
        self._list.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._list.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._list[-1]
    
    def is_empty(self):
        return not self._list


class ArrayStack(AbstractStack):
    def __init__(self, size=10):
        super().__init__()
        self._top = -1
        self._array = [None] * size

    def __len__(self):
        return self._top + 1

    def is_empty(self):
        return self._top == -1
    
    def push(self, value):
        self._top += 1
        if self._top == len(self._array):
            self._expand()
        self._array[self._top] = value
    
    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        value = self._array[self._top]
        self._top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self._array[self._top]

    def _expand(self):
        self._array.extend([None] * len(self._array))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack(AbstractStack):
    def __init__(self):
        super().__init__()
        self.top = None
        self.size = 0

    def __del__(self):
        while self.top:
            self.pop()
    
    def is_empty(self):
        return not self.top

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        deleted = self.top
        value = self.top.value
        self.top = self.top.next
        del deleted
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.top.value

