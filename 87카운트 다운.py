def solution(start, end_num):
    result = []
    for num in range(start, end_num - 1, -1):
        result.append(num)
    return result
