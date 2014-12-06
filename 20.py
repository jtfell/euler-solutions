def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)

value = str(fact(100))
count = 0
for digit in value:
	count += int(digit)

print count