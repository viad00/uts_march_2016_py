import sys

sys.stdin = open("maxarray.in", "r")


# sys.stdout = open("maxarray.out", "w")

def max_sum_part(my_list):
    max_sum = 0
    list_length = len(my_list)
    r_border = list_length + 1
    for i in range(list_length):
        for j in range(i + 1, r_border):
            sum_part = sum(my_list[i:j])
            if sum_part > max_sum:
                max_sum, left, right = sum_part, i, j - 1
    return (max_sum, left, right)


n = int(input())
a = [input().split() for i in range(n)]
b = []
for i in range(n):
    for j in range(n):
        a[i][j] = int(a[i][j])
        b.append(a[i][j])
print(a)
print(b)
print(max_sum_part(a[1]))
