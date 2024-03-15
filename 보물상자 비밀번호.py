from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())

    arr = deque(list(input()))
    R = N//4
    numlist = set()
    for _ in range(R):
        for i in range(4):
            word = ''.join(list(arr)[i * R:i * R + R])
            hexa = int(word, 16)
            numlist.add(hexa)
        arr.rotate(1)
    numlist = sorted(list(numlist), reverse=True)
    print(f"#{test_case} {numlist[K-1]}")
