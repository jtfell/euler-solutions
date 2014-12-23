from common import *

def isPandigitial(xs):
	for i in xrange(1, 10):
		if i not in xs:
			return False
	return True

result = set()
for i in xrange(1, 1000):
	for j in xrange(1, 9999/i):
		xs =  separateDigits(i)
		xs += separateDigits(j)
		xs += separateDigits(i*j)
		if len(xs) == 9 and isPandigitial( xs ):
			result.add(i*j)

print sum(result)