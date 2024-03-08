N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    tree_length = 0
    # 나무 자르기
    for i in tree:
        if mid <= i:
            tree_length += i - mid
        # 잘라진 나무가 충분하니, 높이를 올린다.
    if tree_length >= M:
        start = mid + 1
    # 잘라진 나무가 부족하니, 높이를 내린다.
    else:
        end = mid - 1
print(end)
