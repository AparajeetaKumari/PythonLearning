str = input("Enter the String")

revsd = ""

# using for loop
for x in str:
    revsd = x+revsd
print(revsd)

# slicing
print(str[::-1])