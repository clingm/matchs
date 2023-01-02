from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii
from pwnlib.util.iters import mbruteforce
import string
from pwn import xor

alphabet = string.ascii_letters + string.digits
key = b'tdn\\\x93\x15\xa7tgnx\xbc\x13\xf4\x86\xb7'

def encrypt(message):
    message = pad(message, 16)
    aes = AES.new(key, AES.MODE_CBC, iv=b'\x00' * AES.block_size)
    return binascii.hexlify(aes.encrypt(message)[-16:])

GOD = [b'Whitfield__Diffie']

Authentication = encrypt(b'Whitfield__Diffie')
payload = pad(GOD[0], 16) + xor(bytes.fromhex(Authentication.decode()), GOD[0][:-1]) + b'e'
print(encrypt(payload))
print(len(payload))
print(Authentication == encrypt(payload))