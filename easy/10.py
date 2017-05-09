#!/usr/bin/env python3

########################################
# Post: https://www.reddit.com/r/dailyprogrammer/comments/pv98f/2182012_challenge_10_easy/
########################################

import re

def check_number(number):
    return bool( re.search(r'[\(]?\d{3}[\)]?[\s\.\-]?\d{3}[\.-]?\d{4}', number) )


def main():
    pnum = input('Phone Number: ')
    if check_number(pnum):
        print("Its a phone number")
    else:
        print("Bad number")

if __name__ == '__main__':
    main()


def test_pass():
    assert check_number("1231231234")
    assert check_number("123-123-1234")
    assert check_number("123.123.1234")
    assert check_number("(123)123-1234")
    assert check_number("(123) 123-1234")

def test_fail():
    assert check_number("123-45-6789") == False
    assert check_number("123:4567890") == False
    assert check_number("123/456-7890") == False
