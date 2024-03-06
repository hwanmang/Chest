max_number = 0
row = 1
column = 1

for i in range(1, 10):
    input_list = list(map(int, input().split()))

    for j, num in enumerate(input_list, 1):
        if num > max_number:
            max_number = num
            row = i
            column = j

print(max_number)
print(row, column)
