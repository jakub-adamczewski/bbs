from BBS import BBS

message = "Witaj świecie!"
print("Message:", message)

bbs = BBS(419, 431)
bits = bbs.generateBits(len(message))
key = "0b" + "".join(map(str, bits))
print("Key:", key)
int_key = int(key, 2)

encrypted = []
for m in message:
    encrypted_char = bin(ord(m) ^ int_key)
    encrypted.append(encrypted_char)
print("Cipher:", "".join(map(str, encrypted)))
# print("Cipher:", encrypted[0])

decrypted = []
for e in encrypted:
    decrypted_char = chr(int(e, 2) ^ int_key)
    decrypted.append(decrypted_char)
print("Decrypted:", "".join(decrypted))
