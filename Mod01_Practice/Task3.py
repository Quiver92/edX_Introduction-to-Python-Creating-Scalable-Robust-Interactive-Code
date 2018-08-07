#Random numbers
#Probability of a die roll
#It is possible to mathematically predict the probability (or chance) of getting a certain die roll; however, in this exercise you will use Python to do it without math. The trick is to roll a die a large number of times and count how many times we get a certain roll. You can, then, divide the count by the large number to get the probability. For a fair 6-sided die, the chance of getting any of its faces is about 16.6%

# [ ] Complete the following program to display the probability of a certain die roll

from random import randint

def die_roller ():
    return(randint(1, 6))

#TODO

