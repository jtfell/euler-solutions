SIZE = 1001

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

# Init spiral
spiral = [0] * SIZE
for i in xrange(SIZE):
	spiral[i] = [0] * SIZE

x = SIZE/2
y = SIZE/2
direction = RIGHT
lengthOfMovement = 1
lengthMoved = 0

# Put in values
for i in xrange(1, SIZE**2+1):
	spiral[y][x] = i

	if direction == LEFT:
		x -= 1
	elif direction == RIGHT:
		x += 1
	elif direction == UP:
		y -= 1
	elif direction == DOWN:
		y += 1

	lengthMoved += 1
	if lengthMoved == lengthOfMovement:
		direction = (direction + 1) % 4
		if (direction + 1) % 2 :
			lengthOfMovement += 1
		lengthMoved = 0

# Count diagonals
result = 0
x = 0
y = 0
for i in xrange(0, SIZE):
	result += spiral[y][x]
	result += spiral[y][SIZE-x-1]
	x += 1
	y += 1

result -= 1 # Counts middle element twice

print result