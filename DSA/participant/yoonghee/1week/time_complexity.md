## 시간복잡도 

아래 문제에 대한 답을 작성하기

#### 1. 다음 Big-O 표기법에 대하여 대소비교를 하시오. 

```
O(n), O(1), O(2^n), O(logn), O(n^2), O(10^n), O(n!), O(nlogn), O(n^10)
```

O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^10) < O(2^n) < O(10^n) < O(n!)

#### 2. 다음 함수들에 대하여 시간복잡도를 Big-O 표기법으로 표현하시오.

**2-1)**

```python
def func(n):
    n = 10
    return n
```

연산횟수 : 1
Time complexity : O(1)

**2-2)**

```python
def func(n):
    ret = 0
    for i in range(n):
        ret += 1
    return retn
```

연산횟수 : n + 1 
Time complexity : O(n)

**2-3)**

```python
def func(n):
    ret = 0
    for i in range(n):
        for j in range(n):
            ret += 1
    return ret
```

연산횟수 : n^2 + 1
Time complexity : O(n^2)

**2-4)**

```python
def func(n):
    ret = 0
    for i in range(n):
        for j in range(i):
            ret += 1
    return ret
```

연산횟수 : 1 + 1*0 + 1*1 + 1*2 ~ + 1*9 - 100 ~ 50, 10000 ~ 5050 , 1000000 500500, n^2/2
Time complexity : O(n^2)

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

연산횟수 : 2 + divide한만큼 연산횟수가 줄어듬
Time complexity : O(logn)

**2-6)**

```python
def func(n):
    if n <= 0:
        return 1
    return func(n - 1) + func(n - 1)
```

연산횟수 : 함수 2개를 계속 n번 호출, 2의 지수승으로 분기
Time complexity : O(2^n)

**2-7)**

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

n = 10 일때 
연산횟수 = 2^0 + 2^1 ~ + 2^9 이고, 2^0 + ~ 2^(n-1) = 2^n - 1 
Time complexity : O(2^n)

<br>
