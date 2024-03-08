def solution(num_list):
    hol = [str(i) for i in num_list if i % 2 == 1]
    holsum = ''.join(hol)
    jjak = [str(i) for i in num_list if i % 2 == 0]
    jjaksum = ''.join(jjak)
    return int(holsum) + int(jjaksum)
