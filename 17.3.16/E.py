import sys

sys.stdin = open('product.in')
sys.stdout = open('product.out', 'w')
n = int(input())
a = list(map(float, input().split()))
b = list(map(float, input().split()))
sum = 0
for i in range(n):
    sum += a[i] * b[i]
print('%.3f' % sum)
