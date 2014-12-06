numbers = open("13.txt", "r").read().split("\n")

count = 0
for number in numbers:
	count += int(number)

print count / (10**42)