def solution(arr, n):
    result = []
    if len(arr) % 2 == 1:
        for i in range(len(arr)):
            if i % 2 == 0:
                result.append(arr[i] + n)
            else:
                result.append(arr[i])
        return result
    elif len(arr) % 2 == 0:
        for i in range(len(arr)):
            if i % 2 == 1:
                result.append(arr[i] + n)
            else:
                result.append(arr[i])
        return result
