from datetime import datetime, timedelta
# [ ] Complete the following program to find out if you are closer to the current year's June or December solstice

# Define today's date
now = datetime.today()

# Define the December solstice
december_solstice = datetime(month = 12, day = 21, year = now.year)

# Define the June solstice
june_solstice = datetime(month = 6, day = 21, year = now.year)

count_dec = now - december_solstice
print(count_dec)
count_jun = now - june_solstice
print(count_jun)
if ( count_dec > count_jun):
    print("December is closer")
else:
    print("June is closer")

# Find out which solstice is closer
