
def is_palindrome(n):
    digits = [int(i) for i in str(n)]
    for i in xrange(len(digits)):
        if not digits[-i] == digits[i-1]:
            return False
    return True

max = 0
for i in xrange(99, 999):
    for j in xrange(i + 1, 999):
        if i*j > max and is_palindrome(i*j):
            max = i*j
print max
