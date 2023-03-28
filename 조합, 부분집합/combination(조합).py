N = 10

# [1] N개의 원소 중 3개(i<j<k) 고르는 조합
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            print(i,j,k)


# [2] n개에서 r개 고르는 조합 (재귀)
def nCr(n,r,s):
    if r==0:
        print(*comb)
    else:
        for i in range(s,n-r+1):
            comb[r-1] = A[i]
            nCr(n,r-1,i+1)

n = 5
r = 3
comb = [0]*3
A = [i for i in range(1,n+1)]
nCr(n,r,0)