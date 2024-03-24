from collections import deque


def decreasing_num(n):
    if n < 10:
        return n
    queue = deque(range(1, 10))
    count = 9

    while queue:
        num = queue.popleft()
        last_digit = num % 10
        for i in range(last_digit):  # 마지막 자리 숫자보다 작은 숫자를 추가
            find_num = num * 10 + i
            queue.append(find_num)
            count += 1
            if count == n:
                return find_num
    return -1  # n이 감소하는 수의 개수보다 클 경우


n = int(input())
print(decreasing_num(n))
