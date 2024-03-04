def solution(array, height):
    top = 0
    for i in array:
        if i > height:
            top += 1
    return top
