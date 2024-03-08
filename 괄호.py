def process_parentheses(string):
    count = 0
    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return "NO"
    if count == 0:
        return "YES"
    else:
        return "NO"


T = int(input())
for _ in range(T):
    parentheses_string = input().strip()
    result = process_parentheses(parentheses_string)
    print(result)
