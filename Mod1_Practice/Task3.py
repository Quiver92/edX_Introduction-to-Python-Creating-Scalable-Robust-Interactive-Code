#Random numbers
#Probability of a die roll
#It is possible to mathematically predict the probability (or chance) of getting a certain die roll; however, in this exercise you will use Python to do it without math. The trick is to roll a die a large number of times and count how many times we get a certain roll. You can, then, divide the count by the large number to get the probability. For a fair 6-sided die, the chance of getting any of its faces is about 16.6%

# [ ] Complete the following program to display the probability of a certain die roll

from random import randint
from collections import Counter
def die_roller ():
    return(randint(1, 6))
die_arr = []

K = int(input("Drop Times: "))
while( K > 0 ):
    K = K-1
    die_arr.append(die_roller())

c = Counter(die_arr)
for i in c:
    print(i, c[i] / len(die_arr) * 100.0)





#Pick a candy
#In this exercise, you will write a program to randomly select a candy from a box.

# [ ] Complete the function `pick_candy` so it returns a candy from box at random

def pick_candy():
    box = ["Taffy", "Brownie", "Cookie", "Candy bar", "Chocolate", "Lollipop", "Gingerbread", "Marshmallow"]
    #TODO

print(pick_candy())

