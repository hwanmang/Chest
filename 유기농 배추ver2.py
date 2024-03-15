from collections import deque

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

t = int(input())


def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 그래프 범위 확인
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))


for i in range(t):
    cnt = 0
    n, m, k = map(int, input().split())  # 가로, 세로, 노드
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())  # 입력받은 값으로 노드에 1표시
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)
