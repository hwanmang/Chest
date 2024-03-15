t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))
    temp = [0 for _ in range(n)]
    temp[m] = 1

    count = 0
    while True:
        if arr[0] == max(arr):
            count += 1

            if temp[0] != 1:
                arr.pop(0)
                temp.pop(0)
            else:
                print(count)
                break
        else:
            arr.append(arr.pop(0))
            temp.append(temp.pop(0))
