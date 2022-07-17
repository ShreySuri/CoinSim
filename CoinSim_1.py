
flips = 0

while flips % 1 != 0 and flips < 1:
	print("")
	flips = input(print("How many times will the coun be flipped. Please enter an integer. "))
	flips = float(flips)
flips = int(flips)

total_events = 2 ** flips

head_count = 0

for  i in range (0, flips):
	head_count = head_count + 1
	opposite = flips - head_count