n = 600851475143
factors = []
i = 2
while n > 1:
    while n % i == 0:
        factors.append(i)
        n /= i
    i = i + 1
print max(factors)     