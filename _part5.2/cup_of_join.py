#====================
# 5.2 - Cup of join
#====================


#-------------------------------------------------
# join function:
# the function gets unlimited number of lists (each List as an argument).
# the function gets also a parameter called "sep".
# if sep is not provided, the default value is "-".
# between each list's elements there is a "sep".
# the function returns a string that contains all the elements of the lists.
#-------------------------------------------------
def join(*args, sep="-"):
    if len(args) == 0:
        return None
    result = []
    for arg in args:
        result.extend(arg) # result = result + arg
        result.append(sep) # result = result + [sep]
    result.pop() # remove the last element - the last sep
    return result
    

#----------------
# Main function
#----------------
def main():

    print ("join([1, 2], [8], [9, 5, 6], sep='@'):")
    print (join([1, 2], [8], [9, 5, 6], sep='@'))
    print("=====================================" + '\n')

    print ("join([1, 2], [8], [9, 5, 6]) :")
    print (join([1, 2], [8], [9, 5, 6]))
    print("=====================================" + '\n')

    print ("join([1]) :")
    print(join([1]))
    print("=====================================" + '\n')

    print ("join() :")
    print(join())


if __name__ == "__main__":
    main()