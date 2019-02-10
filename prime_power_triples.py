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

# Answer: 1097343

from math import sqrt

from functools import wraps
from time import time


class PrimePowerTriples(object):
    def __init__(self, upper_bound):
        self.upper_bound = upper_bound

    def get_primes(self):
        primes = [2]

        factor_limit = int(sqrt(self.upper_bound)) + 1

        for p in range(3, factor_limit, 2):
            if all((p % x for x in primes)):
                primes.append(p)

        return primes

    def power_triple_count(self):
        primes = self.get_primes()

        squares = [x for x in (n * n for n in primes)
                   if x < self.upper_bound]

        cubes = [x for x in (p * ps for p, ps in zip(primes, squares))
                 if x < self.upper_bound]

        fourth_powers = [x for x in (n * n for n in squares)
                         if x < self.upper_bound]

        power_triples = set(fourth_power + cube + square
                            for fourth_power in fourth_powers
                            for cube in [cube for cube in cubes
                                         if (fourth_power + cube) < self.upper_bound]
                            for square in [square for square in squares
                                           if (fourth_power + cube + square) < self.upper_bound])

        return len(power_triples)


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

    return PrimePowerTriples(fifty_million).power_triple_count


# main()
# answer, time_taken = prime_power_triples_count()
# print('(answer, time_taken): ({0}, {1})'.format(answer, time_taken))