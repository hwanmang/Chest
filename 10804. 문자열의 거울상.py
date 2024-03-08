T = int(input())

for test_case in range(1, T+1):
    case = input()
    text = ''
    for i in case[::-1]:
        if i == 'b':
            text += 'd'
        elif i == 'd':
            text += 'b'
        elif i == 'p':
            text += 'q'
        else:
            text += 'p'
    print('#' + str(test_case), text)
