# num= int(input("Please enter the number"))
even_number=[]
odd_number=[]

for num in range(20):
    if num%2==0:
        # print("Even")
        even_number.append(num)
    else:
        # print("Odd")
        odd_number.append(num)


print(f"even numbers{even_number}")
print(f"odd numbers{odd_number}")