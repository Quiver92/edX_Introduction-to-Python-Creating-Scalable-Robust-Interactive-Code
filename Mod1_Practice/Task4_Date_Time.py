#Working with date and time
#Current date and time
# [ ] Write a program that displays the current time as (HH:MM AM/PM) (example 02:28 PM)
from datetime import date
import time
d = date.today()
print(d)
print(time.strftime("%I:%M%p"))

# [ ] Write a program that displays the current time as (HH:MM:SS) (example 14:28:10)
print(time.strftime("%H:%M:%S"))

# [ ] Write a program that displays the current date as (Friday, December 15, 2017)
print(d.strftime("%A, %B %d, %Y "))










#American VS European date format
#In the United States, the date is formatted as Month/Day/Year; whereas, in Europe the date is formatted as Day/Month/Year. In this exercise, you will write two functions that will display a datetime object in the American or European format.

# [ ] Complete the functions `american_format(d)` and `european_format(d)` to display the datetime object d in the proper format

from datetime import datetime

def american_format(d):
    return(d.strftime("%m/%d/%Y"))

def european_format(d):
    return(d.strftime("%d/%m/%Y"))

# test
d = datetime(month = 2, year = 2012, day = 13)

print("American format:", american_format(d))
print("European format:", european_format(d))











#Birthday days
# [ ] Write a program to display a list of all your birthdays from the day you were born till 2025.
# You should also show the weekdays so you can see which of them was (or will be) on a weekend
def bithday():
    for i in range(1992, 2026):
        every_year = datetime(year = i, month = 3, day = 20)
        format_year = every_year.strftime("%Y-%A-%m")
        print(format_year)
bithday()






