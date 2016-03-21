import sys

sys.stdin = open("vector.in")
sys.stdout = open("vector.out", "w")
x, y, z = map(float, input().split())
print((x ** 2 + y ** 2 + z ** 2) ** 0.5)
