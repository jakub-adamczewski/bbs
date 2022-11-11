from BBS import BBS

p = 4824863
q = 28804199

bbs = BBS(p=p, q=q)
bits = bbs.generateBits(1_000_000)

stream = "".join(str(bit) for bit in bits)
with open(f'stream.txt', 'w+') as file:
    file.write(stream)
