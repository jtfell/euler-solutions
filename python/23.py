from common import *
import time

def isAbundant(n):
	if sumOfDivisors(n) > n and n != 2:
		return True
	else:
		return False

t = time.time()
abundantNums = set()
ignores = set()
count = 0

for i in xrange(1, 28123):
	if isAbundant(i):
		abundantNums.add(i)
		for x in abundantNums:
			ignores.add(i + x)

	if i not in ignores:
		possible = False
		for n in xrange(1, i/2 + 1):
			if (i - n) in abundantNums and n in abundantNums:
				possible = True
				break

		if not possible:
			count += i

print time.time() - t
print count
