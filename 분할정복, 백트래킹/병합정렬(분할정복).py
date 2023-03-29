# 인덱스로 접근
def merge_sort(start, end):     # 정렬할 애들 인덱스 받아 옴
    if start == end:    # 분할할 원소가 하나면
        return

    else:   # 위에서 리턴하기 때문에 생략 가능
        mid = (start+end)//2
        merge_sort(start, mid)  # 왼쪽 정렬
        merge_sort(mid+1, end)  # 오른쪽 정렬

        # merge()
        k = 0
        # 왼족과 오른쪽에서 가장 작은 숫자의 위치(첫번째 인덱스)
        left = start
        right = mid+1
        while left<=mid or right<=end:  # 실행조건(인덱스가 끝값을 넘지 않아야 함)

            # 둘 다 범위 안에 있다면, 해당 인덱스 값들끼리 크기 비교 후 정렬
            if left <= mid and right <= end:
                if arr[left] <= arr[right]:
                    tmp[k] = arr[left]
                    left += 1     # 다음 인덱스로 이동
                else:
                    tmp[k] = arr[right]
                    right += 1    # 다음 인덱스로 이동
                k += 1

            # 왼쪽과 오른쪽 리스트 길이가 달라서 어느 한 쪽이 남아 있다면
            elif left <= mid:
                while left <= mid:
                    tmp[k] = arr[left]
                    left += 1
                    k += 1
            elif right <= end:
                while right <= end:
                    tmp[k] = arr[right]
                    right +=1
                    k += 1

        i = 0
        while i < k:
            arr[start+i] = tmp[i]
            i += 1
        return


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    tmp = [0] * N        # 계산하면서 두 부분집합을 합쳐야하는데, 이떄 저장할 임시공간
    merge_sort(0,N-1)

