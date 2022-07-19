def bin_list(x, y):
    list_1 = []
    power = 1
    val_count = 0
    for i in range (0, y):
        list_1.append(0)
        power = power * 2
        val_count = val_count + 1

    if x < power:
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
    
    else:
        return(False)


flips = 0
while flips % 1 != 0 or flips < 1:
    print("")
    flips = input(print("How many times will the coin be flipped? Please enter an integer. "))
    flips = float(flips)
flips = int(flips)

total_events = 2 ** flips

for i in range (0, total_events):
    bin_list_1 = bin_list(i, flips)
    total = 0
    
    for j in range (0, flips):
        total = total + bin_list_1[i]

    if total == target:
        counter = counter + 1
    else:
        counter = counter + 0

    fraction = counter/total_events
    print("%s -- %s/%s -- %s" % (target, counter, total_events, fraction))


