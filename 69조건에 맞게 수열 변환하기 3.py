def solution(arr, k):
    if k % 2 == 1:
        return [k * i for i in arr]
    else:
        return [k + i for i in arr]
