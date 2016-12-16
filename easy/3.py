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

test = encrypt('caesar')
print('caesar')
print(test)
print(decrypt(test))
