triangle = []
paths = []
# Construct a list of lists: [[75],  [95, 64], ...]
for line in open("18.txt", "r"):
	triangle.append(line.split(" "))
	paths.append(line.split(" "))

lineNum = 0
for line in triangle:
	valNum = 0
	for val in line:

		if lineNum == 0 or valNum == 0:
			leftPath = 0
		else:
			leftPath = paths[lineNum-1][valNum-1]

		if lineNum == 0 or valNum >= lineNum:
			rightPath = 0
		else:
			rightPath = paths[lineNum-1][valNum]

		paths[lineNum][valNum] = max(rightPath, leftPath) + int(triangle[lineNum][valNum])

		valNum += 1
	lineNum += 1

print max(paths[-1])
