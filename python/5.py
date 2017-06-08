def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_seq(seq):
    return reduce(lcm, seq)

print lcm_seq(xrange(1, 20))