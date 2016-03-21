import math
import sys

sys.stdin = open("twoc.in")
sys.stdout = open("twoc.out", "w")
x, y, x1, y1, R, R1 = map(float, input().split())
d = math.sqrt((x1 - x) * (x1 - x) + (y1 - y) * (y1 - y))
if R + R1 == d:
    print('Tangent: outside')
elif R + R1 < d:
    print('Too far')
elif R1 == d + R:
    print('Tangent: 1 in 2')
elif R == d + R1:
    print('Tangent: 2 in 1')
elif R1 > d and R < R1:
    print('1 inside 2')
elif R > d and R1 < R:
    print('2 inside 1')
else:
    print('Intersect')
