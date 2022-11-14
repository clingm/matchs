
f = open("output.txt", 'r')
pubkey = f.readline()
pubkey = eval(pubkey)
c = f.read()
c = eval(c)
s, t, n = pubkey
# enc = b""
# for idx in range(len(c)):
#     c1, c2 = c[idx]
#     if c1 == c2:
#         print(idx)
#     for m in range(0xff+1):
#         try:
#             m_inv = pow(m, -1, n)
#             if pow(c1 * m_inv, t, n) == pow(c2 * m_inv, s, n):
#                 enc += bytes([m])
#                 break
#         except:
#             continue
# assert len(enc) == len(c)
# print(enc)

enc = b'\x08EZg\xbf\xa0\xeb\x9d\x81\x01\xa8\x96m\x97\x08I(\xed\xb5iQE\xdb\xf5\x8c\xbdcr!\xe6\xc9\xac\x0c\x16K\xa0\x0fr\xecM\x04\xe6\x87\x0f}9\x94\xcfa\x16\x87\x8f4\xcd\xcb\xa4\x0eq\xc3Q\x16\x928&\xe2\x18C\xafN\x87\xcc\x18\xc2D\x9d\x06\xbd"\xe7\xe8\xb7\x12\xb0\xb8CC\x9aM\xff\x12\x01\x05,\xeeopYC)mI\xb7\x81\xb6\x13\x0e\x8a\xc0\xd7\xd3\xd2\xa9\xe5vg.\xa4\xf3\xaa\x10f\x9c\xa4nS=O\xe9'
print(enc[90])
print(c[90][0])
print(c[90][1])