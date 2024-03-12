num = int(input())


def fib(n):
    f = [0] * (n+1)
    f[1], f[2] = 1, 1
    for i in range(3, n+1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


def fibonacci(n):
    return n - 2  # n-2번 쨰 인덱스 임


print(fib(num), fibonacci(num))
