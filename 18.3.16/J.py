import sys

sys.stdin = open("slalom.in")
sys.stdout = open("slalom.out", "w")

n = int(input())
s = []
for i in range(n):
    s.append([])
    for j in range(i + 1):
        s[i].append(1)
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(i):
        s[i][j] = a[i][j] + max(s[i - 1][j - 1], s[i - 1][j])
ss = s[n - 1][0]
for i in range(n):
    if s[n - 1][i] > ss:
        ss = s[n - 1][i]
print(ss)
