from encryption import RSA
import socketserver
import signal
import json
import os


class Handler(socketserver.BaseRequestHandler):

    def handle(self):
        signal.alarm(0)
        main(self.request)


class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


def sendMessage(s, msg):
    s.send(msg.encode())


def receiveMessage(s, msg):
    sendMessage(s, msg)
    return s.recv(4096).decode().strip()


def listFiles():
    directory = "files/"
    files = [file for file in os.listdir(directory)]
    return files


def readFile(file_name):
    return open('files/' + file_name, 'r').read()


def main(s):
    rsa = RSA(2048)

    while True:
        try:
            payload = receiveMessage(
                s,
                "\nOptions:\n\n1.Get public key\n2.List files\n3.Access a file\n\n> "
            )
            payload = json.loads(payload)
            option = payload["option"]
            if option == "1":
                public_key = rsa.export_key()
                response = json.dumps({
                    "response": "success",
                    "public_key": public_key
                })
                sendMessage(s, "\n" + response + "\n")
            elif option == "2":
                file_names = listFiles()
                response = json.dumps({
                    'response': 'success',
                    'files': file_names
                })
                sendMessage(s, "\n" + response + "\n")
            elif option == "3":
                file_name = payload["file_name"]
                forged_signature = payload["signature"]

                if rsa.verify(file_name, forged_signature):
                    data = readFile(file_name)
                    response = json.dumps({
                        'response': 'success',
                        'data': data
                    })
                    sendMessage(s, "\n" + response + "\n")
                else:
                    response = json.dumps({
                        "response": "error",
                        "message": "Invalid signature"
                    })
                    sendMessage(s, "\n" + response + "\n")
            else:
                response = json.dumps({
                    "response": "error",
                    "message": "Invalid option"
                })
                sendMessage(s, "\n" + response + "\n")
        except:
            response = json.dumps({
                "response": "error",
                "message": "An error occurred"
            })
            sendMessage(s, "\n" + response + "\n")


if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer(("0.0.0.0", 1337), Handler)
    server.serve_forever()
