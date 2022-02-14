#remove duplicate using for loop
mylist = [1,4,2,5,2,1,4,9,7,5]
newlist = []
for i in mylist:
    if i not in newlist:
        newlist.append(i)
print(str(newlist))        