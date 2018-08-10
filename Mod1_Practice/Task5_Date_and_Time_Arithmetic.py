#timedelta
# Write a program to find out how many minutes are in a 4-week period
# Hint: Use a timedelta object and the total_seconds() method
from datetime import timedelta

def minutes_in_weeks():
    w = timedelta(weeks = 4)
    
    print(w.total_seconds() // 60, "minute in a 4 weeks")    
minutes_in_weeks()



from datetime import date
#Date arithmetic
# [ ] Write a program to compute the number of days remaining in the current year
def remaining_days():
    current_date = date.today()
    current_year = current_date.year
    begin_of_year = date(year = current_year, month = 1, day = 1)
    r_days = current_date - begin_of_year
    print(r_days)
remaining_days()





#Comparing datetime objects
# [ ] Complete the program below to find out if July 4th is within 10 days of today's date,
# if it is, find out if has passed or not

from datetime import datetime

# get today's date
todays_date = datetime.today()

# 4th of July of current year
july_4th = datetime(month = 11, day = 4, year = todays_date.year)

days_difference = todays_date - july_4th

if(days_difference.days <= 10):
    print("not passed, ", days_difference)

else:
    print("passed")


