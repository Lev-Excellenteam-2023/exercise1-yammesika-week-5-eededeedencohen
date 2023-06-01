#===========================
# מנה מושלמת לחלוקה - 5.3
#===========================


#---------------------------------------
# get_dividers Function with generator
#---------------------------------------
def get_dividers(number):
    for divider in range(1, number):
        if number % divider == 0:
            yield divider


#---------------------------------------------------------------------
# After a small research I found that the perfect number is a number that
# the binary representation of it is must be ones in the left and zeros in the right
# and the amount of one is one more than the amount of zeros.
# example: 6 = 110 in binary, 28 = 11100 in binary, 496 = 111110000 in binary
# but, not all the numbers that fit this condition are perfect numbers 
# for example 1111000 = 120 and is not a perfect number.
#---------------------------------------------------------------------

#--------------------------------------------------------
# helper function: 
# add bit of 1 to the left of the binary representation of the number
#--------------------------------------------------------
def add_one_from_left(n):
    # Convert the number to a binary string and remove the "0b" prefix
    bits = bin(n)[2:]

    # Add a "1" to the left of the binary string
    bits = "1" + bits

    # Convert the new binary string to an integer and return it
    return int(bits, 2) 

#--------------------------------------------------------
# helper function:
# add bit of 0 to the right of the binary representation of the number
#--------------------------------------------------------
def add_zero_on_right(n):
    # Shift the number left by 1 and bitwise OR it with 1
    result = add_one_from_left(n)
    result = (n << 1) 
    return result

#--------------------------------------------
# function that add 1 in left and 0 in right
#--------------------------------------------
def add_one_from_left_and_zero_on_right(n):
    n = add_one_from_left(n)
    n = add_zero_on_right(n)
    return n


#-------------------------------------------------------------------------------
# perfect_serving with generator to collect unlimited number of perfect servings
#-------------------------------------------------------------------------------
def perfect_serving():
    current_number = 6 # 110 in binary
    while True:
        dividers = get_dividers(current_number)
        # sum all the dividers
        sum_dividers = 0
        for divider in dividers:
            sum_dividers += divider
        if sum_dividers == current_number:
            yield current_number
        current_number = add_one_from_left_and_zero_on_right(current_number)


#----------------
# Main function
#----------------
def main():
    perfect_serving_iterator = perfect_serving()
    for i in range(5): # generate 10 perfect servings
        print(next(perfect_serving_iterator))

if __name__ == "__main__":
    main()