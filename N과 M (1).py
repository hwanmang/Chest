def find_sequence(select):
    if len(select) == m:
        print(*select)
    for i in range(1, n+1):
        if i not in select:
            select.append(i)
            find_sequence(select)
            select.pop()
    return


n, m = map(int, input().split())

find_sequence([])
