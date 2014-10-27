fibprevious = 1
fibcurrent = 1

evensum = 0

while fibcurrent <= 4000000:
	#print fibcurrent

	if (fibcurrent % 2 == 0):
		evensum += fibcurrent

	fibnew = fibcurrent + fibprevious
	fibprevious = fibcurrent
	fibcurrent = fibnew

print evensum
