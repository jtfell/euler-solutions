# must be less than 500

# a^2 + b^2 = c^2 and a + b + c = 1000

for i in xrange(1, 500):
    for j in xrange(i + 1, 500):
        value = ((i**2 + j**2)**0.5 + i + j)
        if value == 1000:
            print i * j * (i**2 + j**2)