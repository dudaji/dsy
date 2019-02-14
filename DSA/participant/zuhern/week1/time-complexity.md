# 과제


<br>

## 시간복잡도 

아래 문제에 대한 답을 작성하기

#### 1. 다음 Big-O 표기법에 대하여 대소비교를 하시오. 

```
O(n), O(1), O(2^n), O(logn), O(n^2), O(10^n), O(n!), O(nlogn), O(n^10)
```

#### 2. 다음 함수들에 대하여 시간복잡도를 Big-O 표기법으로 표현하시오.

**2-1)** 
> 답: O(1)
> n 의 값과 상관없이 연산 횟수는 같음

```python
def func(n):
    n = 10
    return n
```

**2-2)**
> 답: O(n)
> n 의 값 만큼 for 문 호출
```python
def func(n):
    ret = 0
    for i in range(n):
        ret += 1
    return retn
```

**2-3)**
> 답: O(n^2)
> n 의 값 만큼 for 문 호출 * n 의 값 만큼 for 문 호출
```python
def func(n):
    ret = 0
    for i in range(n):
        for j in range(n):
            ret += 1
    return ret
```

**2-4)**
> 답: O(n*i)
> n 의 값 만큼 for 문 호출 * i 의 값 만큼 for 문 호출
```python
def func(n):
    ret = 0
    for i in range(n):
        for j in range(i):
            ret += 1
    return ret
```

**2-5)**
> 답: O(log n)
> 최대 연산 횟수 x 일 때,
> (((n/2)-1)/2)-1 .... x번 < 1 (최종적으로 1개가 남음)
> 대략
> n / 2 / 2 ... -> n / 2^x <= 1
> 2^x = n -> x = log2 n
> 인듯
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
> 답: O(2^n)
> 2개씩 갈라지며 n번 연산
> 2 * (2 * 2 ... n번)
> 1 + 2^n 번 
> 1 이면 3번
> 2 이면 7번
> 3 이면 15번
> 2^(n+1) -1
```python
def func(n):
    if n <= 0:
        return 1
    return func(n - 1) + func(n - 1)
```

**2-7)**
> 답: O(2^n)
> n 에 의해 횟수가 결정되니 나머지 a,b는 무시한다.
> n 이 0이 될 때까지 가지치기 하니
> 2 * (2 * 2 ... n번)
> 1 + 2^n 번 
> 1 이면 1번
> 2 이면 3번
> 3 이면 7번
> 2^n -1
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
