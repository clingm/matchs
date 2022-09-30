from ecdsa import ellipticcurve as ecc
import random
import socketserver
import signal
from secret import FLAG


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        signal.alarm(0)
        main(self.request)


class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


class PRNG:

    def __init__(self, seed):
        self.r = random.Random()
        self.r.seed(seed)
        self.a = 0xbc065f4ce6891a5e745086e7e5d003ee014f60ebdf4deefdfba869529833f5466
        self.b = 0xedf08f789e02559963f1cba5779d2c09c6716e35e712374ed3d6e63bca2831e0a
        self.p = 0x1477873e878e09f725474b2f2f5417c5dc99eb0ee0317d037cb5b3aae85d25071f
        self.Gx = 0x753e1cede8ef417047a50f6e8cd41ccdc7b94aedf39ae1129cf2567231934a3a8
        self.Gy = 0xdeea7376f435ddfdcf239f371b7b83fa0c359120a8db4178706323c160d427536
        self.E = ecc.CurveFp(self.p, self.a, self.b)
        self.G = ecc.Point(self.E, self.Gx, self.Gy, self.p)

    def next(self):
        multiplier = self.r.getrandbits(32)
        return multiplier * self.G


def sendMessage(s, msg):
    s.send(msg.encode())


def receiveMessage(s, msg):
    sendMessage(s, msg)
    return s.recv(4096).decode().strip()


def main(s):
    rng = PRNG(random.randint(0, 2**64))
    points = 666
    while True:
        location = rng.next()
        guess = receiveMessage(s, "\nGuess the location of the beaver: ")
        try:
            x, y = guess.split(",")

            if (int(location.x()) == int(x)) and (int(location.y()) == int(y)):
                sendMessage(s, "\nCorrect!\n")
                points += 10
            else:
                sendMessage(s, f"\nThe correct location was: {location}\n")
                points -= 1
        except:
            sendMessage(s, f"\nSomething went wrong!\n")

        if points > 1000:
            sendMessage(s, FLAG)
            exit()
        elif points == 0:
            sendMessage(s, "\nGame over\n")
            exit()
        else:
            sendMessage(s, f"\nYour points are = {points}\n")


if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer(("0.0.0.0", 1337), Handler)
    server.serve_forever()
