# def solution(my_string):
#     mo = {'a', 'e', 'i', 'o', 'u'}
#     result = ''
#     for i in my_string:
#         if i not in mo:
#             result += i
#     return result

def solution(my_string):
    mo = ['a', 'e', 'i', 'o', 'u']
    for i in mo:
        my_string = my_string.replace(i, '')
    return my_string
