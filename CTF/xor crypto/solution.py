#!/usr/bin/python3
import os
flag = open('output.txt', 'r').read().strip()

class XOR:
    def __init__(self):
        self.key = os.urandom(4)
    def encrypt(self, data: bytes) -> bytes:
        xored = b''

        # TO GET KEY
        plaintext = "HTB{"
        plaintext = plaintext.encode()
        data1 = b'\x13\x4a\xf6\xe1'
        #data1 = bytearray.fromhex(data1)
        print(data1)
        key = []
        keyused = []
        for i in range(4):
            key = plaintext[i] ^ data1[i]
            print(chr(key))
            keyused.append(key)

        #y = 0
        for i in range(len(data)):
            #if y > 3:
            #    y = 0
            #xored += bytes([data[i] ^ self.key[i % len(self.key)]])
            #xored += bytes([data[i] ^ self.key[i % 4]])
            xored += bytes([data[i] ^ keyused[i % 4]])
            #print(bytes([data[i]]))
            #print(bytes([self.key[i % len(self.key)]]))
            print(bytes([keyused[i % 4]]))
            #y += 1
        return xored
    def decrypt(self, data: bytes) -> bytes:
        return self.encrypt(data)

def main():
    global flag
    flag = bytearray.fromhex(flag)
    crypto = XOR()
    print ('Flag:', crypto.decrypt(flag).decode('utf-8'))

if __name__ == '__main__':
    main()
