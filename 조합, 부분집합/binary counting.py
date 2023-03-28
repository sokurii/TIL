'''부분집합'''

arr=[3,6,7,1,5,4]
n = len(arr)


for i in range(0,(1<<n)):               # 1<<n : 부분집합 개수
    for i in range(0,n):                # 원소 수만큼 비트를 비교함
        if i & (1<<j):                  # i의 j번째 비트가 1이면 j번째 원소 출력
            print('%d'%arr[j],end='')
    print()

'''재귀호출을 이용한 조합'''
# arr[] " n개원소를 가진 배열
# tr[] r개의 크기 배열, 조합이 임시 저장된 배열

comb(n,r)




