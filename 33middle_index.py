def solution(array):
    array.sort()
    length = len(array)
    index = length // 2
    middle = array[index]
    return middle
