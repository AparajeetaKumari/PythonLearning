num =int(input("enter the year"))

if ((num%4==0 and num%100!=0) or (num%400==0)):
    print("The year is leap year")
else:
    print("The year is not a leap year")