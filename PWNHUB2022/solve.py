from base64 import b64decode

f = open('res.txt', 'w')

def deal(msg, Type):
    padlength = 16 - (len(msg) % 16)
    if padlength <= 8:
        pad = ' '*(padlength*3)
    else:
        pad = ' '*(padlength*3 + 1)
    for i in range((len(msg) - 1) // 16 + 1):
        if Type == 1:
            print(" "*5, end='')
            f.write(" "*5)
        print(f"{i*16:08x}  ", end='')
        f.write(f"{i*16:08x}  ")
        ch = []
        for b in range(len(msg[i*16: i*16+16])):
            if b == 7 or b == 15:
                print(f"{msg[b+i*16]:02x} ", end=' ')
                f.write(f"{msg[b+i*16]:02x} ")
            else:
                print(f"{msg[b+i*16]:02x} ", end='')
                f.write(f"{msg[b+i*16]:02x} ")
            if msg[b+i*16]<=126 and msg[b+i*16] >= 32:
                ch.append(chr(msg[b+i*16]))
            else:
                ch.append('.')
        if i == (len(msg)-1) // 16:
            print(pad, end='')
            f.write(pad)
            ch.insert(7, ' ')
            m = ''.join(ch)
            print(m, end='')
            f.write(m)
            if padlength <= 8:
                print(' '*padlength, end='')
                f.write(' '*padlength + '\n')
            else:
                print(' '*(padlength+1), end='')
                f.write(' '*(padlength+1) + '\n')
        else:
            ch.insert(7, ' ')
            m = ''.join(ch)
            print(m)
            f.write(m + '\n')

if __name__ == "__main__":
    n = int(input().strip())
    for r in range(n):
        Type, msg = input().strip().split(' ')
        Type = int(Type)
        msg = msg.encode()
        deal(b64decode(msg), Type)
        if r != n-1:
            print('\n', end='')
            f.write('\n')