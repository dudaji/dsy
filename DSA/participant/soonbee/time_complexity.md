## 시간복잡도 

아래 문제에 대한 답을 작성하기

#### 1. 다음 Big-O 표기법에 대하여 대소비교를 하시오. 

```
O(n), O(1), O(2^n), O(logn), O(n^2), O(10^n), O(n!), O(nlogn), O(n^10)
```

$O(1) < (logn) < O(n)< O(nlogn)< O(n^2) < O(n^10) < O(2^n) < O(10^n) < O(n!)$

#### 2. 다음 함수들에 대하여 시간복잡도를 Big-O 표기법으로 표현하시오.

**2-1)**

```python
def func(n):
    n = 10
    return n
```

정답: $O(1)$

**2-2)**

```python
def func(n):
    ret = 0
    for i in range(n):
        ret += 1
    return retn
```

정답: $O(n)$

**2-3)**

```python
def func(n):
    ret = 0
    for i in range(n):
        for j in range(n):
            ret += 1
    return ret
```

정답: $O(n^2)$

**2-4)**

```python
def func(n):
    ret = 0
    for i in range(n):
        for j in range(i):
            ret += 1
    return ret
```

정답: $O(n^2)$

**2-5)**

```python
# data의 길이를 n이라고 가정
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

정답: $O(logn)$

**2-6)**

```python
def func(n):
    if n <= 0:
        return 1
    return func(n - 1) + func(n - 1)
```

정답: $O(n^2)$

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

정답: $O(n^2)$

<br>

