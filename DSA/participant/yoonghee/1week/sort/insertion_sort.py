'''
insertion sort는 비교연산을 적게하고 값 교환을 많이합니다.
입력 데이터 만큼 for문과 값을 옮기는 만큼 while문을 돌며 연산 하므로
정렬이 되어 있을수록 좋은 성능을 나타냅니다.
time complexity : O(n^2)
'''
def sort(array):
    for i in range(len(array)-1):
        temp = array[i+1] # 속도향상을 위한 배열값 저장
        j = i
        while array[j] > temp and j >= 0:
            array[j+1] = array[j] # 앞에 큰값을 뒤로 이동 - 한번이상
            j -= 1
        array[j+1] = temp # 뒤에 작은값을 앞으로 이동 - 한번
    return array