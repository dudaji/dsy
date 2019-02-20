import random

def type_a(arr, s, e):
    # Base case
    if s >= e:
        return

    # Random pivot for escape worst case
    random_idx = random.randrange(s, e+1)
    arr[s], arr[random_idx] = arr[random_idx], arr[s]
    pivot = arr[s]

    # Sorting
    i = s + 1
    j = e
    while i <= j:
        while arr[i] < pivot and i < e:
            i += 1
        while arr[j] >= pivot and j > s:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[s], arr[j] = arr[j], arr[s] # Move pivot to middle
    type_a(arr, s, j-1)
    type_a(arr, j+1, e)


def type_b(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    left, mid, right = [], [], []
    pivot = arr[0]

    # Sorting
    for element in arr:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            mid.append(element)
    
    return type_b(left) + mid + type_b(right)


def type_c(arr, s, e):
    # Base case
    if s >= e:
        return
    
    # Sorting
    # less than pivot, place on the left side of the wall
    # position => | less elements | wall | greater elements | unsorted items | pivot |
    # wall is first element in greater elements
    # end of the iteration, swap pivot with wall
    # position after iteration => | less elements | pivot | greater elements | unsorted items | wall |
    pivot = arr[e]
    wall = s
    for i in range(s, e):
        if arr[i] < pivot:
            arr[i], arr[wall] = arr[wall], arr[i]
            wall += 1
    arr[wall], arr[e] = arr[e], arr[wall]
    type_c(arr, s, wall-1)
    type_c(arr, wall+1, e)
        