import math

def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

for x, i in enumerate(primes_sieve(999999)):
    if x > 9999:
        print i
        break
