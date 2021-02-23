import os
try:
    fileName = "File1.cyg"
    with open(fileName, "r+") as file1:
        print(file1.read())
        file1.close()
except IOError:
    print("File ",fileName," not found")