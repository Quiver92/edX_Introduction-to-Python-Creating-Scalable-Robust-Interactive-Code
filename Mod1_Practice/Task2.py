#Mathematical operators
#Coin calculators
#In the following exercises, you will develop functions to count the number of coins in a certain dollar amount. You will then use these functions to write a program that can calculate the change due to a customer in coins.


##Quarters
# [ ] Complete the function `quarters_count` so it calculates and prints the number of quarters in `input_cents`
# The function input `input_cents` should be in cents 
# The function should print the number of calculated quarters in `input_cents`
# The function should return the number of remaining cents `remaining_cents` (which is less than 25, why?)
# HINT: You might want to use % and // operators

def quarters_count(input_cents):
    quarter = input_cents // 25
    return quarter

# test with $2
# Output should be: 8 quarter\s
dollars = 2
total_cents = dollars * 100
remaining_cents = quarters_count(total_cents)

# test with $5.30
# Output should be: 21.0 quarter\s
dollars = 5.30
total_cents = dollars * 100
remaining_cents = quarters_count(total_cents)

# test with $9.49
# Output should be: 37.0 quarter\s
dollars = 9.49
total_cents = dollars * 100
remaining_cents = quarters_count(total_cents)

##Dimes
# [ ] Complete the function `dimes_count` so it calculates and prints the number of dimes in `input_cents`
# The function input `input_cents` should be in cents
# The function should print the number of calculated dimes in `input_cents`
# The function should return the number of remaining cents `remaining_cents` (which is less than 10, why?)
# HINT: You might want to use % and // operators

def dimes_count(input_cents):
    dime = input_cents // 10
    return dime

# test with $2
# Output should be: 20 dime\s
dollars = 2
total_cents = dollars * 100
remaining_cents = dimes_count(total_cents)

# test with $5.30
# Output should be: 53.0 dime\s
dollars = 5.30
total_cents = dollars * 100
remaining_cents = dimes_count(total_cents)

# test with $9.49
# Output should be: 94.0 dime\s
dollars = 9.49
total_cents = dollars * 100
remaining_cents = dimes_count(total_cents)



#Nickels
# [ ] Complete the function `nickels_count` so it calculates and prints the number of nickels in `input_cents`
# The function input `input_cents` should be in cents 
# The function should print the number of calculated nickels in `input_cents`
# The function should return the number of remaining cents `remaining_cents` (which is less than 5, why?)
# HINT: You might want to use % and // operators

def nickels_count(input_cents):
    nickel = input_cents // 5
    return nickel

# test with $2
# Output should be: 40 nickel\s
dollars = 2
total_cents = dollars * 100
remaining_cents = nickels_count(total_cents)

# test with $5.30
# Output should be: 106.0 nickel\s
dollars = 5.30
total_cents = dollars * 100
remaining_cents = nickels_count(total_cents)

# test with $9.49
# Output should be: 189.0 nickel\s
dollars = 9.49
total_cents = dollars * 100
remaining_cents = nickels_count(total_cents)



#Change calculator
# [ ] Complete the function `coins_due` to calculate and print the change due to a customer in coins
#
# The function `coins_due` has 2 inputs:
#      - `amount_paid`: Amount paid by a customer (in cents)
#      - `item_price`: Purchase price of an item
#
# The function should print:
#      - The number of quarters due
#      - The number of dimes due
#      - The number of nickels due
#      - The number of cents due
#      
# The function does not need to return anything
#
# HINT: Use the functions you developed before `quarters_count`, `dimes_count`, `nickels_count`


#def quarters_count(input_cents):
    #TODO

#def dimes_count(input_cents):
    #TODO

#def nickels_count(input_cents):
    #TODO

def coins_due(amount_paid, item_price):
    print("Change due:")
    x = amount_paid - item_price #463
    quarter = quarters_count(x) #18
    print(quarter,'quarter')
    next_stage1 = quarter * 25.0 #450
    dime = dimes_count(x - next_stage1)#13
    print(dime,'dime') 
    next_stage2 = dime * 10.0
    nickel = nickels_count( x - next_stage1 + next_stage2) #3 #0
    print(nickel+'nickel')
    
    
# Test case:
# amount paid = $10, item price = $5.37
# Output should be: 
#    Change due:
#    18.0 quarter\s
#    1.0 dime\s
#    0.0 nickel\s
#    3.0 cent\s

amount_paid = 10 * 100 # in cents
item_price = 5.37 * 100 # in cents
coins_due(amount_paid, item_price)
