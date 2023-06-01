#====================
# כפלו לי שתו לי 
#====================

#-------------------------------------------------
# avg function 
# the function gets unlimited number of arguments.
# the function returns the average of the arguments. 
#-------------------------------------------------
def avg(*args):
    if len(args) == 0: # if there are no arguments
        return None
    return sum(args) / len(args)


#print(avg(5, 6))
#print(avg(10, 5, 3))
#print(avg(2))
#print(avg())

#----------------
# Main function
#----------------
def main():

    print ("avg(5, 6) :")
    print (avg(5, 6))
    print("=====================================" + '\n')

    print ("avg(10, 5, 3) :")
    print (avg(10, 5, 3))
    print("=====================================" + '\n')

    print ("avg(2) :")
    print (avg(2))
    print("=====================================" + '\n')

    print ("avg() :")
    print (avg())

if __name__ == "__main__":
    main()