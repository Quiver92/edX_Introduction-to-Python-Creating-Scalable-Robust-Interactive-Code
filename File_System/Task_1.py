import os
import sys
#print("Current working directory is: ", os.getcwd())
#os.chdir("../..")
#print("Current working directory is: ", os.getcwd())
#print(os.listdir())
#os.mkdir("test")
#print(os.listdir())
#os.rmdir("test")
#print(os.listdir())


# [ ] Write a program to:
# 1) Prompt the user for a directory name
# 2) Create the directory
# 3) Verify the directory was created by listing the content of the current working directory
# 4) Remove the created directory
# 5) Verify the directory was removed by listing the content of the current working directory

dir_name =  input("Please provide a new directory name: ")
dir_name
os.mkdir(dir_name)
print(os.listdir())
os.rmdir(dir_name)
print(os.listdir())


# [ ] Write a program to:
# 1) Create a directory called "my_dir"
# 2) Change the current working directory to "my_dir"
# 3) Verify you are in the correct directory by displaying the current working directory
# 4) Change the working directory back to the parent directory
# 5) Verify you are in the correct directory by displaying the current working directory
# 6) Rename "my_dir" to "your_dir"
# 7) Verify the directory was renamed by listing the content of the current working directory
# 8) Remove "your_dir"
# 9) Verify the directory was removed by listing the content of the current working directory
os.mkdir("my_dir")
os.chdir("my_dir")
print(os.getcwd())
os.chdir("..")
os.rename('my_dir', 'your_dir')
print(os.listdir())
os.rmdir("your_dir")
print(os.listdir())

