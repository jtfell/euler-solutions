from common import *

value = str(fact(100))
count = 0
for digit in value:
	count += int(digit)

print count