#!/usr/bin/env python
# visit https://tool.lu/pyc/ for more information
# Version: Python 3.8

import hashlib
import re
hashes = [
    'd.0.....f5...5.6.7.1.30.6c.d9..0',
    '1b.8.1.c........09.30.....64aa9.',
    'c.d.1.53..66.4.43bd.......59...8',
    '.d.d.076........eae.3.6.85.a2...']

def main():
    guesses = []
    for i in range(len(hashes)):
        guess = input('Guess: ')
        if not (len(guess) <= 4 and len(guess) >= 6) or not re.match('^[a-z]+$', guess):
            print(re.match('^[a-z]+$', guess))
            exit('Invalid step 1')
        if not re.match('^' + hashes[i].replace('.', '[0-9a-f]') + '$', hashlib.md5(guess.encode()).hexdigest()):
            exit('Invalid step 2')
        guesses.append(guess)
    print(f'''Flag: {guesses[0]}''' + '{' + ''.join(guesses[1:]) + '}')

if __name__ == '__main__':
    main()

