if __name__ == '__main__':
    sieve = [True] * 10000
    sieve[0] = sieve[1] = False
    primes_set = {}

    for number in xrange(2, 10000):
        if sieve[number]:
            for multiple in xrange(number * 2, 10000, number):
                sieve[multiple] = False
            if number >= 1000 and number <= 9999:  # 4-digit
                digits = ()
                for digit in sorted(list(set(str(number)))):
                    digits += (int(digit), str(number).count(digit))
                primes_set.setdefault(digits, []).append(number)

    solved = False
    for seq in [sorted(s) for s in primes_set.itervalues() if len(s) >= 3]:
        for i in xrange(0, len(seq) - 3 + 1):
            subseq = seq[i:i + 3]
            if subseq[2] - subseq[1] == subseq[1] - subseq[0]:
                print ''.join(str(n) for n in subseq)
                solved = True
                break
        if solved: break
    if not solved:
        print 'Not found'
