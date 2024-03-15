def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        if i < len(num_list):
            answer.append(num_list[i])
    return answer
