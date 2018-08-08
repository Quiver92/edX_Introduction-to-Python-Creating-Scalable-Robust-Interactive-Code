# [ ] Create a `timedelta` object that contains: 2 hours, 3 minutes, and 1 week
from datetime import datetime, timedelta, time, date
delta1 = timedelta( hours = 2, minutes = 3, weeks = 1)
print(delta1)

# [ ] Use a `timedelta` object to calculate the total number of seconds in: 1 hour and 15 minutes
delta2 = timedelta( hours = 1, minutes = 15)
d = delta2.seconds
print(d)

# Use a `timedelta` object to find out how many days are left until your upcoming birthday
today = datetime.today()
my_birthday = datetime( year = today.year, month = 11, day = 17)
delta3 = my_birthday - today
print(delta3.days,"Days until my Birthday come  ")
