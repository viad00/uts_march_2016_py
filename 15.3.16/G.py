import sys

sys.stdin = open("explosion.in", "r")
sys.stdout = open("explosion.out", "w")
n = int(input())
answ = [0, 0, 0, 1, 3, 8, 20, 47, 107, 238, 520, 1121, 2391, 5056, 10616, 22159, 46023, 95182, 196132, 402873, 825259,
        1686408, 3438828,
        6999071, 14221459, 28853622, 58462800, 118315137, 239186031, 483072832, 974791728, 1965486047, 3960221519,
        7974241118,
        16047432332, 32276862265, 64888470307, 130392234088, 261917705028, 525918286159, 1055667578747, 2118381476878,
        4249723155672, 8523283839073, 17090411727175, 34261465233024, 68671253821480, 137615316826095, 275732407969431,
        552387722794670, 1106472935945524]
print(answ[n])
# нет неразрешённых проблем, есть нерешённые задачи
