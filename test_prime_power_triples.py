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

from prime_power_triples import PrimePowerTriples


def test_1_bound_30():
    upper_bound = 30

    actual_count = PrimePowerTriples(upper_bound).power_triple_count
    expected_count = 1

    assert actual_count == expected_count


def test_2_bound_40():
    upper_bound = 40

    actual_count = PrimePowerTriples(upper_bound).power_triple_count
    expected_count = 2

    assert actual_count == expected_count


def test_3_bound_50():
    upper_bound = 50

    actual_count = PrimePowerTriples(upper_bound).power_triple_count
    expected_count = 4

    assert actual_count == expected_count


def test_4_bound_fifty_million():
    fifty_million = 50 * 1000 * 1000

    actual_count = PrimePowerTriples(fifty_million).power_triple_count
    expected_count = 1097343

    assert actual_count == expected_count

