import math
import sys

sys.stdin = open("radius.in")
sys.stdout = open("radius.out", "w")
a = float(input())
d = float(2 * a)
C = float(2 * math.pi * a)
S = float(math.pi * a ** 2)
print('%.3f' % d, '%.3f' % C, '%.3f' % S)
