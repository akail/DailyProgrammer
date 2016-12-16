#!/usr/bin/env python3

import getpass

class AuthenticationFailure(Exception):
    pass


def get_creds():
    with open('5.txt') as cred_file:
        data = cred_file.readline()
        data = data.strip()
        return data.split(':')

if __name__ == '__main__':
    u = input('Username: ')
    p = getpass.getpass('Password: ')
    user, password = get_creds()

    if u != user or p != password:
        raise AuthenticationFailure("Bad username or password")
    else:
        print('Authenticated!')


