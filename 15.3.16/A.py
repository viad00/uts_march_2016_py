import sys

sys.stdin = open("sum.in", "r")
sys.stdout = open("sum.out", "w")
a, b = map(int, input().split())
print(a + b)
