def bin_list(x):
    list_1 = [0]
    power = 1
    while 2 ** power <= x:
        power = power + 1
        list_1.append(0)

    val_count = power
    for i in range (0, x):
        list_1[0] = list_1[0] + 1

        for j in range (0, val_count):
            if list_1[j] == 2:
                list_1[j] = 0
                k = j + 1
                list_1[k] = list_1[k] + 1
            else:
                toggle = True

    list_1.reverse()
    return(list_1)


flips = 0
while flips % 1 != 0 or flips < 1:
    print("")
    flips = input(print("How many times will the coin be flipped? Please enter an integer. "))
    flips = float(flips)
flips = int(flips)

total_events = 2 ** flips

print(bin_list(flips))
print(bin_list(total_events))
