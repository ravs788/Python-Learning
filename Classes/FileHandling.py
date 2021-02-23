L = ["This is OneDelhi6 \n", "This is Paris-Love \n", "This is London-Smirth \n"] 

filePath = "‪D:\Learning\Python\Files\File1.txt"
filePath = filePath.strip("\u202a")

file1 = open(filePath, "w+")
print(file1.tell())
file1.write("This is the beginning of the end.")
print(file1.tell())
file1.writelines(L)
print(file1.tell())
print(file1.readline())
print(file1.readline())
file1.close()