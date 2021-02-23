import os

print(os.getcwd())
print(os.listdir("D:"))
print(os.name)
filePath = "‪D:\Learning\Python\Files\File1.txt"
filePath = filePath.strip("\u202a")

with open(filePath, "r") as file1:
    file1.seek(15)
    print(file1.tell())
    print(file1.read())
    file1.close()

with open(filePath, "rb") as file1:
    file1.seek(-10,2)
    print(file1.tell())
    print(file1.read())
    file1.close()