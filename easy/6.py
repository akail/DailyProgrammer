#!/usr/bin/env python3

import math

def get_denom():
    a,b,c = 2,3,4
    while True:
        yield a,b,c
    a += 1
    b += 1
    c += 1

def pi_gregor_leibniz(iterations=100000):
    pi = 4
    mul = -1
    for i in range(3,iterations*2, 2):
        pi += 4/i*mul
        mul *= -1

    return pi

def pi_nilakantha(iterations=1000000):
    pi = 3
    mul = 1
    for i in range(1,iterations):
        pi += mul*4/(8*i**3 + 12*i**2 + 4*i)
        mul *= -1
    return pi

def pi_ramanujan(iterations=3):
    _sum = 0
    for k in range(iterations):
        _sum += math.factorial(4*k)*(1103+26390*k)/( math.factorial(k)**4 * 396**(4*k))

    inv_pi = 2*math.sqrt(2)/9801 * _sum
    return 1/inv_pi


print("{0:.30f}".format(pi_gregor_leibniz()))
print("{0:.30f}".format(pi_nilakantha()))
print("{0:.30f}".format(pi_ramanujan()))
print("{0:.30f}".format(math.pi))


