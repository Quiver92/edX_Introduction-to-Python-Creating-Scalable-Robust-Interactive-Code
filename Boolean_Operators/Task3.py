#Boolean Expressions Equality
# [ ] Write an expression equivalent to the one below 
# to test if x is outside the range [10, 20] (seen in a previous example)

# (x < 10) or (x > 20)

# Test your expression with 
x = 11
print(x < 10) or (x > 20)
x = 50
print(x < 10) or (x > 20)



# [ ] Write a second expression to test if x is an even number outside the range [-100, 100]
# Do NOT use the expression you wrote for a previous exercise

# Test your expression with:
def express(x):
    y = (x < -100) or (x > 100) and (x % 2 == 0)
    print(y)
x = 104
express(x)
x = 115
express(x)
x = -106
express(x)
x = -99 
express(x)

