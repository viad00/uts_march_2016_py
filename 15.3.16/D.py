import sys

sys.stdin = open("ball.in", "r")
sys.stdout = open("ball.out", "w")


def fib(n):
    a, b, c = 1, 2, 4
    if n < 4:
        return [0, a, b, c][n]
    i = 3
    while i < n:
        a, b, c = b, c, a + b + c
        i += 1
    return c


n = int(input())
print(fib(n))
