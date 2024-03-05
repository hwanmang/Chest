def solution(n):
    digits = []
    hap = 0

    while n > 0:
        digit = n % 10
        digits.append(digit)
        n //= 10

    for i in digits:
        hap += i
    return hap
