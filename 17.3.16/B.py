import sys

# import math
sys.stdin = open("line.in")
sys.stdout = open("line.out", "w")
x, y, xx, yy = map(float, input().split())
a = float(-yy + y)
b = float(xx - x)
c = float(yy - y) * x - (xx - x) * y
print(a, b, c)
