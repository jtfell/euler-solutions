def calcNameScore(name):
	count = 0
	for letter in name:
		count += ord(letter) - 64
	return count

f = open("22.txt", "r")

rawNames = f.read().lstrip("\"").rstrip("\"")
names = rawNames.split("\",\"")
names.sort()

count = 0
index = 1
for name in names:
	count += calcNameScore(name) * index
	index += 1

print count