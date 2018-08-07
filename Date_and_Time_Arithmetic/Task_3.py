# [ ] Write a program to find out if 4th of July of this year has passed or not

from datetime import date
today = date.today()
today_format = today.strftime("%d-%b-%Y")
print(today_format)
dt = date(year = today.year, month = 7, day = 4)
dt_format = dt.strftime("%d-%b-%Y")
print(dt_format)
if (today >= dt):
    print("pased")
else:
    print("wait")

