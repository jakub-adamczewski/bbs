from BBS import BBS


def char_to_binary_str(c):
    return '{0:b}'.format(ord(c))


def str_xor(a, b):
    y = int(a, 2) ^ int(b, 2)
    return '{0:b}'.format(y)


message = "Hello World!"
print("Message:", message)

message_binary = list(map(char_to_binary_str, message))
print("Binary message:", message_binary)

key_len = sum(map(lambda x: len(x), message_binary))

bbs = BBS(419, 431)
key = bbs.generateBits(key_len)
key = list(map(str, key))

key_parts = []
last_key_idx = 0
for letter_bin in message_binary:
    new_key_idx = last_key_idx + len(letter_bin)
    key_parts.append(''.join(key[last_key_idx:new_key_idx]))
    last_key_idx = new_key_idx

print("Key parts:", key_parts)

encrypted = []
for letter_bin, key_part in zip(message_binary, key_parts):
    encrypted.append(str_xor(letter_bin, key_part))
print("Encrypted:", encrypted)

decrypted = []
for encrypted_part, key_part in zip(encrypted, key_parts):
    decrypted.append(chr(int(str_xor(encrypted_part, key_part), 2)))
print("Decrypted:", "".join(decrypted))
