import sys

sys.stdin = open("toany.in", "r")
sys.stdout = open("toany.out", "w")

a = [line.strip() for line in sys.stdin.readlines()]

for i in range(len(a)):
    org = int(a[i])
    to = int(a[i + 1])
    i = +1
    b = []
    while org != 0:
        new = org // to
        b.append(org - new * 2)
