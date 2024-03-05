def solution(n, k):
    service = 0
    if n >= 10:
        service = n // 10
    return n * 12000 + k * 2000 - service * 2000
