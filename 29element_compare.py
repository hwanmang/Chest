def solution(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    common = s1 & s2
    return len(common)
