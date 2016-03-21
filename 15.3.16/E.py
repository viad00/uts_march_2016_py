import sys

sys.stdin = open("turtle.in", "r")
sys.stdout = open("turtle.out", "w")
n = int(input())
a = [input().split() for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(a[i][j])
b = [[0 for i in range(len(a))] for j in range(len(a))]
for i in range(n):
    for j in range(n):
        b[i][j] = max(b[i - 1][j], b[i][j - 1]) + a[i][j]
print(b[len(b) - 1][len(b) - 1])
