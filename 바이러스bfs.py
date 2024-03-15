from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        now = queue.popleft()
        count += 1

        for i in graph[now]:  # 그래프의 노드를 순서대로 검사
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return count - 1  # 시작 노드는 세지 않음


visited = [False] * (n+1)
result = bfs(1)
print(result)
