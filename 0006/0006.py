if __name__ == '__main__':
    sum_of_squares = sum(x**2 for x in xrange(1, 101))
    square_of_sum = sum(x for x in xrange(1, 101))**2
    print abs(sum_of_squares - square_of_sum)
