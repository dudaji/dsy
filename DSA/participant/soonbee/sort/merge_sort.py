def sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])

    # Merge
    ret = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ret.append(left[i])
            i += 1
        else:
            ret.append(right[j])
            j += 1
    while i < len(left):
        ret.append(left[i])
        i += 1
    while j < len(right):
        ret.append(right[j])
        j += 1
    return ret
