def binary(integer):
    bit_string = bin(integer)
    final = bit_string.lstrip('-0b')
    return(final)

while flips % 1 != 0 and flips < 1:
    print("")
    flips = input(print("How many times will the coin be flipped. Please enter an integer. "))
    flips = float(flips)
flips = int(flips)

total_events = 2 ** flips

for i in range (0, total_events):
    flip_pos = binary(i)
    flip_pos = flip_pos.split()

def bin_list(x):
    list_1 = [0]
    list_length = 1
    for i in range (0, x):