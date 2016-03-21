import sys

sys.stdin = open('triangles.in')
sys.stdout = open('triangles.out', 'w')

n = int(input())
mas = [[0] * 2 for i in range(n)]
min = 10000000.0
a, b, c = 0, 0, 0

for i in range(n):
    mas[i][0], mas[i][1] = [float(x) for x in input().split()]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != k and k != j and j != i:
                l1 = ((mas[k][0] - mas[i][0]) ** 2 + (mas[k][1] - mas[i][1]) ** 2) ** 0.5
                l2 = ((mas[k][0] - mas[j][0]) ** 2 + (mas[k][1] - mas[j][1]) ** 2) ** 0.5
                l3 = ((mas[j][0] - mas[i][0]) ** 2 + (mas[j][1] - mas[i][1]) ** 2) ** 0.5
                if (min - l1 - l2 - l3) > 0.0000001:
                    a = k + 1
                    b = i + 1
                    c = j + 1
                    min = l1 + l2 + l3
print(a, b, c)
