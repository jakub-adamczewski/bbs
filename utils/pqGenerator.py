from utils.isPrime import isPrime
from rx.subject import Subject


class PQGenerator:
    subject = Subject()

    def generate(self, num):
        for q in range(num):
            for p in range(q):
                if isPrime(p) and isPrime(q) and p % 4 == 3 and q % 4 == 3:
                    new_nums = (p, q)
                    self.subject.on_next(new_nums)
