'''
2중 for문으로 두원소를 비교해 가며 swap하여 정렬하는 알고리즘으로
이미 큰값으로 정렬이 끝난 index에 대해서는 연산을 하지 않습니다.
단순 2중 for문 이므로 time complexity : O(n^2)
'''
def sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j+1] < array[j]:
                array[j], array[j+1] = array[j+1], array[j]
    return array