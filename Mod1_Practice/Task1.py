# [ ] Use the math module to display an accurate value for pi
from math import pi
print(pi)


# [ ] Write a program to:
# 1) find all the numbers in a list that are divisible by 3
# 2) display the square root of these numbers
# 3) use a rounding function to display the square roots while ignoring the decimal fraction

lst = [23, 45, 65, 2345, 42, 76, 37, 87, 647, 35, 37 ,39, 898, 92, 18]

def divis(n):
    return (n % 3) == 0
for i in lst:
    if divis(i == True):
        print("Divisible by 3:", i)
