n = int(input())
ans = 0
for i in range(n):
    s = list(input())
    stack = [False]
    for j in s:
        if stack[-1] == j:  # 현재 문자가 스택의 맨 위에 있는 문자와 비교
            stack.pop()  # 현재 문자와 같으면 스택에서 제거
        else:
            stack.append(j)  # 그렇지 않으면 스택에 현재 문자를 추가
    if len(stack) == 1:
        ans += 1
print(ans)
