N = int(input())  # 수의 개수
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

result = []


def dfs(i, j):
    if (i == N):  # 연산을 마쳤을 경우
        result.append(j)
        return
    if (operators[0] > 0):  # 덧셈 연산
        operators[0] -= 1
        dfs(i+1, j+numbers[i])
        operators[0] += 1

    if (operators[1] > 0):  # 뺄셈연산
        operators[1] -= 1
        dfs(i+1, j-numbers[i])
        operators[1] += 1

    if (operators[2] > 0):  # 곱셈연산
        operators[2] -= 1
        dfs(i+1, j*numbers[i])
        operators[2] += 1

    if (operators[3] > 0):  # 나눗세면산
        operators[3] -= 1
        dfs(i+1, int(j/numbers[i]))
        operators[3] += 1


dfs(1, numbers[0])  # 첫 번째 수열을 카운트하고 시작
print(max(result))  # 가장 큰값
print(min(result))  # 가장 작은값
print(result)
