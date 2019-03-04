def select_min_idx(arr, start, end):
    min_idx = start
    for i in range(start + 1, end):
        if arr[min_idx] > arr[i]:
            min_idx = i
    return min_idx


def sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = select_min_idx(arr, i, n)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

