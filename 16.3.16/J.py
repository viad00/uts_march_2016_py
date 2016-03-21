import sys

sys.stdin = open('floyd.in', 'r')
# sys.stdout = open('floyd.out', 'w')
n = int(input())
W = []
for k in range(n):
    for i in range(n):
        for j in range(n):
            W[i][j] = min(W[i][j], W[i][k] + W[k][j])
