import sys

sys.stdin = open('trianglep.in')
sys.stdout = open('trianglep.out', 'w')
n = int(input())

for i in range(n):
    xxx, yyy, xxxx, yyyy, x, y = [float(i) for i in input().split()]
    xx, yy = [float(i) for i in input().split()]
    l = (xxx - xx) * (yyyy - yyy) - (xxxx - xxx) * (yyy - yy)
    ll = (xxxx - xx) * (y - yyyy) - (x - xxxx) * (yyyy - yy)
    lll = (x - xx) * (yyy - y) - (xxx - x) * (y - yy)
    if (xx < xxx and xx < xxxx and xx < x) or (xx > xxx and xx > xxxx and xx > x):
        print('NO')
    elif (yy < yyy and yy < yyyy and yy < y) or (yy > yyy and yy > yyyy and yy > y):
        print('NO')
    elif l > 0 and ll > 0 and lll > 0:
        print('YES')
    elif l < 0 and ll < 0 and lll < 0:
        print('YES')
    elif abs(l) < 1e-5 or abs(ll) < 1e-5 or abs(lll) < 1e-5:
        print('YES')
    else:
        print('NO')
