#Task 1: Directory Inspector:

    #Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

import os 

user_path = input("Please enter directory path:  ")
def list_directory_contents(user_path):

    # checking if path exists
    if os.path.exists(user_path):
        print("This is a path")

        # checking for directory path
        if os.path.isdir(user_path):
            print("This is a directory path")
            directories  = os.listdir(user_path)

            # displaying contents of directory path
            print("\nLoading subdirectories...")
            for sub in directories:
                print("-",sub)
            
        else:
            print("Not a directory path tho..")
    else:
        print("Sorry this path does not exist")

list_directory_contents(user_path)