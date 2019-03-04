class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.before = None


class List:
    def __init__(self):
        self.head = Node('[head]')
        self.tail = self.head
        self.cur = self.head
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        ret = '['
        cur = self.head.next
        while cur:
            ret += '%s-> ' % cur.data
            cur = cur.next
        ret += ']'
        return ret

    def push_back(self, data):
        new = Node(data)
        self.tail.next = new
        new.before = self.tail
        self.tail = new
        self.length += 1


    def pop(self):
        if self.cur is self.head:
            return None
        ret = self.cur.data
        self.cur.before.next = self.cur.next
        self.cur.next.before = self.cur.before
        deleted = self.cur
        self.cur = self.cur.before
        del deleted
        self.length -= 1
        return ret
    
    def peek(self):
        return self.cur.data

    def move_left(self):
        if self.cur is not self.head:
            self.cur = self.cur.before

    def move_right(self):
        if self.cur.next is not self.tail:
            self.cur = self.cur.next
