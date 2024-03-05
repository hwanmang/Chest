def solution(num_list):
    hol = 0
    jjak = 0

    for i in num_list:
        if i % 2 == 0:
            jjak += 1
        else:
            hol += 1

    return jjak, hol
