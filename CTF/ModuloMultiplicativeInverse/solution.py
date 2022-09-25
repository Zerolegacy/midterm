import string

msg = ""
raw = ""

with open("msg.enc", 'r') as g:
    for line in g:
        raw = raw + line
    msg = bytes.fromhex(raw)
    print("Orignal")
    print(msg)
    print(raw)

#test = b'\xab\xdc'
#for char in test:
#    print(char)

def dencryption(msg):
    ct = []
    for char in msg:
        #ct.append((123 * char + 18) % 256)
        ct.append(round((179 * (char - 18) % 256) ))
    return bytes(ct)

ct = dencryption(msg)
print("END")
print(ct)
f = open('./msg.txt','w')
f.write(ct.decode("ASCII"))
f.close()