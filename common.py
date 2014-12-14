def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

def sumOfDivisors(n):
	count = 0
	for i in xrange(1, n/2 + 2):
		if n % i == 0:
			count += i
	return count

def separateDigits(n):
    digits = []
    value = n

    while value > 0:
        digits.append(value % 10)
        value = value / 10

    return digits