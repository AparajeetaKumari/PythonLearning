
# store all prime numbers from 1-100

num1=int(input("Enter the number"))

if num1>1:
    for i in range(2,num1):
        if num1%i==0:
            print("not a prime number")
            break
        else:
            print("Its a prime number")
            break
else:
    print("Number is not a prime number")




