def solution(a, b):
    c = str(a)+str(b)
    d = 2 * a * b
    if int(c) > int(d):
        return int(c)
    else:
        return int(d)
