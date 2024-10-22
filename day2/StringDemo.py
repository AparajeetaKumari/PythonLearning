name = "Aparajeeta"

# indexing in string
print(name[0])
print(name[7])
# print(name[11]) --> error - string index out of range
print(name.upper())
print(name)

print(name.lower())

print(name.title())

# finding the element in the string
print(name.find('e'))

# finding the element in the string--> this will return -1
print(name.find('z'))

# slicing
print(name[0:4])
print(name[0:4:2])

print(name[0:8])
print(name[0:8:2])

print(name[0:])
print(name[:])

name1 = " selenium with python is intresting and fun "
print(name1.split())
print(name1.capitalize())
print(name1.count("selenium"))
print(name1.strip())
print(name1.replace("intresting","amazing"))