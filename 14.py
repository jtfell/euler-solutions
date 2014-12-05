cache = {}

def collatz(n):
	if n in cache:
		return cache[n]
	elif n%2:
		return collatz(3*n+1) + 1
	else:
		return collatz(n/2) + 1

cache[1] = 1
for i in xrange(1, 1000000):
	cache[i] = collatz(i)

print max(cache, key=cache.get)