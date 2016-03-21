import sys

sys.stdin = open('maxdist.in')
sys.stdout = open('maxdist.out', 'w')
n = int(input())

city = [[0] * 2 for i in range(n)]
for i in range(n):
    city[i][0], city[i][1] = [int(x) for x in input().split()]
m = int(input())
if m == 0:
    print(-1)
else:
    mas = [[1e6] * n for i in range(n)]
    for i in range(n):
        mas[i][i] = 0
    for i in range(m):
        v1, v2 = [int(x) for x in input().split()]
        mas[v1 - 1][v2 - 1] = ((city[v1 - 1][0] - city[v2 - 1][0]) ** 2 + (
            city[v1 - 1][1] - city[v2 - 1][1]) ** 2) ** 0.5
        mas[v2 - 1][v1 - 1] = ((city[v1 - 1][0] - city[v2 - 1][0]) ** 2 + (
            city[v1 - 1][1] - city[v2 - 1][1]) ** 2) ** 0.5
    for kkk in range(n):
        for i in range(n):
            for j in range(n):
                if mas[i][j] > mas[i][kkk] + mas[kkk][j]:
                    mas[i][j] = mas[i][kkk] + mas[kkk][j]
    max = 1488
    for i in range(n):
        for j in range(n):
            if mas[i][j] == 1e6:
                print(-1)
            else:
                max = 0
    if max != 1488:
        for i in range(n):
            for j in range(n):
                if mas[i][j] > max and mas[i][j] != 1e6: max = mas[i][j]
        print('%.6f' % max)
