def sort(arg):
    array = arg[:]
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array