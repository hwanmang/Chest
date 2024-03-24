codes = {
    '063': 0,
    '010': 1,
    '093': 2,
    '079': 3,
    '106': 4,
    '103': 5,
    '119': 6,
    '011': 7,
    '127': 8,
    '107': 9
}

while True:
    input_str = input()
    if input_str == "BYE":
        break

    A, B = input_str.rstrip("=").split("+")

    A_decimal = ''.join(str(codes[A[i:i+3]]) for i in range(0, len(A), 3))
    B_decimal = ''.join(str(codes[B[i:i+3]]) for i in range(0, len(B), 3))

    try:
        C_decimal = str(int(A_decimal) + int(B_decimal))

        C_code = ""
        for digit in C_decimal:
            for key, value in codes.items():
                if value == int(digit):
                    C_code += key
                    break
        print(A + "+" + B + "=" + C_code)
    except ValueError:
        print("error")
