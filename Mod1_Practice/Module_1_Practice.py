#-Directory creator
# [ ] The following program is designed to generate a number of directories.
# The directory names follow the pattern (MM_DD_YY_randnum), where:
#     - MM_DD_YY: is today's date as month/day/year
#     - randnum: is a random integer between 10000 and 50000
# For example, if today is May 12th, 2016, then the following would be valid names: 05_12_16_11050 or 05_12_16_15001
#
# For this task, you should complete the functions:
# 1) `directory_count()`
# 2) `name_generator()`
# 3) `directory_creator(name)`
# 4) `create()`
#
# HINT: You should import all necessary modules
from datetime import datetime
import os
import math

def directory_count():
    """
    Calculate the number of directories to be generated.
    
    I) Get the current minute using appropriate functionality from `datetime`
    II) Take the square root of ..the current minute + 15
    III) Round the square root to an integer
    VI) return the rounded number as the number of directories to be created
    
    args: 
          NONE
    
    returns: 
         `dir_count`: number of directories to be created 
    """
    minute = datetime.today().minute
    count = int(math.sqrt(minute) + 15)
    return(count)

def name_generator():
    """
    Generate a single directory name using the pattern (MM_DD_YY_randnum).
    
    args:
         NONE
    
    returns:
         `dir_name`: string containing a valid directory name
    """
    #TODO

def directory_creator(name):
    """
    Create a single directory called `name` in the current working directory.
    
    args:
         name: directory to be created
    
    returns:
         NONE
    """
    #TODO

def create():
    """
    Generate the necessary directories.
    
    Use `directory_count` to calculate the number of directories, then use `directory_creator` and `name_generator`.

    args:
         NONE
    
    returns:
         NONE
    """
    #TODO
