def sumOfDivisors(n):
	count = 0
	for i in xrange(1, n/2 + 2):
		if n % i == 0:
			count += i
	return count

result = {}
count = 0
for n in xrange(10000):
	value = sumOfDivisors(n)
	if value in result.keys() and value != 1 and value < n:
		if result[value] == n:
			count += n + value
	result[n] = value

print count