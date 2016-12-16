#!/usr/bin/env python3

import sys

morse_2_letter = {'.-': 'a',
                  '-...': 'b',
                  '-.-.': 'c',
                  '-..': 'd',
                  '.': 'e',
                  '..-.': 'f',
                  '--.': 'g',
                  '....': 'h',
                  '..': 'i',
                  '.---': 'j',
                  '-.-': 'k',
                  '.-..': 'l',
                  '--': 'm',
                  '-.': 'n',
                  '---': 'o',
                  '.--.': 'p',
                  '--.-': 'q',
                  '.-.': 'r',
                  '...': 's',
                  '-': 't',
                  '..-': 'u',
                  '...-': 'v',
                  '.--': 'w',
                  '-..-': 'x',
                  '-.--': 'y',
                  '--..': 'z'
                  }

letter_2_morse = { v:k for k,v in morse_2_letter.items()}


def morse_2_string(morse):
    for word in morse.split('/'):
        
        for letter in word.split():
            print(morse_2_letter[letter], end='')

        print(' ', end='')

def string_2_morse(text):
    for word in text.split():
        for letter in word:
            print(letter_2_morse[letter], end=' ')
    print('/', end=' ')

#morse_2_string(' '.join(sys.argv[1:]))
string_2_morse(' '.join(sys.argv[1:]))
