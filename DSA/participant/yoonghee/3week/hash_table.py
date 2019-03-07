
class HashTable(object):

	MINIMUM_BUCKETS = 4 # 최소 버킷 갯수
	BUCKET_SIZE = 5 # 버킷당 값의 최대 갯수

	def __init__(self, capacity=MINIMUM_BUCKETS*BUCKET_SIZE): 
		self.size = 0
		self.threshold = capacity # 4*5
		self.buckets = [[] for _ in range(capacity//self.BUCKET_SIZE)]  # 이중 list, 버킷 수만큼 빈 버킷생성

	def push(self, key, value): # key, value값 
		bucket = self.hash(key)
		#print("push 버킷: ",bucket) # hash code % 버킷수 나머지값 : 버킷 인덱스 번호
		for n, element in enumerate(self.buckets[bucket]): # 버킷 탐색
			if element['key'] == key: # 이미 동일한 key값이 있는지 확인
				element['value'] = value # 해당 key의 value값 갱신
				self.buckets[bucket][n] = element # 확인한 key, value를 해당 버킷의 인덱스에 저장
				return
		else:
			self.buckets[bucket].append({'key': key, 'value': value}) #동일한 key값이 없을 경우 key와 value값 버킷에 추가
			self.size += 1 # 현제 크기 업데이트 
			if self.size == self.threshold: # 크기가 threshold와 같아질 경우 resize
				self.resize()

	def get(self, key):
		bucket = self.hash(key)
		for element in self.buckets[bucket]: # get할 key값을 찾아 value를 반환
			if element['key'] == key:
				return element['value']
		raise KeyError("No such key '{0}'!".format(key))

	def pop(self, key):
		bucket = self.hash(key)
		for n, element in enumerate(self.buckets[bucket]): # pop할 key값을 찾아 del 후 size -1
			if element['key'] == key:
				del self.buckets[bucket][n]
				self.size -= 1
				return
		raise KeyError("No such key '{0}'!".format(key)) # 찾는 key값이 없을 경우 raise

	def hash(self, key):
		return hash(key) % len(self.buckets) # hash code를 버킷수로 나눈 나머지값 반환

	def contains(self, key):
		bucket = self.hash(key)
		for element in self.buckets[bucket]: # 해당 key값이 있는지 boolean으로 반환
			if element['key'] == key:
				return True
		return False

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, value):
		return self.push(key, value)

	def __delitem__(self, key):
		return self.pop(key)

	def __len__(self):
		return self.size

	def is_empty(self): 
		return self.size == 0

	def resize(self): # capacity 20, size = 20이 되었을 경우, 버킷사이즈 5, 미니멈 버킷 4
		capacity = self.size / self.BUCKET_SIZE * 2 # 20/5*2 = 8
		if capacity >= self.MINIMUM_BUCKETS: # 8 >= 4
			old = self.buckets # 이전 버킷 2중 list 값 저장
			self.buckets = [[] for _ in range(capacity)] # resize한 크기 4->8로 버킷 재생성
			for n in range(len(self.buckets)): # 새로 만든 버킷에 이전값 대입
				self.buckets[n] = old[n]
			self.rehash() # 대입 후 rehash

	def rehash(self): # 다시 rehash 해주는 이유??
		for n, bucket in enumerate(self.buckets):
			for m, element in enumerate(bucket):
				new_bucket = self.hash(element['key'])  # hash code 재생성 후 나머지 값
				self.buckets[new_bucket].append(element) # 다시 버킷에 저장
				del self.buckets[n][m] # 기존값 제거

def main():
	table = HashTable() # hash table 객체 생성

	table.__setitem__("one", 1)
	table.push("two", 2)
	table.push("three", 3)
	table.push("four", 4)
	table["four"] = 4
	table["five"] = 5
	table.push("six", 6)
	table.push("seven", 7)
	table.push("eight", 8)
	
	print(len(table))

	print(table.is_empty())
	print(table.__getitem__("two"))

	table["one"] = 123

	print(table["one"])
	print(table["two"])

	table.pop("three")
	print(table["two"])
	table.pop("four")
	table.pop("five")
	
	print(len(table))
	print(table["two"])
	
	table.__delitem__("one")
	table.__delitem__("two")
	table.__delitem__("six")
	
	print(table.is_empty())
	
	print(table["seven"])

	table.pop("seven")
	table.pop("eight")

	print(len(table))
	print(table.is_empty())


if __name__ == '__main__':
	main()