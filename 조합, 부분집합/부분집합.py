def f(i,k):         # bit[i]를 결정하는 함수
    if i ==k        # bit의 모든 원소 결정
        print(*bit)
    else:           # 갈림길(0,1)
        bit[i] = 0
        f(i+1,k)
        bit[i] = 1
        f(i+1,k)

A = [7,2,5,3,4]
N = len(A)
bit = [0] * N        # bit[i] A[i] 원소가 부분집합에 표시되는지 표시하는 배열

f(0,N)               # bit[0]번부터 접근