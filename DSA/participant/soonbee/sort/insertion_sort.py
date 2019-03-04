def sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        j = i - 1
        while j > -1 and arr[j] > cursor:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cursor