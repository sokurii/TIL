lst = [5,7,9,0,3,1,6,2,4,8]

# 퀵정렬 함수 정의하기 :  quickSort(리스트, 시작 인덱스(0), 끝 인덱스(len(lst)-1))
def quickSort(lst, start, end):
    if start >= end:
        return
    # 비교할 인덱스 지정
    pivot = start
    left = start + 1
    right = end

    # 엇갈릴 때까지 반복
    while left <= right:
        # [선형탐색]
        # 피벗보다 큰 데이터를 찾을 때까지 반복(왼->오)
        while left <= end and lst[left] <= lst[pivot]:
            left += 1
        # 피벗보다 작은 데이터 찾을 떄까지 반복(오->왼)
        while right > start and lst[right] >= lst[pivot]:
            right -= 1

        if left > right:    # 엇갈렸다면 작은 데이터와 피벗을 교체
            lst[right], lst[pivot] = lst[pivot], lst[right]
        else:               # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            lst[left], lst[right] = lst[right], lst[left]

    # [정렬 수행]
    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬 수행
    quickSort(lst, start, right-1)
    quickSort(lst, right+1, end)

quickSort(lst,0,len(lst)-1)
print(lst)