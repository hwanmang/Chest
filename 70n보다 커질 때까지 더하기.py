def solution(numbers, n):
    hap = 0
    for i in numbers:
        hap += i
        if hap > n:
            return hap
