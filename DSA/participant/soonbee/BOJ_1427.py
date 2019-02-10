array = list(input())
n = len(array)
for i in range(n):
    tmp = array[i]
    j = i - 1
    while j > -1 and array[j] < tmp:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = tmp
print(''.join(array))