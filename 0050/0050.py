if __name__ == '__main__':
    sieve = [True] * 1000001
    sieve[0] = sieve[1] = False
    primes = []

    for number in xrange(2, 1000001):
        if sieve[number]:
            for multiple in xrange(number * 2, 1000001, number):
                sieve[multiple] = False
            primes.append(number)
    sum_primes = primes[:1]
    for prime in primes[1:]:
        sum_primes.append(sum_primes[-1] + prime)

    problem_solved = False
    result = 2
    for length in xrange(len(primes), 1, -1):
        for i in xrange(0, len(primes) - length + 1):
            j = i + length
            sum_ = sum_primes[j - 1]
            if i > 0:
                sum_ -= sum_primes[i - 1]
            if sum_ >= 1000000:
                break
            if sieve[sum_]:
                result = sum_
                problem_solved = True
                break
        if problem_solved:
            break
    print result
