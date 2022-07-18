
def binary(integer):
    bit_string = bin(integer)
    final = bit_string.lstrip('-0b')
    return(final)

