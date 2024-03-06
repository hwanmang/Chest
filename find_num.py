a = int(input())
number = list(map(int, input().split()))
b = int(input())
target = list(map(int, input().split()))
number.sort()


def binary_search(number, i, start, end):
    if start > end:  # 탐색 범위가 없으므로 0 반환
        return 0
    mid = (start + end) // 2
    if i == number[mid]:  # 찾는 수가 있으면 1
        return 1
    elif i > number[mid]:  # 찾는 수가 중간 보다 크면 mid 보다 오른쪽에서 탐색
        return binary_search(number, i, mid + 1, end)
    else:  # 찾는 수가 중간 보다 작으면 mid 보다 왼쪽에서 탐색
        return binary_search(number, i, start, mid - 1)


for i in target:
    print(binary_search(number, i, 0, a - 1))
