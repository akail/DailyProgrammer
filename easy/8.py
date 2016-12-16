#!/usr/bin/env python3

import sys

try:
    bottles = sys.argv[1]
except TypeError:
    print("Not an integer!")
except IndexError:
    bottles = 99

for i in range(bottles, 0, -1):
    print("{} bottles of beer on the wall".format(i), end=' ')
    print("{} bottles of beer.".format(i), end=' ')
    print("Take one down pass it around", end=' ')
    print("{} bottles of beer.".format(i-1), end=' ')


