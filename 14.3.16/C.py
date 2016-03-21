import sys

sys.stdin = open("tohex.in", "r")
sys.stdout = open("tohex.out", "w")

a = [line.strip() for line in sys.stdin.readlines()]

for i in range(len(a)):
    print(str(str(hex(int(a[i]))).replace('0x', '')).upper())
