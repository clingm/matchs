from base64 import b64decode

enc = b'QUlgNGoxT2A2empxMQ=='
vi = b64decode(enc)[::-1]

vi = bytes([i - 1 for i in vi])
print(vi)