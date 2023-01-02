from pwn import *
from base64 import b64decode, b64encode
import os

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

# context.log_level = 'debug'

sh = remote('47.97.127.1',27457)

sh.sendlineafter(b'> ', b'2')
sh.sendlineafter(b'Which one? ', b'0')
sh.recvuntil(b'Order: ')
order = b64decode(sh.recvline().strip()).split(b'&')
origin_data = order[0] + b'&' + order[1] + b'&' + order[2]
assert order[-1].startswith(b's=')
origin_sign = order[-1][2:]
print(f"origin_data: {origin_data}")

sk_len = 9
pad_data = b'&p=flag'
msg = []
while sk_len <= 20:
    pipeline = os.popen(f"hashpump -s '{origin_sign.decode()}' --data '{origin_data.decode()}' -a '&p=flag' -k {sk_len+1}")
    sign, data = pipeline.read().strip().split('\n')
    sign = sign.encode()
    data = str2byte(data)
    print(sign)
    print(data)
    assert len(sign) == 64
    link = data + b'&s=' + sign
    link = b64encode(link)
    sh.sendlineafter(b'> ', b'3')
    sh.sendlineafter(b"Order: ", link)
    sk_len += 1
    msg = sh.recvline().strip()
    if msg != b'Invalid Order!':
        print(sh.recvline())
        print(sh.recvline())
        sh.close()
        exit()
    else:
        continue
sh.interactive()