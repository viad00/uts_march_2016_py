import sys

sys.stdin = open("mul.in", "r")
sys.stdout = open("mul.out", "w")
a, b = map(int, input().split())
print(a * b)
