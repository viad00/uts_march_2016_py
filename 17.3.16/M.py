import sys

sys.stdin = open('pack.in')
sys.stdout = open('pack.out', 'w')
l, d = [float(x) for x in input().split()]
r = d / 2
h = (l ** 2 - r ** 2) ** 0.5
print('%.4f' % ((h * r) / (l + r)))
