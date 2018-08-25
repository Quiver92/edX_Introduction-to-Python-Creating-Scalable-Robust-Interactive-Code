#Loops Containing Compound Conditional Expressions
#Counting specific numbers
# [ ] Complete the following program to count the number of even positive numbers, odd negative numbers, and zeros in `lst`

lst = [9, 0, -2, -4, -5, 2, -15, 6, -65, -7]

even_positives = 0
odd_negatives = 0
zeros = 0

for num in lst:
    if((num % 2 == 0) and (num > 0)):
        even_positives = even_positives + 1
    elif((num %2 != 0) and (num < 0)):
        odd_negatives = odd_negatives + 1
    elif(num == 0):
        zeros = zeros + 1
            
print("Number of even positives:", even_positives)
print("Number of odd negatives:", odd_negatives)
print("Number of zeros:", zeros)





#Counting characters
# [ ] Write a program to count the number of punctuation marks (. , ? ! ' " : ;) in `s`

s = "Once you eliminate the impossible, whatever remains, no matter how improbable, must be the truth." # Sherlock Holmes (by Sir Arthur Conan Doyle, 1859-1930)
period_count = 0
comma_count = 0
semicolon_count = 0
colon_count = 0
exclamation_count = 0
question_count = 0
total = 0


for i in s:
    if (i == '.'):
        period_count += 1
        total += 1
    if (i == ','):
        comma_count += 1
        total += 1
print(comma_count)
#etc



#User input
# [ ] Write a program to prompt the user for an odd positive number; use an infinite  loop and a `break` statement.
while True:
    num = int(input("Please input odd number: "))
    if(num % 2 != 0):
        break

