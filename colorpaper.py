a = int(input())

check = [[0]*100 for _ in range(100)]
cnt = 0

for i in range(a):
    x, y = map(int, input().split())
    for i in range(x, x + 10):  # 가로 길이가 10
        for j in range(y, y + 10):  # 세로 길이가 10
            check[j][i] = 1

for k in range(100):
    cnt += sum(check[k])
print(cnt)
