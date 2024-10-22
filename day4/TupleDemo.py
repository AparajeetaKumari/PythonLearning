# List is mutable - Dynamic collection
# Tuple-Seq, Indexes -> Immutable - Static collection


l1= []
print(type(l1))

t1=("Selenium","Python","Pytest","Pytest","Pytest")
print(type(t1))
print(t1)
print(t1[1])


# tuples are immutable so updating tuples values is not allowed
# t1[1]="NewPython"
print(t1)
print(len(t1))

print(t1.index("Selenium"))
print(t1.count("Pytest"))