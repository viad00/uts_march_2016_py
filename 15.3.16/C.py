import sys

sys.stdin = open("fib.in", "r")
sys.stdout = open("fib.out", "w")


def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a


n = int(input())
print(fib(n))
