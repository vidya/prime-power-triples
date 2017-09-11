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

from math import sqrt
from itertools import takewhile, izip, imap

from functools import wraps
from time import time


class PrimePowerTriples(object):
    def __init__(self, limit_num):
        self.limit_num = limit_num

        primes = self.get_primes()

        squares = filter(self.limit_filter, imap(lambda p: p * p, primes))

        cubes = filter(self.limit_filter, imap(lambda (p, ps): p * ps, izip(primes, squares)))

        fourth_powers = filter(self.limit_filter, imap(lambda ps: ps * ps, squares))

        self.valid_sums = set(fp + c + s
                              for fp in fourth_powers
                              for c in takewhile(lambda pc: self.limit_filter(fp + pc), cubes)
                              for s in takewhile(lambda ps: self.limit_filter(fp + c + ps), squares))

    def get_primes(self):
        primes = [2]

        num_max = int(sqrt(self.limit_num)) + 1

        for p in xrange(3, num_max, 2):
            if all((p % x for x in primes)):
                primes.append(p)

        return primes

    def limit_filter(self, n):
        return n < self.limit_num


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        ret_value = func(*args, **kwargs)
        end = time()

        duration = end - start
        return ret_value, duration

    return wrapper


@time_it
def prime_power_triples_count():
    fifty_million = 50 * 1000 * 1000

    return len(PrimePowerTriples(fifty_million).valid_sums)

# main()
answer, time_taken = prime_power_triples_count()
print('(answer, time_taken): ({0}, {1})'.format(answer, time_taken))