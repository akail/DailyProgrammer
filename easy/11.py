#!/usr/bin/env python3

########################################
# Post: https://www.reddit.com/r/dailyprogrammer/comments/pwons/2192012_challenge_11_easy/
########################################

import click
from math import floor
import datetime

R = list(range(1,13))
MONTH_DICT = dict(zip(R, R[-2:] + R[:-2]))

def weekday(month, day, year):
    r = list(range(1,13))
    if month < 3:
        year -= 1
    month = MONTH_DICT[month]
    century = floor(year / 100)
    year = year % 100
    print(day, century, year, month)
    #return (day + floor(13*(month+1)/5) + year + floor(year/4) + floor(century/4) -2*century) % 7

    return (day + floor(2.6*month - 0.2) + year + floor(year/4) + floor(century/4) -2*century) % 7



@click.command()
@click.argument('month', type=int)
@click.argument('day', type=int)
@click.argument('year', type=int)
def main(month, day, year):
    print(weekday(month, day, year))

if __name__ == '__main__':
    main()


def test_pass():
    sd = datetime.date(2017, 1, 1)
    delta = datetime.timedelta(days=1)

    r = list(range(0,7))
    d = dict(zip(r[-1:] + r[:-1], r))
    for i in range(30):
        assert d[sd.weekday()] == weekday(sd.month, sd.day, sd.year)
        sd += delta

def test_month_dictionary():
    assert MONTH_DICT[1] == 11
    assert MONTH_DICT[5] == 3
