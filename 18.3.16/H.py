import sys

sys.stdin = open('ones.in')
sys.stdout = open('ones.out', 'w')

n = int(input())

mas = [1] * (n + 1)

if n == 1:
    print(2)
elif n == 2:
    print(4)
elif n == 3:
    print(7)
else:
    mas[1] = 2
    mas[2] = 4
    mas[3] = 7
    for i in range(4, n + 1):
        mas[i] = (mas[i - 1] + mas[i - 2] + mas[i - 3]) % 12345
    print(mas[n])
