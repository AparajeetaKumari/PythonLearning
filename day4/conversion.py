# conversion of tuple to list
t1=(10,20,30)

l1=list(t1)
l1.append(40)

print(l1)


tuple1=(10,20,30,(40,50))
a,b,c,d=tuple1
print(a)
print(b)
print(c)
print(d)
print('*********')
l1=list(d)
print(l1)

l1.append(a)
l1.append(b)
l1.append(c)
print(l1)

