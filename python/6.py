sum = 0
for i in xrange(1, 101):
    sum += i**2
result = 0
for i in xrange(1, 101):
    result += i

print result**2 - sum
