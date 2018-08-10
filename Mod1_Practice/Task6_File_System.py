<<<<<<< HEAD
# [ ] Complete the following program to:
import os, os.path

# 1) navigate to `parent_dir` directory (if not already in it)
if('parent_dir' not in os.getcwd()):
    # Changing the current working directory to parent dir
    print("Changing working dir to parent_dir")
    os.chdir('parent_dir')
    print("Current working directory:", os.getcwd())

# 2) create a new directory called `practice_1`
os.mkdir("practice_1")

# 3) change the working directory to `practice_1`
os.chdir('practice_1')

# 4) display the current working directory to verify you are in the correct location
print("Current working directory:", os.getcwd())
# 5) create a new directory called `practice_2`
os.mkdir('practice_2')

# 6) verify that `practice_2` was created by listing the content of the current directory
print(os.listdir('.'))

# 7) rename `practice_2` as `sub_practice_2`
os.rename('practice_2', 'sub_practice_2')


# 8) verify the name was successful changed by listing the content of the current directory
print(os.listdir('.'))

# 9) remove `sub_practice_2`
os.rmdir('sub_practice_2')


# 10) change working directory to the parent directory using `..`
os.chdir('..')


# 11) remove `practice_1`
os.rmdir('practice_1')


# 12) verify your current working directory and display its content
print("Current working directory:", os.getcwd())
print(os.listdir('.'))





#Path operations
# [ ] Write a program that prompts the user for a file or directory name
# if it exists in the current working directory, it prints whether it is a file or directory


=======
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
>>>>>>> origin/master

