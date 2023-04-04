n, m = map(int,input().split())
s = int(input())    # 시작 노드
INF = 1e8

adj = [[] for _ in range(n+1)]    # 1번 노드부터 시작하므로 하나 더 추가

visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    start,to,w = map(int,input().split()) # start출발, to도착, w가중치
    adj[start].append((to,w))     # 거리정보, 도착노드 함께 입력

# 미방문 & 시작노드와 최단거리인 노드 반환
def get_min_node():
    min_val = INF
    index = 0
    for i in range(1,n+1):  # 1번 노드부터 시작하죠 ?
        if not visited[i] and distance[i] < min_val:
            min_val = distance[i]
            index = i
    return index

# 다익스트라 알고리즘
def dijkstra(S):
    # [1] 시작노드
    # 시작노드 거리 =0, 시작노드 방문처리
    distance[S] = 0
    visited[S] = True
    # 시작노드의 인접 노드들에 대해 최단거리 계산
    for i in adj[S]:
        distance[i[0]] = i[1] # i[0] 도착노드 정보, i[1] 가중치

    # [2] 시작노드 외 다른 노드들
    # 시작노드 제외한 N-1개의 다른 노드들 처리
    for _ in range(n-1):
        now = get_min_node()    # 미방문 & 가장 짧은 거리의 노드 선택
        visited[now] = True     # 해당 노드 방문 처리
        # 해당 노드의 인접한 노드들 간 거리 계산
        for next in adj[now]:
            cost = distance[now] + next[1]  # (시작->now 거리) + (now->now인접노드 거리)
            # 거리 값 갱신
            if cost < distance[next[0]]:    # cost < 시작->now인접노드 다이렉트 거리
                distance[next[0]] = cost    # 더 작은 값으로 갱신!

dijkstra(s)

for i in range(1,n+1):
    if distance[i] == INF:
        print('도달할 수 없음')
    else:
        print(distance[i])





