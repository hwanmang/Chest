n, m = map(int, input().split())
space = []

for _ in range(n):
    space.append(list(input()))

answer = []

for i in range(n-7):
    for j in range(m-7):
        black = 0
        white = 0

        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if space[k][l] != 'B':
                        black += 1
                    if space[k][l] != 'W':
                        white += 1
                else:
                    if space[k][l] != 'W':
                        black += 1
                    if space[k][l] != 'B':
                        white += 1
        answer.append(black)
        answer.append(white)
print(min(answer))
