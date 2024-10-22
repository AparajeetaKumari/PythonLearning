
# list is a data type in python which can store values of any type
l1 =[21,22,45,67,True,"Selenium",None]

# list allow duplicate values
l1 =[21,21,22,45,67,True,"Selenium",None]

# Dynamic data dynamic type and it grows as per the data.

print(len(l1))
l1.append("Python")
print(len(l1))
print(l1)


# delete last element
l1.pop()
print(l1)

# Index based access of elements
print(l1[7])

# index error
# print(l1[11])

# delete all elements from list
l1.clear()
print(l1)

# sorting a list
names =['Selenium',"Cypress","Java","WDIO","Tosca","Playwrite"]
names.sort()
print(names)
names.reverse()
print(names)

# looping the list
for x in names:
    print(x)

print("**************")

# loop list
for x in range(len(names)):
    print(names[x])

# Delete last element using pop
names.pop()
print(names)

names.pop(2)
print(names)


newnames=["java","python","javascript",["restassured","selenium"]]
print(newnames[0])
print(newnames[3][0])