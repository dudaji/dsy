class HashTable:
  EMPTY = "EMPTY"
  DELETED = "DELETED"

  def __init__(self):
    self.table = [self.EMPTY for _ in range(11)]
    self.size = 0
    self.capacity = 11
    self.k = 7
  
  def __len__(self):
    return self.size
  
  def __str__(self):
    return str(self.table)
  
  def push(self, key, value):
    if self.size > self.capacity * 0.7:
      self._expand()
    index = self._hashing(key) % self.capacity
    step = self._hashing2(self._hashing(key))
    try:
      self.pop(key)
    except KeyError:
      self.size += 1
    finally:
      while True:
        if self.table[index] in [self.EMPTY, self.DELETED]:
          self.table[index] = (key, value)
          break
        index = (index + step) % self.capacity
  
  def pop(self, key):
    index = self._hashing(key) % self.capacity
    start = index
    step = self._hashing2(self._hashing(key))
    while True:
      if self.table[index][0] == key:
        ret = self.table[index][1]
        self.table[index] = self.DELETED
        return ret
      index = (index + step) % self.capacity
      if index == start:
        raise KeyError(key)

  def peek(self, key):
    index = self._hashing(key) % self.capacity
    start = index
    step = self._hashing2(self._hashing(key))
    while True:
      if self.table[index][0] == key:
        return self.table[index][1]
      index = (index + step) % self.capacity
      if index == start:
        raise KeyError(key)
  
  def _hashing(self, key):
    h = 0
    for ch in key:
      h = h * 31 + ord(ch)
    return h
  
  def _hashing2(self, key):
    return self.k - (key % self.k)

  def _expand(self):
    old_table = self.table[:]
    self.k = self.capacity
    self.capacity += self.capacity // 2
    self.capacity = self._find_next_prime_number(self.capacity) 
    self.table = [self.EMPTY for _ in range(self.capacity)]
    self.size = 0
    for e in old_table:
      if e in [self.EMPTY, self.DELETED]:
        continue
      self.push(e[0], e[1])

  def _is_prime(self, n):
    return all([(n%j) for j in range(2, int(n**0.5 + 1))]) and n > 1

  def _find_next_prime_number(self, n):
    n += 1
    while not self._is_prime(n):
      n += 1
    return n