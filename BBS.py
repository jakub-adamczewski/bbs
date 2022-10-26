from math import gcd
from random import randint

from utils.isPrime import isPrime


class BBS:
    p = 0
    q = 0
    n = 0
    seed = 0
    generatedValues = []

    def __init__(self, p, q):
        assert isPrime(p)
        self.p = p
        assert isPrime(q)
        self.q = q
        if self.p > 0 and self.q > 0:
            self.n = self.p * self.q
            self.__setSeed()

    def __setSeed(self):
        while not gcd(self.n, self.seed) == 1 and self.seed < 1:
            self.seed = randint(0, self.n - 1)

    def __generateValue(self):
        if self.p > 0 and self.q > 0:
            x = 0
            while not gcd(self.n, x) == 1:
                x = randint(0, self.n)
            return pow(x, 2) % self.n

    def generateBits(self, amount):
        assert self.p != self.q
        assert self.n > 0

        bitsArray = []

        a = 0
        while not gcd(self.n, a) == 1:
            a = randint(0, self.n)
        self.generatedValues.append(a)
        bitsArray.append(a % 2)
        amount -= 1

        while amount > 0:
            last = self.generatedValues[-1]
            next = pow(last, 2) % self.n
            self.generatedValues.append(next)
            bitsArray.append(next % 2)
            amount -= 1
        return bitsArray
