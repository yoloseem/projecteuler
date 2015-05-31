if __name__ == '__main__':
    ends = {1: set([1]), 89: set([89])}
    for n in xrange(1, 10000000):
        stack = [n]
        while True:
            top = stack[-1]
            if top in ends[1] or top in ends[89]:
                break
            chain = sum(int(x)**2 for x in str(top))
            stack.append(chain)
        if stack[-1] in ends[1]: end = 1
        elif stack[-1] in ends[89]: end = 89
        for chain in stack[:-1]:
            ends[end].add(chain)
    print len(ends[89])
