import sys

sys.stdin = open('rpn.in', 'r')
sys.stdout = open('rpn.out', 'w')


def slove2(a, do):
    ss = ''
    for i in range(len(a) - 1):
        ss = ss + str(a[i]) + ' ' + do + ' '
    ss = ss + str(a[-1])
    return int(eval(ss))


s = []
answ = int
n = int(input())
for i in range(n):
    var = str(input())
    if '1234567890'.find(var[0]) != -1:
        s.append(int(var))
    else:
        send = [s[-2], s[-1]]
        answ = slove2(send, str(var))
        s.pop()
        s[-1] = answ
print(answ)
