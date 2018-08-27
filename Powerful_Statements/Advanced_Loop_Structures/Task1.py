#Changing Loop Iterations
#Prime numbers
#A prime number is a number greater than 1 that is divisible only by 1 and itself. Prime numbers play an important role in several cryptographic algorithms that we use every day, and it is very useful to build a program to test whether a number is prime.

# [ ] The following program tests if `num` is prime or not, use a `break` statement to improve its efficiency
# and reduce the number of necessary iterations

# Compare the number of necessary iterations with and without the `break` statement
# Use the following numbers for the comparison: 

num = 45345
#num = 11579
#num = 948240
#num = 128093
#num = 519937
#num = 694394

prime = True # assume num is prime unless proven otherwise

iteration_count = 0

for i in range(2, num):
    if num % i == 0:
        prime = False;
        break
    iteration_count = iteration_count + 1
# Display results
if prime:
    print(num, "is prime")
else:
    print(num, "is NOT prime")

print("Total number of iterations:", iteration_count)





#User input
# [ ] Write a program to prompt the user for an odd number; use an infinite loop and a `break` statement.


while True:
   num = input("Please input odd number: ")
   if ( num % 2 == 0 ):
      print("Odd")
   else:
      break





# [ ] Modify the following program to display numbers that are divisible by 7 along with their square roots.
# HINT: Use a `continue` statement in the loop

from math import sqrt

for num in range(1, 100):
    if ( num % 7 != 0 ) and ( sqrt(num) % 7 != 0 ):
       continue
    print(num)
        
