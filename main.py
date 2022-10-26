from BBS import BBS
from Tests import Tests
from utils.pqGenerator import PQGenerator
from rx.core import Observer

bits_list = []


def bbs_test(p, q):
    bbs = BBS(p=p, q=q)
    bits = bbs.generateBits(20000)

    bits_list.append(bits)

    try:
        all_tests(bits)
        print("Passed!", p, q, bbs.n)
        print_by_lines(100, -1)

        raise RuntimeError("Found")
    except AssertionError:
        print("Not passed!", p, q, bbs.n)


def all_tests(bits):
    tests = Tests()
    tests.singleBit(bits)
    tests.series(bits)
    tests.longSeries(bits)
    tests.poker(bits)


def print_by_lines(line_size=50, bits_idx=0):
    bits = bits_list[bits_idx]
    assert len(bits) % line_size == 0
    i = 0
    while i < (len(bits) / line_size):
        bits_line = bits[i * line_size:(i + 1) * line_size]
        print(''.join(map(str, bits_line)))
        i += 1


generator = PQGenerator()
observer = Observer(on_next=lambda arg: bbs_test(arg[0], arg[1]))
generator.subject.observers.append(observer)
generator.generate(1_000_000)

# Tests of tests
# print(Tests().singleBit([1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0], validateLen=False))
# print(Tests().series([1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0], validateLen=False))
# print(Tests().longSeries([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], validateLen=False))
