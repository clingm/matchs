#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
import string
import random
import socketserver
import signal
from os import urandom
from hashlib import sha256
from flag import FLAG

BANNER = rb"""
.--------.--------.--------.--------.     .--------.--------.--------.--------.--------.
| C.--.  | A.--.  | R.--.  | D.--.  |.-.  | S.--.  | H.--.  | A.--.  | R.--.  | K.--.  |
|  :/\:  |  (\/)  |  :():  |  :/\:  (( )) |  :/\:  |  :/\:  |  (\/)  |  :():  |  :/\:  |
|  :\/:  |  :\/:  |  ()()  |  (__)  |'-.-.|  :\/:  |  (__)  |  :\/:  |  ()()  |  :\/:  |
|  '--'C |  '--'A |  '--'R |  '--'D | (( ))  '--'S |  '--'H |  '--'A |  '--'R |  '--'K |
`--------`--------`--------`--------'  '-'`--------`--------`--------`--------`--------'
"""


class Card:
    def __init__(self):
        random.seed(urandom(32))
        self.cards = []
        for t in ('Hearts', 'Spades', 'Diamonds', 'Clubs'):
            for p in ('J', 'Q', 'K', 'A'):
                self.cards.append(f'{p} {t}')

    def deal(self):
        n = random.getrandbits(4)
        return self.cards[n]


class Task(socketserver.BaseRequestHandler):
    def _recv_all(self):
        BUFF_SIZE = 1024
        data = b''
        while True:
            part = self.request.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data.strip()

    def send(self, msg, newline=True):
        if isinstance(msg, str):
            msg = msg.encode()
        if newline:
            msg += b'\n'
        self.request.sendall(msg)

    def recv(self, prompt='> '):
        self.send(prompt, newline=False)
        return self._recv_all()

    def proof_of_work(self):
        random.seed(urandom(32))
        alphabet = string.ascii_letters + string.digits
        proof = ''.join(random.choices(alphabet, k=32))
        hash_value = sha256(proof.encode()).hexdigest()
        self.send(f'sha256(XXXX+{proof[4:]}) == {hash_value}')
        nonce = self.recv(prompt='Give me XXXX > ')
        if len(nonce) != 4 or sha256(nonce + proof[4:].encode()).hexdigest() != hash_value:
            return False
        return True

    def timeout_handler(self, signum, frame):
        raise TimeoutError

    def handle(self):
        try:
            self.send(BANNER)

            signal.signal(signal.SIGALRM, self.timeout_handler)
            signal.alarm(60)

            if not self.proof_of_work():
                self.send('Wrong!')
                return

            card = Card()
            coin = 5200
            count = 0

            self.send('Greetings! I will give you my secret, if you can guess my card 200 times in a row. '
                      'One coin, one chance.')

            signal.alarm(3600)

            while coin > 0:
                coin -= 1
                c = card.deal()
                r = self.recv(prompt='Your guess > ').decode('l1')
                if r == c:
                    count += 1
                    self.send(f'Correct! Your progress: {count}/200.')
                    if count >= 200:
                        self.send('You are the Card Shark! Flag is yours:')
                        self.send(FLAG)
                        break
                else:
                    count = 0
                    self.send(f'Sorry! My card is {c}.')

            if coin == 0:
                self.send('You have no money! See you another day.')

            self.send('Bye!')

        except TimeoutError:
            self.send('Timeout!')
        except:
            pass
        finally:
            self.request.close()


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == '__main__':
    HOST, PORT = '0.0.0.0', 10000
    print(HOST, PORT)
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
