#!/usr/bin/env python3

import pytest

class InvalidInput(Exception):
    pass

def read_inputs():
    print("Input 2 of 3 variables F,M,A")
    F = input("F= ")
    M = input("M= ")
    A = input("A= ")
    return F, M, A

def get_result(F, M, A):
    if not A:
        try:
            F = float(F)
            M = float(M)
        except ValueError:
            raise InvalidInput('Invalid input.  Please use numeric values')
        return "A", F/M
    elif not F:
        try:
            A = float(A)
            M = float(M)
        except ValueError:
            raise InvalidInput('Invalid input.  Please use numeric values')
        return "F", A*M
    elif not M:
        try:
            A = float(A)
            F = float(F)
        except ValueError:
            raise InvalidInput('Invalid input.  Please use numeric values')
        return "M", F/A
    raise Exception("Invalid inputs")

def main():
    F,M,A = read_inputs()
    print("{} = {}".format(*get_result(F,M,A)))

if __name__ == '__main__':
    main()


def test_function():
    assert get_result(1,2, None) == ('A', 0.5)
    assert get_result(1,None, 2) == ('M', 0.5)
    assert get_result(None,1, 2) == ('F', 2)

def test_exceptions():
    with pytest.raises(InvalidInput):
        get_result('a',None,2)
    with pytest.raises(InvalidInput):
        get_result(None,'a',2)
    with pytest.raises(InvalidInput):
        get_result(2,None,'a')

def test_all_inputs():
    with pytest.raises(Exception):
        get_result(1,2,3)

