# rewirte the values
file = open("d:/readfile/file.txt")
files = file.readlines()
print(files)
files.pop()
files.append("fourth")
print(files)
file.close()

file = open("d:/readfile/file.txt","w")
for i in files:
    file.write(i)
file.close()    
