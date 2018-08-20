# Generate a staircase character art
# Size controls the number of steps
def char_art(steps):
    for row in range(steps):
        for col in range(steps):
            if(col <= row):
                print("[]", end = "")
        print()

# Generate a staircase with 6 steps                
char_art(6)
