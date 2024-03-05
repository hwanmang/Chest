# 10번 문제
# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

def solution(n):
    answer = 0
    for i in range(2, n+1, 2):
        answer += i
    return answer
