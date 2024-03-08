def power_recursive(N, M):
    # 지수가 0 이면 1
    if M == 0:
        return 1
    # 거듭제곱 계산
    return N * power_recursive(N, M - 1)


for i in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())
    result = power_recursive(N, M)
    print(f'#{i} {result}')
