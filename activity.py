import os

file_path = 'file handling.txt'  # Define the variable properly
if os.path.exists(file_path):
    print("the file already exist")
else:
    print("the file does not exist. please check the file path")
    file = open("file handling.txt", "x")