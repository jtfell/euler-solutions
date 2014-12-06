# day 6 starting from monday
SUNDAY = 6 

months = {1: 31, 2: -1, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# starting on a tuesday
day = 1
sundays = 0

# Determine if its a leap year
def isLeapYear(year):
	if year % 100 == 0:
		if year % 400 == 0:
			return True
		else:
			return False
	elif year % 4:
		return False
	else:
		return True


for year in xrange(1901, 2001):
	for month in months:

		daysInMonth = months[month]
		if daysInMonth == -1:
			if isLeapYear(year):
				daysInMonth = 29
			else:
				daysInMonth = 28

		for i in xrange(1, daysInMonth+1):
			
			if day == SUNDAY and i == 1:
				sundays += 1

			day = (day + 1) % 7

			



print sundays
