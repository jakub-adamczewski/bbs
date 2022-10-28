def print_by_lines(bits, line_size=50):
    assert len(bits) % line_size == 0
    i = 0
    while i < (len(bits) / line_size):
        bits_line = bits[i * line_size:(i + 1) * line_size]
        print(''.join(map(str, bits_line)))
        i += 1
