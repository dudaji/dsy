class HashTable:
  def __init__(self, capacity=10):
    self.table = [[] for _ in range(capacity)]
    self.capacity = capacity
    self.size = 0

  def __len__(self):
    return len(self.table)

  def __str__(self):
    ret = ""
    for idx, chain in enumerate(self.table):
      ret += "[{}]".format(idx)
      for e in chain:
        ret += "-> {}".format(str(e))
      ret += "\n"
    return ret
  
  def _hashing(self, key):
    h = 0
    for ch in key:
      h = h * 31 + ord(ch)
    return h

  def _expand(self):
    old_table = self.table[:]
    self.capacity += self.capacity // 2
    self.table = [[] for _ in range(self.capacity)]
    self.size = 0
    for line in old_table:
      while line:
        item = line.pop()
        self.push(item[0], item[1])

  def push(self, key, value):
    if self.size > self.capacity:
      self._expand()
    index = self._hashing(key) % self.capacity
    try:
      self.pop(key)
    except KeyError:
      # add new key-value
      self.size += 1
    finally:
      self.table[index].append((key, value))

  def pop(self, key):
    index = self._hashing(key) % self.capacity
    for i, e in enumerate(self.table[index]):
      if key == e[0]:
        ret =  e[1]
        del self.table[index][i]
        return ret
    raise(KeyError(key))

  def peek(self, key):
    index = self._hashing(key) % self.capacity
    for e in self.table[index]:
      if key == e[0]:
        return e[1]