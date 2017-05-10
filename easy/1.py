#!/usr/bin/env python3

from unittest import mock
from IPython import embed
#embed()

def read_inputs():

    name = input("What is your name? ")
    age = input("What is your age? ")
    username = input("What is your username? ")

    return "Your name is {}, you are {} years old, and your username is {}".format(name,age,username) 

def main():
    print(read_inputs())

if __name__ == '__main__':
    main()

class Test:
    def test_function(self):
        assert read_inputs() == "Your name is test, you are test years old, and your username is test"

    def setup_method(self):
        global input
        self.old_input = input
        input = lambda x: 'test'

    def teardown_method(self):
        input = self.old_input
