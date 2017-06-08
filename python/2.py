
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
result = 0
i = 1
while 1:
    term = fib(i)
    if term > 4000000:
        break
    if term % 2 == 0:
        result += term
    i += 1
    
print result