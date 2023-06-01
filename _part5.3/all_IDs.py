#========================
# פיצוץ אוכלוסין - 5.3
#========================

NUM_OF_IDS_TO_GENERATE = 10

#-------------------------------------------------------------------------------
# get full ID number Function:
# gets 8 digits of an Israeli ID number and return the full ID number.
# the function calculate the 9th digit and return the full ID number (9 digits).
# steps:
# 1. iterate over the digits from left to right
# 2. for each digit: multiply it by 1 or 2 (1 for even index, 2 for odd index).
# 3. in case of the multiplication is bigger than 9, connect the two digits.
# 4. sum all.
# 5. the 9th digit is the difference between the sum and the next multiple of 10.
# return the full ID number.
#-------------------------------------------------------------------------------
def get_full_id(id_number):
    id_number = str(id_number) # validate that the input is a string
    sum_digits = 0
    for index, digit in enumerate(id_number): 
        if index % 2 == 0:
            sum_digits += int(digit)
        else:
            sum_digits += int(digit) * 2
    last_digit = 10 - sum_digits % 10 -1
    return id_number + str(last_digit) 

#----------------------------------------------------
# generator for collection all israeli ID numbers
#----------------------------------------------------
def israeli_id_numbers():
    id_number = 11111111 # asume that the first ID number is 11111111
    while True:
        yield get_full_id(id_number)
        id_number += 1


#----------------
# Main function
#----------------
def main():
    israeli_id_numbers_iterator = israeli_id_numbers()
    for i in range(NUM_OF_IDS_TO_GENERATE): # generate 10 ID numbers
        print(next(israeli_id_numbers_iterator))

if __name__ == "__main__":
    main()
