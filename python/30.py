from common import *

result = 0
for i in xrange(50, 6 * 9**5):
	if i == sum([x**5 for x in separateDigits(i)]):
		result += i

print result