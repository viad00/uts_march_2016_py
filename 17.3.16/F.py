import sys

sys.stdin = open("triangle.in")
sys.stdout = open("triangle.out", "w")
p, q = map(float, input().split())
S = float(p * q / 2)
print(S)
print(p, 0)
print(0, 0)
print(0, q)
# maybe?
