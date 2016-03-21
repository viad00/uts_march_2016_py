import sys

sys.stdin = open("robot.in", "r")
sys.stdout = open("robot.out", "w")
k, X, Y = map(int, input().split())
f = [[[0] * 18 for x in range(18)] for t in range(18)]
f[0][0][0] = 1
for t in range(1, 17):
    for x in range(17):
        for y in range(17):
            f[t][x][y] = f[t - 1][abs(x - 1)][y] + f[t - 1][x][abs(y - 1)] + f[t - 1][x + 1][y] + f[t - 1][x][y + 1]
print(f[k][abs(X)][abs(Y)])
