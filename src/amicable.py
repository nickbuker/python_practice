def amicable_numbers(n1,n2):
    return sum(get_divisors(n1)) == n2 and sum(get_divisors(n2)) == n1

def get_divisors(n):
    return [x for x in xrange(1, 1 + n/2) if n % x == 0]
