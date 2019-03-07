'''
priority queue
1. 일반적인 큐는 FIFO 자료구조 이기 때문에 먼저 들어온 데이터를 먼저 내보냈다면, 우선순위 큐는
우선순위가 높은 데이터를 먼저 내보내는 자료구조
2. 새로운 노드를 삽입하면 우선순위에 맞게 위치에 삽입(Enqueue)
3. 제거를 할 때는 가장 우선 순위가 높은 맨 앞에 노드를 배면서 삭제(Dequeue)
'''

import heap
from heap import Heap

class PriorityQueue(Heap):
    enqueue = Heap.insert
    dequeue = Heap.delete

if __name__ == "__main__":
    pq = PriorityQueue("min")
    pq.enqueue(3)
    pq.enqueue(7)
    pq.enqueue(2)
    pq.enqueue(1)
    pq.enqueue(9)
    pq.enqueue(5)
    pq.enqueue(8)
    pq.enqueue(10)
    pq.enqueue(5)
    pq.enqueue(6)
    pq.enqueue(4)

    for i in range(1, pq.size()+1):
        print(pq.dynamic_arr[i], end = '  ')
        # 1  2  3  5  4  5  8  10  7  9  6  

    print("\n")

    for i in range(1, pq.size()+1):
        print(pq.dequeue(), end = '  ')
        # 1  2  3  4  5  5  6  7  8  9  10  