import sys

sys.stdin = open("gcd.in", "r")
sys.stdout = open("gcd.out", "w")


def nod(a, b):
    if a > b:
        return (nod(a - b, b))
    if a < b:
        return (nod(a, b - a))
    if a == b:
        return (a)


"""rasist jokes (ahaha)"""
killing, niggers = map(int, input().split())
print(nod(killing, niggers))
