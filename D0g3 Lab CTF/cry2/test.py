from pwnlib.util.iters import mbruteforce
from Crypto.Cipher import AES

flag = b'D0g3{BUhN2Qsc6aZt2Voecd}'


flag1, flag2 = flag[:8], flag[8:]
aes = AES.new(flag2, AES.MODE_ECB)


ct = aes.encrypt(flag2)
print(ct)
print(aes.decrypt(ct))