import sys

sys.stdin = open('step.in', 'r')
# sys.stdout = open('step.out', 'w')
ans = []


def ass(v):
    used[v] = True
    ans.append(v)
    for n in g[v]:
        if not used[n]:
            ass(n)
            ans.append(v)


n, m, v = map(int, input().split())
g = [[] for i in range(n)]
used = [False for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    g[y - 1].append(x)
    g[x - 1].append(y)
print(g)
print(used)
ass(v)
print(ans)
print(used)
