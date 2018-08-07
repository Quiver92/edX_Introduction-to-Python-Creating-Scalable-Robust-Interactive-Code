# [ ] Write a program to compute the date 3 weeks before your birthday 
# to help you remember when to send the invitations
from datetime import datetime, timedelta
today = datetime.today()
my_birthday = datetime(today.year, 11, 17)
three_weeks_ago = timedelta(weeks = 3)
three_weeks_before_my_birhtday = my_birthday - three_weeks_ago
print(three_weeks_before_my_birhtday.strftime("%b/%d/%Y"))


# [ ] Write a program that computes the number of days from the current date till the 3 weeks reminder
# 1) Create a `timedelta` object (td1) for the period between the current date and your upcoming birthday
# 2) Create a `timedelta` object (td2) containing 3 weeks
# 3) Use the `timedelta` objects (td) from 1 and 2 to compute the required number of days
td0 = today - three_weeks_ago
print(td0.total_seconds())

