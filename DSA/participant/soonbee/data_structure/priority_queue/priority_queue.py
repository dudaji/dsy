class Node:
  def __init__(self, value, priority):
    self.value = value
    self.priority = priority
  
  def __str__(self):
    return "({}, {})".format(self.value, self.priority)

  def __repr__(self):
    return "({}, {})".format(self.value, self.priority)
  
  def __gt__(self, other):
    return self.priority > other.priority
  
  def __lt__(self, other):
    return self.priority < other.priority


class PriorityQueue:
  def __init__(self):
    self.heap = []

  def __del__(self):
    del self.heap
  
  def __len__(self):
    return len(self.heap)

  def __str__(self):
    return str(self.heap)

  def _get_left_child(self, index):
    return self.heap[self._get_left_child_index(index)]

  def _get_right_child(self, index):
    return self.heap[self._get_right_child_index(index)]

  def _get_parent(self, index):
    return self.heap[self._get_parent_index(index)]

  def _get_left_child_index(self, index):
    return index * 2 + 1

  def _get_right_child_index(self, index):
    return index * 2 + 2

  def _get_parent_index(self, index):
    return (index - 1) // 2

  def _has_left_child(self, index):
    left_child_index = self._get_left_child_index(index)
    return left_child_index < len(self.heap)
  
  def _has_right_child(self, index):
    right_child_index = self._get_right_child_index(index)
    return right_child_index < len(self.heap)

  def _has_parent(self, index):
    parent_index = self._get_parent_index(index)
    return parent_index >= 0

  def _swap(self, a, b):
    self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

  def push(self, value):
    self.heap.append(value)
    index = len(self.heap) - 1
    parent = self._get_parent_index(index)
    while self._has_parent(index) and self.heap[index] < self.heap[parent]:
      self._swap(index, parent)
      index = parent
      parent = self._get_parent_index(index)
  
  def pop(self):
    if not self.heap:
      raise IndexError("pop from empty priority queue")
    ret = self.heap[0]
    self.heap[0] = self.heap[-1]
    self.heap.pop()
    index = 0
    while self._has_left_child(index):
      left = self._get_left_child_index(index)
      right = self._get_right_child_index(index)
      min_child_index = left
      if (self._has_right_child(index) and self.heap[left] > self.heap[right]):
          min_child_index = right
      if self.heap[index] > self.heap[min_child_index]:
        self._swap(index, min_child_index)
      index = min_child_index
    return ret

  def peek(self):
    if not self.heap:
      raise IndexError("peek from empty priority queue")
    return self.heap[0]
  
  def is_empty(self):
    return not self.heap