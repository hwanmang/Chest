def solution(n):
    hol = []
    for i in range(n+1):
        if i % 2 == 1:
            hol.append(i)
    return hol
