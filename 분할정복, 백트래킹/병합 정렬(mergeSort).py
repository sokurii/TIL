A = [69, 10, 30, 2, 16, 8, 31, 22]

# m : 정렬하고 싶은 리스트(배열)
def mergeSort(lst):
    # [종료조건]
    # 더이상 쪼갤 수 없을 때까지 분할 (리스트 길이 : 1)
    if len(lst) == 1:
        return lst

    # [분할]
    left = right = []
    # 분할 기준 : 정확히 반으로
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # [정복]
    left = mergeSort(left)
    right = mergeSort(right)

    # [병합]
    return merge(left,right)


# 병합 함수
def merge(left,right):
    # li : 왼쪽에서 다음에 꺼내올 원소 위치
    # ri : 오른쪽에서 다음에 꺼내올 원소 위치
    li = ri = 0

    result = []
    # left[li], right[ri] 비교해서 작은 것부터 result에 담기
    # 오른쪽에 없다면, 왼쪽에 남은 거 다 result
    # 왼쪽에 없다면, 오른쪽에 남은 거 다 result
    while li < len(left) or ri < len(right):
        # 둘 다 남아 있는 경우, 작은 것부터 담는다
        if li < len(left) and ri < len(right):
            if left[li] <= right[ri]:
                result.append(left[li])
                li += 1
            else:
                result.append(right[ri])
                ri += 1

        # 둘 중 하나만 남아 있는 경우
        elif li < len(left):
            result.append(left[li])
            li += 1
        elif ri < len(right):
            result.append(right[ri])
            ri += 1

    return result



print(mergeSort(A))