#Path operations
# [ ] Write a program that prompts the user for a file or directory name
# if it exists in the current working directory, it prints whether it is a file or directory
import os, os.path


def file_prompt():
    f_name = input("Type name of the file or directory: ")
    
    l = os.listdir()
    if f_name in l:
        print("File/Directory i Exists")
file_prompt()

