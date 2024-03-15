T = int(input())


def preorder(n):
    global result
    if n:
        result += 1
        preorder(left_child[n])
        preorder(right_child[n])


for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    inputlist = list(map(int, input().split()))

    result = 0

    left_child = [0]*(E+2)
    right_child = [0]*(E+2)

    for i in range(0, len(inputlist), 2):
        parent, child = inputlist[i], inputlist[i+1]

        if left_child[parent] == 0:
            left_child[parent] = child
        else:
            right_child[parent] = child

    preorder(N)
    print(f'#{test_case} {result}')
