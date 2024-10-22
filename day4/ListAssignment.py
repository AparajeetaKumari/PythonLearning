
# enter list of 5 cities

# user_input=input("Please enter if you want to enter new city to visit, please enter YES or NO")
list_of_cities=["Chennai","Bangalore","Pune","Delhi","Goa"]

print(f"The list of cities is {list_of_cities}")
# new_city=""
#

# Code to enter the list of cities dynamically
# while user_input.lower()=="yes":
#     new_city = input("Enter the citi name")
#     list_of_cities.append(new_city)
#     user_input = input("Please enter if you want to enter new city to visit, please enter YES or NO")
# else:
#     print(f"final list of cities are {list_of_cities}")


update_city = input("Do you want to update the list,please enter yes or no")
new_city=""

# code to update the list based on index
# while update_city.lower()=="yes":
#     new_city=input("Please enter the city to be added")
#     inx=int(input("Please enter the order in the list"))
#     if inx<len(list_of_cities):
#         list_of_cities.insert(inx,new_city)
#     else:
#         list_of_cities.append(new_city)
#     print(list_of_cities)
#     update_city = input("Do you want to update the list,please enter yes or no")
# else:
#     print(list_of_cities)

# code to update the list based on entry
while update_city.lower()=="yes":
    new_city=input("Please enter the city to be added")
    after_city=input("Please enter the city after which new city should be added")
    if list_of_cities.__contains__(after_city):
        ind = list_of_cities.index(after_city)
        list_of_cities.insert(ind+1,new_city)
    else:
            print("Please enter city present in the list")
    update_city = input("Do you want to update the list,please enter yes or no")
else:
    print(list_of_cities)



print(list_of_cities)


delete_city = input("Do you want to delete entry from the list,please enter yes or no")

while delete_city.lower()=="yes":
    delete_city = input("Please enter the city to be deleted")
    if list_of_cities.__contains__(delete_city):
        list_of_cities.remove(delete_city)
    else:
        print("Please enter city present in the list")
    delete_city = input("Do you want to delete entry from the list,please enter yes or no")
else:
    print(f"Final list of cities {list_of_cities}")







