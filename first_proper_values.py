from BBS import BBS
from Tests import Tests
from utils.fileReader import read_file
from utils.pqGenerator import PQGenerator
from rx.core import Observer

from utils.printer import print_by_lines

bits_list = []
tests = Tests()


def bbs_test(p, q):
    bbs = BBS(p=p, q=q)
    bits = bbs.generateBits(20000)

    bits_list.append(bits)

    try:
        tests.allTests(bits)
        print("Passed!", p, q, bbs.n)
        print_by_lines(bits_list[-1], 100)
        raise RuntimeError("Found")
    except AssertionError:
        print("Not passed!", p, q, bbs.n)


# Test which checks first p and q values, for which FIPS tests are passed
generator = PQGenerator()
observer = Observer(on_next=lambda arg: bbs_test(arg[0], arg[1]))
generator.subject.observers.append(observer)
generator.generate(1_000_000)
