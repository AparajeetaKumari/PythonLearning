# packing
t1=("Selenium","Python","Pytest","Pytest","Java")

# unpacking
a,b,*c=t1
print(a)
print(b)
print(c)

x,*y=t1
print(x)
print(y)

x,*y,z=t1
print(y)
print(x)
print(z)

