for i in range(100):
    ii = i
    ii /= 2
    ii = ii * 3
    ii += 1
    ii /= 2
    ii = ii * 3
    ii += 1
    ii /= 2
    ii = ii * 3
    ii += 1
    print(ii)

    ii -= 1
    ii -= ii / 3
    ii -= 1
    ii -= ii / 3
    ii -= 1
    ii -= ii / 3
    print(' ', ii)
