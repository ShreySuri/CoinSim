def bin_list(x):
    list_1 = [0]
    list_length = 1
    val_count = 1
    
    for i in range (0, x):

        j = i

        while j > 1:
            j = j/2

        if j == 1 and i != i:
            list_1.append(0)
            val_count = val_count + 1
        else:
            toggle = True

        list_1[0] = list_1[0] + 1
        for i in range (0, val_count):
            if list_1[i] == 2:
                list_1[i] = 0
                x = i + 1
                list_1[x] == list_1[x] + 1

        return(list_1)

while flips % 1 != 0 and flips < 1:
    print("")
    flips = input(print("How many times will the coin be flipped. Please enter an integer. "))
    flips = float(flips)
flips = int(flips)

total_events = 2 ** flips

print(binary(flips))
print(binary(total_events))
