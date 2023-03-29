'''
분할정복 기반 알고리즘
'''

# n 제곱

def recursive_power(x,n):
    # 1 제곱은 그 수를 그대로 반환
    if n == 1 :
        return x

    # 짝수라면
    if n % 2 == 0:
        y = recursive_power(x, n//2)
        return y*y

    # 홀수라면 -1 후 나머지 짝수에 대한 제곱
    else:
        y = recursive_power(x, (n-1)//2)
        return y*y*x

