import sys

sys.stdin = open("badsubs.in")
sys.stdout = open("badsubs.out", "w")

n = int(input())

a, b, c = 1, 1, 1
for i in range(n):
    a, b, c = a + b + c, b + c, a + b + c
print(a)
