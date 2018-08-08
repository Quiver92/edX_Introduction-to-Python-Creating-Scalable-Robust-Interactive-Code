#timedelta
# Write a program to find out how many minutes are in a 4-week period
# Hint: Use a timedelta object and the total_seconds() method
from datetime import timedelta

def minutes_in_weeks():
    w = timedelta(weeks = 4)
    
    print(w.total_seconds() // 10080)    
minutes_in_weeks()
