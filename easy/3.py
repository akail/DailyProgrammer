#!/usr/bin/env python3

import string

def encrypt(text, shift=3):
    text = text.lower()
    
    alpha = string.ascii_lowercase
    beta = alpha[-shift:] + alpha[0:-shift]

    table = str.maketrans(alpha,beta)
    return text.translate(table)

def decrypt(text, shift=3):
    return encrypt(text, -shift)

def main():


    test = encrypt('caesar')
    print('caesar')
    print(test)
    print(decrypt(test))

if __name__ == '__main__':
    main()

def test_encrypt():
    assert encrypt('d') == 'a'
    assert encrypt('a', shift=-3) == 'd'

    assert encrypt('a') == 'x'
    assert encrypt('x', shift=-3) == 'a'


def test_ignored():
    assert encrypt('1234567890!@#$%^&*()_+{}[]:";\'<>?,./') == '1234567890!@#$%^&*()_+{}[]:";\'<>?,./'
    assert encrypt('d1234567890!@#$%^&*()_+{}[]:";\'<>?,./') == 'a1234567890!@#$%^&*()_+{}[]:";\'<>?,./'
