#Compound Conditionals
# [ ] Write a program to validate that user input is outside the range [0, 100]
def user_input():
   x = int(input("Input your favorite number: "))
   return(x)
x = user_input()
if ((x >= 0) or (x <= 100)):
   print "Your favorite number is ok"
else:
   print "Out of the range"




#BMI category
#The Body Mass Index (BMI) measures the body fat using the weight and height of a person. The BMI is used to classify adults into categories as in the following table.
# [ ] Write a program to ask a user for her/his BMI index, then display the user's BMI category
#Underweight < 18.5
#Normal Weight	18.5 - 24.9
#Overweight	25 - 29.9
#Obese	≥ 30
