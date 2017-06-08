from common import *

factorials = {}
factorials[0] = 1

for i in xrange( 1, 10 ):
	factorials[i] = fact(i)

result = 0
for i in xrange(3, 2540161 ):
	x = sum( [factorials[n] for n in separateDigits(i)] )
	if x == i:
		result += i

print result