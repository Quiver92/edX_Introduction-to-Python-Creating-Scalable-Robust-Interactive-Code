#Combining Comparisons
# [ ] Write an expression to test if x is an even number outside the range [-100, 100]

# Test your expression with:
# x = 104 (True)
# x = 115 (False)
# x = -106 (True)
# x = -99 (False)

x = 104
print((x > -100) or( x < 100) and ( x % 2 != 0))
x = 115
print((x > -100) and ( x < 100) and ( x % 2 != 0))
x = -106
print((x > -100) or ( x < 100) or ( x % 2 != 0))
x = -99
print((x > -100) and ( x < 100) or ( x % 2 != 0))



# [ ] Write an expression to test if a string s starts and ends with a capital letter
# HINT: You might find the function `str.isupper()` useful

# Test your expression with
# s = "CapitaL" (True)
# s = "Not Capital" (False)
def isup(s):
 print(str.isupper(s[::len(s)-1]))

s = "CapitaL"
isup(s)

s = "Not Capital"
isup(s)




# [ ] Write an expression to test if a string s contains a numerical value
# then test if the value is greater than the value stored in x
# HINT: Use the functions `s.isnumeric()` and `float(s)`
def numeric(s,x):
   if s.isnumeric() == True:
       print(float(s) > x, "Correct")

   else:
      print(False, "Not Correct")
# Test your expression with
s = "39"
x = 24
numeric(s,x)
# Expression should yield True

s = "a39"
x = 24
numeric(s,x)
# Expression should yield False






