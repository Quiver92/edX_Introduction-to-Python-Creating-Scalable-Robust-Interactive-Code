import os.path
# [ ] Write a program that prompts the user for a file or directory name 
# then prints a message verifying if it exists in the current working directory
dir_name = input("Please provide a file or directory name: ")
if(os.path.exists(dir_name)):
    print("Path exists")
    # Test to see if it's a file or directory
    if(os.path.isfile(dir_name)):
       print("It's a file")
    elif (os.path.isdir(dir_name)):
       print("It's a dir")
else:
    print("Path doesn't exist")

# [ ] Write a program to print the absolute path of all directories in "parent_dir"
# HINTS:
# 1) Verify you are inside "parent_dir" using os.getcwd()
# 2) Use os.listdir() to get a list of files and directories in "parent_dir"
# 3) Iterate over the elements of the list and print the absolute paths of all the directories
dir_list = os.listdir()
print(dir_list)
for i in dir_list:
    print(os.path.abspath(i))
