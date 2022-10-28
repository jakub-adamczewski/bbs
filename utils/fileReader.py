def read_file(path):
    bits = []
    with open(path) as f:
        lines = f.readlines()
    f.close()
    for l in lines:
        for c in l:
            if c != '\n':
                assert c in ['0', '1']
                bits.append(int(c))
    return bits
