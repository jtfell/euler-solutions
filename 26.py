
def cycleLength(n):
	if n % 2 == 0: 
		return cycleLength(n / 2)
	if n % 5 == 0: 
		return cycleLength(n / 5)
	
	i = 1
	while True:
		if not (10**i - 1) % n: 
			return i
		i = i + 1

maxLength = 0
result = 0

for n in xrange(1,1000):

	currentLength = cycleLength(n)

	if currentLength > maxLength:
		maxLength = currentLength
		result = n

print result