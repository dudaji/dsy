'''
selection sort는 비교연산을 많이하고 값 교환을 적게합니다.
가장 작은 수를 찾아 가장 앞에 두고
남은 수 중 가장 작은 수를 찾아 그 다음에 두는 방식으로 반복
time complexity : O(n^2) - worst, average, best경우 모두
'''
def sort(array):
    for i in range(len(array)):
        min_value = array[i]
        min_index = i
        for j in range(i+1,len(array)):
            if min_value > array[j]: # 가장작은 최소값을 남은 배열에서 탐색
                min_value = array[j]
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]   
    return array