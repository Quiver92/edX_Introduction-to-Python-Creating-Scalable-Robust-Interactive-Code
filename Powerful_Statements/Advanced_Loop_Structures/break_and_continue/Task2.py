#Sum of rows
import math
# [ ] Write a program to display the sum of each row in table
table = [[5, 2, 6], [4, 6, 0], [9, 1, 8], [7, 3, 8]]
for row in table:
    print(sum(row))






#Character art
# [ ] Complete the function `generate_star` so it displays a star of variable `size` using "*"
# For size = 5 the star should look like:
# *   *
#  * *
#   *
#  * *
# *   *

def generate_star(size):
    for star in range(size):
        for col in range(size):
            print(star,col)
            if (col == star) or ((size - col -1) == star):
                print("*",  end='')
            else:
                print(' ', end = '')
        print()

    pass
# Display star
generate_star(5)

