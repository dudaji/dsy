# 과제

## 시간복잡도 

아래 문제에 대한 답을 작성하기

#### 1. 다음 Big-O 표기법에 대하여 대소비교를 하시오. 

```
O(n), O(1), O(2^n), o(logn), O(n^2), O(10^n), O(n!), O(nlogn), O(n^10)
```

#### 2. 다음 함수들에 대하여 시간복잡도를 Big-O 표기법으로 표현하시오.

**2-1)**

```python
def func(n):
    n = 10
    return n
```

**2-2)**

```python
def func(n):
    ret = 0
    for i in range(n):
        ret += 1
    return retn
```

**2-3)**

```python
def func(n):
    ret = 0
    for i in range(n):
        for j in range(n):
            ret += 1
    return ret
```

**2-4)**

```python
def func(n):
    ret = 0
    for i in range(n):
        for j in range(i):
            ret += 1
    return ret
```

**2-5)**

```python
def func(data, x):
    lo = 0
    hi = len(data)
    while lo < hi:
        mid = (lo + hi) // 2
        if data[mid] == x:
            return mid
        elif data[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return None
```

**2-6)**

```python
def func(n):
    ret = 0
    for i in range(n):
        for j in range(i, n, i + 1):
            ret += 1
    return ret
```

**2-7)**

```python
def func(n):
    if n <= 0:
        return 1
    return func(n - 1) + func(n - 1)
```

**2-8)**

```python
def func(n, a=1, b=2):
    if n <= 1:
        print('{0}: {1} -> {2}'.format(n, a, b))
        return
    c = 6 - a - b
    func(n - 1, a, c)
    print('{0}: {1} -> {2}'.format(n, a, b))
    func(n - 1, c, b)
```

## 정렬

#### 1. 유닛테스트를 통해 아래 테스트 케이스 검증

- 단순한 배열(배열의 길이 홀수)

  [10, 7, 17, 3, 4, 21, 6, 20, 1] => [1, 3, 4, 6, 7, 10, 17, 20, 21]

- 단순한 배열(배열의 길이 짝수)

  [10, 7, 17, 3, 4, 21, 6, 20, 1, 9] => [1, 3, 4, 6, 7, 9, 10, 17, 20, 21]

- 역정렬된 배열

  [7, 6, 5, 4, 3, 2, 1] => [1, 2, 3, 4, 5, 6, 7]

- 정렬된 배열

  [1, 2, 3, 4, 5, 6, 7] => [1, 2, 3, 4, 5, 6, 7]

- 같은 숫자들이 있는 배열

  [3, 3, 4, 3, 6, 5, 6, 4, 3, 4, 6, 3] => [3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 6, 6]

- 1개 혹은 2개만 있는 배열

  [1] => [1]

  [10, 2] => [2, 10]

  [2, 10] => [2, 10]

#### 2. 구현한 정렬코드를 이용하여 다음 아래 문제 통과하기

  버블: https://www.acmicpc.net/problem/1517 
  
  선택: https://www.acmicpc.net/problem/2750

  삽입: https://www.acmicpc.net/problem/1427

  합병: https://www.acmicpc.net/problem/2751

  퀵: https://www.acmicpc.net/problem/11931

## 자료구조

#### 1. 유닛테스트를 통해 아래 테스트 케이스 검증

해시테이블

- 비어있는 해시테이블에 대한 삭제 및 선택
- 3개의 원소 삽입 후 1개 선택
- 4개의 원소 삭제
- 일정 개수 이상의 삽입 (resizing 검증)

우선순위큐

- 비어있는 우선순위큐에 대한 삭제 및 선택
- 3개의 원소 삽입 후 1개 선택
- 4개의 원소 삭제
- 우선순위가 같은 원소를 삽입했을때의 처리 검증
