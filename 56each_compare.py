def solution(a, b):
    c = str(a)+str(b)
    d = 2 * a * b
    if int(c) > int(d):
        return int(c)
    else:
        return int(d)


def solution(a, b):
    if str(a)+str(b) > str(b)+str(a):
        return int(str(a)+str(b))
    else:
        return int(str(b)+str(a))
