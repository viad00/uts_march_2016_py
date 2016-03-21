import sys

sys.stdin = open('sum.in')
sys.stdout = open('sum.out', 'w')
n = int(input())
a = list(map(float, input().split()))
b = list(map(float, input().split()))
for i in range(n):
    print(a[i] + b[i], end=' ')
