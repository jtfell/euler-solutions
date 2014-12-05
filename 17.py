cache = {}
cache[0] = 0
cache[1] = 3
cache[2] = 3
cache[3] = 5
cache[4] = 4
cache[5] = 4
cache[6] = 3
cache[7] = 5
cache[8] = 5
cache[9] = 4
cache[10] = 3
cache[11] = 6
cache[12] = 6
cache[13] = 8
cache[14] = 8
cache[15] = 7
cache[16] = 7
cache[17] = 9
cache[18] = 8
cache[19] = 8
cache[20] = 6
cache[30] = 6
cache[40] = 5
cache[50] = 5
cache[60] = 5
cache[70] = 7
cache[80] = 6
cache[90] = 6

HUNDRED = 7
THOUSAND = 8
AND = 3

def buildNum(n):
	if n < 20:
		return cache[n]
	if n < 100:
		return cache[n % 10] + cache[(n / 10) * 10]
	if n < 1000:
		temp = buildNum(n % 100)
		if temp:
			temp += AND
		return cache[n / 100] + HUNDRED + temp
	if n == 1000:
		return 3 + THOUSAND

count = 0
for x in xrange(1, 1001):
	count += buildNum(x)

print count


