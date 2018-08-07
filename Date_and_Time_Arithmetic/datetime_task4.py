from datetime import datetime, date, time
# [ ] Write a program that displays the time: (17:39:10) as:
# 1) 05:39:10 PM
# 2) 17:39:10

def path_one():
    t = time(17, 39, 10)
    tform_one = t.strftime("%I:%M:%S %p") 
    print tform_one
    print t
path_one()

# [ ] Write a program that displays the date: (October 23rd 2018) as:
# 1) Oct 23, 2018
# 2) 10/23/18
# 3) 23/October/2018
# 4) Tuesday October 23

def path_two():
    d = date(2018, 10 ,23)
    dform_one = d.strftime("%b %d, %Y")
    dform_two = d.strftime("%m/%d/%y")
    dform_three = d.strftime("%d/%B/%Y")
    dform_four = d.strftime("%A %B %d")

    print dform_one
    print dform_two
    print dform_three
    print dform_four
path_two()

# [ ] Complete the function `weekday` to return the weekday name of `some_date`
# Use the function to find the weekday on which you were born

def weekday(some_date): 
    a = some_date.strftime("%A")  
    return a

# Modify to your birthdate
bd = date(day = 17, month = 11, year = 1992)

# Display the day on which you were born
day = weekday(bd)
print(day)
