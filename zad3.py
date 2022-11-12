from BBS import BBS
from Tests import Tests


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc id urna ut tortor viverra gravida nec rutrum diam. Quisque ultrices leo sit amet nulla rutrum, vitae imperdiet quam facilisis. Nam risus nunc, egestas ut risus sit amet, placerat finibus ligula. Mauris malesuada eros vel ipsum sollicitudin pulvinar. Fusce est orci, lacinia eget mattis non, pretium vel ex. Curabitur leo urna, feugiat id feugiat ut, condimentum et felis. Sed sit amet commodo dui. Phasellus vehicula pellentesque metus, in rutrum nulla suscipit ut. In imperdiet massa ante, non hendrerit nulla porttitor vel. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tortor risus, iaculis eget tristique sed, mattis vel tortor. Nullam elementum quam congue ligula fringilla, sit amet feugiat felis eleifend. Phasellus bibendum consequat velit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce in tellus convallis, feugiat tortor et, convallis nisi. Nullam sollicitudin condimentum auctor. Integer lacinia egestas tellus, sed lobortis sem auctor sit amet. Suspendisse aliquam tincidunt neque, in tristique nulla laoreet vitae. Aliquam lacinia egestas varius. Integer in sapien facilisis, placerat ex at, egestas massa. Proin dapibus leo ultricies sollicitudin convallis. Ut ultrices, arcu eget tincidunt gravida, neque purus auctor velit, vel pulvinar nisl eros ut orci. Donec pellentesque justo ut diam sagittis, sit amet iaculis diam convallis. Ut ut eleifend lectus, nec ullamcorper neque. Etiam at porttitor nibh, sit amet consectetur urna. Nam malesuada tortor et diam auctor aliquet. Proin nec vehicula sem, eget pellentesque leo. Suspendisse tincidunt sem eu felis finibus, ac aliquam sem porttitor. Nam ac eleifend tellus. Donec ac aliquet risus, nec ullamcorper elit. Etiam fermentum, massa a efficitur luctus, dolor velit interdum lectus, eget sodales ligula mi sit amet elit. Suspendisse id odio eget elit scelerisque dapibus quis ut risus marcus bueno.'
print("Message:", message)

message_binary = list(map(lambda c: '{0:b}'.format(ord(c)).zfill(10), message))
message_binary_separate_bits = list(map(int, "".join(str(e) for e in message_binary)))
print("Binary message:", "".join(map(str, message_binary_separate_bits)))
print("Binary message len:", len(message_binary_separate_bits))

key_len = len(message_binary_separate_bits)

# (5000011, 5000087)
# (5000011, 5000111)
# (5000087, 5000111)
# (1000000000002791, 1000000000003891)

bbs = BBS(5000087, 5000111)
key = bbs.generateBits(key_len)

print("Key:", "".join(map(str, key)))
print("Key len:", len(key))

encrypted = []
for msg, k in zip(message_binary_separate_bits, key):
    encrypted.append(msg ^ k)

print("Encrypted:", "".join(map(str, encrypted)))
print("Encrypted len:", len(encrypted))

decrypted = []
for encrypted_bit, k in zip(encrypted, key):
    decrypted.append(encrypted_bit ^ k)

print("Decrypted:", "".join(map(str, decrypted)))
print("Decrypted len:", len(decrypted))
decrypted_divided_by_chars = list(map(lambda list: "".join(map(str, list)), list(divide_chunks(decrypted, 10))))

decrypted_chars = []
for binary_char in decrypted_divided_by_chars:
    decrypted_chars.append(chr(int(binary_char, 2)))
print("Decrypted message", "".join(decrypted_chars))

Tests().allTests(encrypted)