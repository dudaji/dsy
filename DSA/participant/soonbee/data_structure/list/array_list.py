class ArrayList:
  def __init__(self, capacity=10):
    self._array = [None] * capacity
    self.size = 0
  
  def __len__(self):
    return self.size

  def __str__(self):
    return str(self._array[:self.size])

  def push(self, index, value):
    if index < 0:
      raise IndexError("index out of range")
    if index > self.size:
      raise IndexError("index out of range")
    if self.size >= len(self._array):
      self._expand()
    for i in range(self.size, index, -1):
      self._array[i] = self._array[i-1]
    self._array[index] = value
    self.size += 1
  
  def _expand(self):
    self._array.extend([None] * len(self._array))
  
  def pop(self, index):
    if index < 0:
      raise IndexError("index out of range")
    if index >= self.size:
      raise IndexError("index out of range")
    ret = self._array[index]
    for i in range(index+1, self.size):
      self._array[i-1] = self._array[i]
    return ret
  
  def peek(self, index):
    if index < 0:
      raise IndexError("index out of range")
    if index >= self.size:
      raise IndexError("index out of range")
    return self._array[index]