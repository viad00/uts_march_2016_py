import sys

sys.stdin = open('queue.in', 'r')
sys.stdout = open('queue.out', 'w')
s = []
n = int(input())

for i in range(n):
    command = str(input())
    if command == 'GET':
        x = s[-1]
        s = s[:-1]
        print(x, ' ', s)
    else:
        var = int(command.split()[-1])
        s = [var] + s
        print(s)
