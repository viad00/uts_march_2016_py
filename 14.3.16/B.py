import sys

sys.stdin = open("tobin.in", "r")
sys.stdout = open("tobin.out", "w")
while input() != 0:
    n = int(input())
    print(str(bin(n)).replace('0b', ''))
