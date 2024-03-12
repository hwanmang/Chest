def solution(myString, pat):
    answer = myString.replace("A", "X").replace("B", "A").replace("X", "B")
    if pat in answer:
        return 1
    else:
        return 0
