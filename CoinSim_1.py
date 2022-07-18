
flips = 0

def mid(x)
	if x % 2 == 0:
		y = int(x / 2)
	elif x % 2 == 1:
		y = int((x + 1) / 2)
	else:
		y = False

	return(y)



while flips % 1 != 0 and flips < 1:
	print("")
	flips = input(print("How many times will the coun be flipped. Please enter an integer. "))
	flips = float(flips)
flips = int(flips)

total_events = 2 ** flips

