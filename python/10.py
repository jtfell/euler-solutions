from common import *


    
result = 0
for x in primes_sieve(2000000):
    result += x
print result