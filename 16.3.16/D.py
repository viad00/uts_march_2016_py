import sys

sys.stdin = open('incident.in', 'r')
sys.stdout = open('incident.out', 'w')
n, m = map(int, input().split())
s = []
for i in range(m):
    s.append(n * [0])
for i in range(m):
    x, y = map(int, input().split())
    s[i][x - 1] = 1
    s[i][y - 1] = 1
for i in range(n):
    for t in range(m):
        print(s[t][i], end=' ')
    print('\n', end='')
