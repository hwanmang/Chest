T = int(input())

for test_case in range(1, T + 1):
    X, Y, K = map(int, input().split())

    min_val = min(X, Y)
    diff = abs(X - Y)
    if X > Y:
        X -= diff
    else:
        Y -= diff

    A = X + K * (diff // 2)
    B = Y + K * (diff // 2)

    answer = min(A, B)
    print(f'#{test_case} {answer}')
