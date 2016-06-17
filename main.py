# find rows
import random

maxsize = 10


def gennxnxn():
    a = []
    for i in range(maxsize):
        a.append([])
        for j in range(maxsize):
            a[i].append([])
            for l in range(maxsize):
                a[i][j].append(random.randint(0, 9))
    return a


def max_st(a):
    maxi = -1
    for j in range(maxsize):
        for l in range(maxsize):
            summ = 0
            for i in range(maxsize):
                summ += a[i][j][l]
            if summ > maxi:
                maxi = summ
                posi = j, l

    maxj = -1
    for i in range(maxsize):
        for l in range(maxsize):
            summ = 0
            for j in range(maxsize):
                summ += a[i][j][l]
            if summ > maxj:
                maxj = summ
                posj = i, l

    maxl = -1
    for i in range(maxsize):
        for j in range(maxsize):
            summ = 0
            for l in range(maxsize):
                summ += a[i][j][l]
            if summ > maxl:
                maxl = summ
                posl = i, j

    return posi, posj, posl


print(max_st(gennxnxn()))