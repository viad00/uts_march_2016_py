import sys

sys.stdin = open("roman.in", "r")
sys.stdout = open("roman.out", "w")


def usingreadyfunctionsisfinetoo(a_num):
    dict_out = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
                10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
                100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
                1000: 'M'}
    r_num = ''
    for cnt in [1000, 100, 10, 1]:
        num = a_num % (cnt * 10) - a_num % cnt
        if num in dict_out.keys():
            r_num += dict_out[num]
        else:
            if (1 * cnt) < num < (4 * cnt):
                r_num += dict_out[1 * cnt] * (num // cnt)
            elif (5 * cnt) < num < (9 * cnt):
                r_num += dict_out[5 * cnt] + dict_out[1 * cnt] * (num // cnt - 5)
    return r_num


for i in range(int(input())):
    print(usingreadyfunctionsisfinetoo(int(input())))
