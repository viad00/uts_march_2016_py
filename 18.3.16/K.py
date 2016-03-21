import sys

sys.stdin = open('smooth.in')
sys.stdout = open('smooth.out', 'w')

n = int(input())

mas = [[0] * n for i in range(12)]
for i in range(2, 11):
    mas[i][0] = 1
for i in range(1, n):
    for j in range(1, 11):
        mas[j][i] = mas[j - 1][i - 1] + mas[j][i - 1] + mas[j + 1][i - 1]
sum = 0
for i in range(1, 11):
    sum += mas[i][n - 1]
print(sum)
