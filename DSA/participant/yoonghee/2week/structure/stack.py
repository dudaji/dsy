# LIFO 구조 list로 구현함
# node로 구현 : https://wayhome25.github.io/cs/2017/04/18/cs-20/
# 추상구조, 배열, linked list 구현 : https://github.com/keon/algorithms/blob/master/algorithms/stack/stack.py

class Stack(list):
    push = list.append    # Insert
                          # Delete - 내장 pop 메소드 활용
    def is_empty(self):   # 데이터가 없는지 확인
        if not self:
            return True
        else:
            return False

    def peek(self):        # 최상단 데이터 확인
        return self[-1]

if __name__=="__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    while s:
        data = s.pop()
        print(data, end=' ') # 3 2 1