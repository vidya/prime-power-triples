# https://projecteuler.net/problem=87
#
# Prime power triples
# Problem 87
# The smallest number expressible as the sum of a prime square, prime cube,
# and prime fourth power is 28. In fact, there are exactly four numbers below
# fifty that can be expressed in such a way:
#
# 28 = 2^2 + 2^3 + 2^4
# 33 = 3^2 + 2^3 + 2^4
# 49 = 5^2 + 2^3 + 2^4
# 47 = 2^2 + 3^3 + 2^4
#
# How many numbers below fifty million can be expressed as the sum of a prime
# square, prime cube, and prime fourth power?

from itertools import takewhile, izip

from functools import wraps
from time import time


class PrimePowerTriples(object):
    def __init__(self, limit_num):
        self.limit_num = limit_num

        self.primes = [2]

        valid_primes = takewhile(lambda n: (n * n) < self.limit_num, xrange(3, self.limit_num, 2))

        for p in valid_primes:
            if not any([p % x == 0 for x in self.primes]):
                self.primes.append(p)

        self.prime_squares = filter(self.limit_filter, [p * p
                                                        for p in self.primes])

        self.prime_cubes = filter(self.limit_filter, [p * ps
                                                      for p, ps in izip(self.primes, self.prime_squares)])

        self.prime_fourth_powers = filter(self.limit_filter, [ps * ps
                                                              for ps in self.prime_squares])

    def limit_filter(self, n):
        return n < self.limit_num

    def get_unique_power_triples(self):
        return set([fp + c + s
                    for fp in self.prime_fourth_powers
                    for c in takewhile(lambda pc: (fp + pc) < self.limit_num, self.prime_cubes)
                    for s in takewhile(lambda ps: (fp + c + ps) < self.limit_num, self.prime_squares)])


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        ret_value = func(*args, **kwargs)
        end = time()

        time_taken = end - start
        return ret_value, time_taken

    return wrapper


@time_it
def prime_power_triples_count():
    fifty = 50
    fifty_million = fifty * 1000 * 1000

    pt_set = PrimePowerTriples(fifty_million).get_unique_power_triples()
    return len(pt_set)

# main()
answer, time_taken = prime_power_triples_count()
print('(answer, time_taken): ({0}, {1})'.format(answer, time_taken))