#=======================
# אין לי וִנִגְרֶט - 5.1
#=======================

from datetime import datetime
import random

#----------------------------------------------------
# A function of software that get two dates YYYY-MM-DD.
# The software return a random date between the two dates.
# _________________________________
# strptime - convert string to date
#----------------------------------------------------
def random_date(start_date, end_date):

    # convert start_date and end_date from string to date
    start_date = datetime.strptime(start_date, '%Y-%m-%d') 
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # error if the start_date is after the end_date:
    if start_date > end_date:
        raise ValueError('start_date must be before end_date')

    # get random date between start_date and end_date
    random_date = start_date + (end_date - start_date) * random.random()

    return random_date.strftime('%Y-%m-%d')


#----------------
# Main function
#----------------
def main():
    print(random_date('2023-01-01', '2023-12-31'))

if __name__ == "__main__":
    main()
