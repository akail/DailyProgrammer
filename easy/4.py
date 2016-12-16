#!/usr/bin/env python3

from os import urandom
from base64 import b64encode
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', help='Password Length', type=int, default=10)
parser.add_argument('-n', '--number', help='Number of passwords', type=int, default=1)
args = parser.parse_args()

def generate_password(length=10):
    print(b64encode(urandom(length)).decode('utf8')[0:length])

if __name__ == "__main__":
    for i in range(args.number):
        generate_password(args.length)
