#!/usr/bin/env python3

########################################
# Post: https://www.reddit.com/r/dailyprogrammer/comments/pxs2x/2202012_challenge_12_easy/
########################################

import click
from math import factorial

def gen_strings(string):
    """Generates string permutations

    Implements the python version of the itertools.permutation
    function
    """

    pool = tuple(string)
    n = len(pool)
    r = n
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])

    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

@click.command()
@click.argument('string', type=str)
def main(string):
    for p in gen_strings(string):
        print(''.join(p))

if __name__ == '__main__':
    main()


def test_length():
    string = 'te'
    assert len(list(gen_strings(string))) == factorial(len(string))

    string = 'tes'
    assert len(list(gen_strings(string))) == factorial(len(string))

def test_uniques():
    string = 'helo'

    results = [''.join(r) for r in gen_strings(string)]
    assert len(set(results)) == factorial(len(string))
