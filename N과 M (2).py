N, M = map(int, input().split())

numberlist = []
used = [False] * (N + 1)  # 숫자가 사용되었는지 여부를 저장하는 리스트


def suyeol():
    if len(numberlist) == M:
        print(' '.join(map(str, numberlist)))
        return
    for i in range(1, N + 1):
        if not used[i]:  # 숫자가 사용되지 않았으면 추가
            numberlist.append(i)
            used[i] = True
            suyeol()
            numberlist.pop()
            used[i] = False  # 재귀가 끝나면 다시 사용되지 않았음으로 표시


suyeol()
