import sys

sys.stdin = open("bricks.in")
sys.stdout = open("bricks.out", "w")

n = int(input())

if n == 0:
    print(1)
elif n == 1:
    print(0)
elif n == 2:
    print(1)
elif n == 3:
    print(1)
elif n == 4:
    print(1)
elif n == 5:
    print(2)
else:
    a, b, c, d = 1, 1, 2, 1
    for i in range(6, n + 1):
        d = a + b
        a = b
        b = c
        c = d
    print(d)
