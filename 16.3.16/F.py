import sys

sys.stdin = open('wave.in', 'r')
sys.stdout = open('wave.out', 'w')
n, m, start = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    g[y - 1].append(x)
    g[x - 1].append(y)
visited = set()
Q = []
BFS = []


def bfs(v):
    if v in visited:
        return
    visited.add(v)
    BFS.append(v)
    for i in g[v - 1]:
        if not i in visited:
            Q.append(i)
    while Q:
        bfs(Q.pop(0))


bfs(start)
print(len(BFS))
print(*BFS)
