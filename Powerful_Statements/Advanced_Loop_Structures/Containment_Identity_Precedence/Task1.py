#Containment (in, not in)
#Number containment
# [ ] Write a program to prompt the user for an integer input between 0 and 100
# then print if the number is contained in `lst`
def listed_item():
    lst = [22, 89, 69, 78, 58, 22, 56, 13, 74, 8, 32, 58, 8, 63, 46, 79, 9, 38, 25, 96]
    while True:
        inp = int(input("Please input integer beetween 0 and 100: "))
        if ((inp < 0) and (inp > 100)):
            print("Out of range")
        else:
            if inp in lst:
                print("In list:", inp)
            elif inp not in lst:
                print("Not in list")
                break
           


#List containment
# [ ] The `records` list contains information about a company's employees
# each of the elements in `records` is a list containing the name and ID of an employee.
# Write a program to test if `applicant` is contained in `records` and display an appropriate message

# Records of names and IDs
#records = [['Colette', 22347], ['Skye', 35803], ['Alton', 45825], ['Jin', 24213]]

#applicant = ['Joana', 20294]







#String containment
# [ ] Write a program to prompt the user for a letter (capital or small) then print if the number is a vowel
# HINT: Use a string containing all the vowels and the `in` or `not in` operator
def letter():
    vow_small = ['a', 'i', 'e', 'u']
    let = input("Please input the letter: ")
    if (let in vow_small):
        print('ok small')
    elif (let in vow_upper.upper() for vow_upper in vow_small ):
        print('ok upp')
    else:
        print(";(")
letter()








