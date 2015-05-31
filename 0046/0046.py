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

    for odd in xrange(9, 1000000, 2):
        if sieve[odd]: continue
        goldbach = False
        for prime in primes:
            if prime >= odd: break
            if (odd - prime) % 2 == 0:
                if prime + 2 * int(math.sqrt((odd - prime) / 2))**2 == odd:
                    goldbach = True
                    break
        if not goldbach:
            print odd
            break
