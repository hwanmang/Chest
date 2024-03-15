def dfs(start, score, calorie):
    global best
    if calorie > L:
        return
    if calorie <= L:
        if best < score:
            best = score
    for j in range(start, N):
        dfs(j+1, score + food[j][0], calorie+food[j][1])


T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())  # N:재료수 L:제한 칼로리
    food = [list(map(int, input().split())) for _ in range(N)]
    # start, 칼로리, 만족도
    best = 0
    dfs(0, 0, 0)
    print(f'#{test_case} {best}')
