#======================
# כלים שלובים - 5.4
#======================
import itertools

#----------------------------------------------------------
# interleave Function:
# this function gets one or meore iterable parameters.
# The Function returns a list of the elements of the iterables.
#__________________________________________________________
# I assume that all the iterables have the same length, 
# but if the imput iterables have different length, the function will ignore the extra elements.
#----------------------------------------------------------
def interleave(*iterables):
    # len of shortest iterable
    minLen = min(len(iterable) for iterable in iterables)
    # Iterate over each index from 0 to min_len-1
    for i in range(minLen):
        # Iterate over each iterable and yield the i-th element
        for iterable in iterables:
            yield iterable[i]


#----------------
# Main function
#----------------
def main():
    # Create an iterator that returns the elements of the iterables
    interleaveIterator = interleave('abc', [1, 2, 3], ('!', '@', '#'))

    # Print the elements of the iterator
    for element in interleaveIterator:
        print(element, end=" ")


if __name__ == "__main__":
    main()



