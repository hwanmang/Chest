iron_stick = input()

stack = []
count_sticks = 0

for i in range(len(iron_stick)):
    if iron_stick[i] == "(":
        stack.append(i)
    elif iron_stick[i] == ")":
        if stack[-1] == i - 1: # 스택 top이 직전 나온 "("과 같을 때
            stack.pop()
            count_sticks += len(stack)
        else:
            stack.pop()
            count_sticks += 1

print(count_sticks)
