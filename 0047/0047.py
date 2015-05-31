import math

if __name__ == '__main__':
    sieve = [True] * 1000000
    sieve[0] = sieve[1] = False
    primes = []

    for number in xrange(2, 1000000):
        if sieve[number]:
            for multiple in xrange(number * 2, 1000000, number):
                sieve[multiple] = False
            primes.append(number)

    factor_sets = [set()] * 6
    consecutive = 0
    for x in xrange(6, 100000000):
        num = x
        factors = set()
        upper_factor = int(math.sqrt(x))
        for prime in primes:
            if prime > upper_factor:
                break
            while x % prime == 0:
                x /= prime
                factors.add(prime)
        if x > 1:
            factors.add(x)
        factor_sets.append(factors)
        if len(factors) == 4:
            consecutive += 1
            if consecutive == 4:
                print num - 3
                break
        else:
            consecutive = 0
