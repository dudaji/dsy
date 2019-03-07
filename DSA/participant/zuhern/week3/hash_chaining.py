
class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value


class HashTable():

  def __init__(self, size=7):
    self._table = [[] for _ in range(size)]
    self.size = size

  def set(self, key, value):
    
    new_node = Node(key, value)

    box, item, in_index = self.find(key)
    
    if item == None:
      box.append(new_node)
    else:
      item = new_node
    


  def get(self, key):

    _, item, in_index = self.find(key)
    if item == None:
      return None

    return item.value


  def delete(self, key):

    box, item, in_index = self.find(key)
    if item is None:
      return False
    
    del_item = box.pop(in_index)
    return del_item.value


  def find(self, key):
    
    hash_key = hash(key)
    index = hash_key % self.size

    box = self._table[index]
    
    cnt = len(box)
    for in_index in range(0, cnt):
      item = box[in_index]
      if item.key == key:
        return box, item, in_index 

    return box, None, -1




hash_table = HashTable()

def hash_set(key, value):
  return hash_table.set(key, value)
    

def hash_get(key):
  return hash_table.get(key)


def hash_delete(key):
  return hash_table.delete(key)
