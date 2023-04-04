T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    INF = 1e8
    adj = [[INF]*(V+1) for _ in range(V+1)]   # 인접행렬

    for _ in range(E):
        start,to,w = map(int,input().split())
        adj[start][to] = w

    distance = [INF] * (V+1)
    distance[0] = 0             # 출발점 거리는 0

    for i in range(V+1):
        for j in range(V+1):
            # 거리가 INF보다 작은 값이라면
            if i != j and adj[i][j] != INF:
                # 현재까지의 거리 + j로 이동했을 때 거리 < 원래 j까지 거리
                if distance[i] + adj[i][j] < distance[j]:
                    distance[j] = distance[i] + adj[i][j] # 짧은 거리로 갱신

    # print(distance)
    ans = distance[-1]
    print(f'#{tc} {ans}')
