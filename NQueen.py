n = int(input())  # n Queens Problem

queens = [0] * n  # 각 row별 Queen의 위치를 저장할 배열
result = 0


def is_promising(row):
    for before_row in range(row):  # 이전 row까지 체크
        if (queens[row] == queens[before_row]) or (
            abs(queens[row] - queens[before_row]) == abs(row - before_row)
        ):
            return False
    return True


def n_queens(row):
    global result
    if row == n:
        result += 1
        return

    for col in range(n):
        queens[row] = col  # 이번 Queen 두기 (row, col)
        if is_promising(row):  # 이번 row까지 괜찮은지 체크 (유망여부)
            n_queens(row + 1)


# main
n_queens(0)  # 첫 row부터 탐색시작
print(result)  # 결과 출력
