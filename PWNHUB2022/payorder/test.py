import os
import string
import random
import time
from hashlib import sha256
from base64 import b64encode, b64decode

def str2byte(str):
    byte = []
    i=0
    while i < len(str):
        if str[i:i+2] != '\\x':
            byte.append(ord(str[i]))
            i+=1
        else:
            byte.append(int(str[i+2:i+4], 16))
            i+=4
    return bytes(byte)

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
sk = ''.join([random.choice(string.printable) for _ in range(10)])
sk_len = len(sk)
_id = 0
product, price = flags[_id]
timestamp = int(time.time()*1000000)
link = f'p={product}&c={price}&t={timestamp}'
sign = sha256(f'k={sk}&{link}'.encode()).hexdigest()
order = f'{link}&s={sign}'.encode()
print(f'Order: {order}')
command = f"hashpump -s '{sign}' --data '{link}' -a '&p=flag' -k {sk_len}"
# print(command)
pipeline = os.popen(command)
newsign, newdata = pipeline.read().strip().split('\n')
newdata = str2byte(newdata)
newlink = newdata + b'&s=' + newsign.encode()


payments = newlink.split(b'&')
assert payments[-1].startswith(b's=') and len(payments[-1]) == 66, "Invalid"
link, sign = newlink[:-67], newlink[-64:]
print(link)
print(sign)
signchk = sha256(f'k={sk}&'.encode() + link).hexdigest()
print(signchk)
print(signchk.encode() == sign)
for payment in payments:
    if payment.startswith(b'p='):
        product = payment[2:].decode()
    if payment.startswith(b'c='):
        coin = int(payment[2:])
print(product, coin)