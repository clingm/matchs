#!/usr/bin/python3
#coding:utf-8
import time
import string
import random
import signal
from hashlib import sha256
from secret import flag
from base64 import b64encode, b64decode

coins = 1000
sk = ''.join([random.choice(string.printable) for _ in range(random.randint(10, 20))])

flags = [
  ('f', 10), 
  ('l', 10), 
  ('a', 10), 
  ('g', 10), 
  ('fl', 100), 
  ('la', 100), 
  ('ag', 100), 
  ('fla', 1000), 
  ('lag', 1000), 
  ('flag', 10000),
]

def show():
    x = 0
    for name, coin in flags:
        print(f"{x}. {name:4s} -> {coin:6d}")
        x += 1

def order():
    _id = int(input('Which one? '))
    product, price = flags[_id]
    timestamp = int(time.time()*1000000)
    link = f'p={product}&c={price}&t={timestamp}'
    sign = sha256(f'k={sk}&{link}'.encode()).hexdigest()
    link = b64encode(f'{link}&s={sign}'.encode()).decode()
    print(f'Order: {link}')

def pay():
    global coins
    link = b64decode(input('Order: '))
    payments = link.split(b'&')
    assert payments[-1].startswith(b's=') and len(payments[-1]) == 66, "Invalid"

    link, sign = link[:-67], link[-64:]
    signchk = sha256(f'k={sk}&'.encode() + link).hexdigest()
    if signchk.encode() != sign:
        print('Invalid Order!')
        return False

    for payment in payments:
        if payment.startswith(b'p='):
            product = payment[2:].decode()
        if payment.startswith(b'c='):
            coin = int(payment[2:])

    if coins < coin:
        print('Go away you poor bastard!')
        return False

    coins -= coin
    print(f'Your current coins: {coins}')
    print(f'You have bought {product}')
    if product == 'flag':
        print(f'Good job! Here is your flag: {flag}')

def menu():
    funcs = [show, order, pay, exit]
    print("Welcome Flag Store")
    for _ in range(100):
        print(f"Your Coins: {coins}")
        print("1. Show flags")
        print("2. Get order")
        print("3. Pay coin")
        print("4. Bye~")
        funcs[int(input('> ')) - 1]()

if __name__ == "__main__":
    signal.alarm(60)
    menu()