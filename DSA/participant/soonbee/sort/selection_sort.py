def select_min_idx(array, start, end):
    min_idx = start
    for i in range(start + 1, end):
        if array[min_idx] > array[i]:
            min_idx = i
    return min_idx


def sort(arg):
    array = arg[:]
    n = len(array)
    for i in range(n):
        min_idx = select_min_idx(array, i, n)
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

