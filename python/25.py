cache = {}

def fib(n):
	if n in cache:
		return cache[n]
	elif n == 1 or n == 2:
		return 1
	else:
		value = fib(n-1) + fib(n-2)
		cache[n] = value
		return value

count = 0
for n in xrange(1, 2000000):
	if len(str(fib(n))) == 1000:
		print n
		break