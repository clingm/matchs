from Crypto.Util.number import *
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import socketserver
from secret import flag,d,secret_msg
n = 371181735793602263214407627064240752682904360651839790776279730010108199446252957056492894355059407687871720163518170980583353114277037220782340139305099588912125378884020671883469062462569008314657315818574495963121817239379332744134361151790721596229985450872751373651410837059421397267220864420956837719
e = 0x10001
sec = secret_msg + get_random_bytes(69) 
assert 96 < len(sec) < 128
# but the flag is not too long! only the former !
assert pow(2,e*d,n)==2
enc = pow(bytes_to_long(sec),e,n)


class Task(socketserver.BaseRequestHandler):
    def _recvall(self):
        BUFF_SIZE = 2048
        data = b''
        while True:
            part = self.request.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data.strip()

    def send(self, msg, newline=True):
        try:
            if newline:
                msg += b'\n'
            self.request.sendall(msg)
        except:
            pass

    def recv(self, prompt=b'[-] '):
        self.send(prompt, newline=False)
        return self._recvall()

    def handle(self):
        self.send(b"My enc is :" + str(enc).encode())
        self.send(b"My n is :" + str(n).encode())
        k = get_random_bytes(32)
        iv = get_random_bytes(16)
        self.cipher = AES.new(k, AES.MODE_CBC, iv)
        while 1:
            try:
                self.send(b"Enter a message you want to sign: ")
                inp = int(self.recv(),16)
                tmp = long_to_bytes(inp)
                if tmp == secret_msg:
                    self.send(b'you guess right!flag is:'+flag)
                    break
                assert 0 < inp < n
                self.send(b"signed message (encrypted with military-grade aes-256-cbc encryption):")
                self.send(self.cipher.encrypt(pad(long_to_bytes(pow(inp,d,n)).rjust(16,b'\x00'),32)).hex().encode())
                # To make sure that the lenngth of the oringinal msg is bigger than 16 ,and after padding,the length is a multiply of 32.
            except:
                self.send(b"bad input,exit.")
        self.request.close()

class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10001
    print("HOST:POST " + HOST+":" + str(PORT))
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever() 
