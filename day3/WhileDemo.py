
# WAP which will keep adding student until user is saying no

students=[]
while True:
    name = input("Enter the name of the student")
    students.append(name)
    choice = input("Do you want to enter more student names")
    if choice =="No":
        break

print(students)