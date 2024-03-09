def solution(arr1, arr2):
    hap1 = sum(arr1)
    hap2 = sum(arr2)

    if len(arr1) > len(arr2):
        return 1
    elif len(arr1) < len(arr2):
        return -1
    else:
        if hap1 > hap2:
            return 1
        elif hap1 < hap2:
            return -1
        else:
            return 0
