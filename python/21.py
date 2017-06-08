from common import *

result = {}
count = 0
for n in xrange(10000):
	value = sumOfDivisors(n)
	if value in result.keys() and value != 1 and value < n:
		if result[value] == n:
			count += n + value
	result[n] = value

print count