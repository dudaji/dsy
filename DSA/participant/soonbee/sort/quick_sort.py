import random

def sort(arr):
  quick(arr, 0, len(arr)-1)


def quick(arr, s, e):
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
    quick(arr, s, j-1)
    quick(arr, j+1, e)
