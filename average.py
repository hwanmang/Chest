# 11번 문제
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def solution(numbers):
    return sum(numbers) / len(numbers)


result = solution(numbers)
print("평균값은:", result)
