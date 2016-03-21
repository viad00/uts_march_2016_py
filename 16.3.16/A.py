import sys

sys.stdin = open('stack.in', 'r')
sys.stdout = open('stack.out', 'w')
s = []
n = int(input())

for i in range(n):
    command = str(input())
    if command == 'POP':
        x = s[-1]
        s = s[:-1]
        print(x, ' ', s)
    else:
        var = int(command.split()[-1])
        s.append(var)
        print(s)
