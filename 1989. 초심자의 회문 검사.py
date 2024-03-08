def is_palindrome(word):
    return word == word[::-1]


T = int(input())
for i in range(1, T + 1):
    input_word = input()
    if is_palindrome(input_word):
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')
