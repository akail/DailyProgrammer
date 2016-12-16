#!/usr/bin/env python3

print("Input 2 of 3 variables F,M,A")
F = input("F= ")
M = input("M= ")
A = input("A= ")

if not A:
    try:
        F = float(F)
        M = float(M)
    except:
        pass
    print("A = {}".format(F/M))
elif not F:
    try:
        A = float(A)
        M = float(M)
    except:
        pass
    print("F = {}".format(A*M))
elif not M:
    try:
        A = float(A)
        F = float(F)
    except:
        pass
    print("M = {}".format(F/A))
