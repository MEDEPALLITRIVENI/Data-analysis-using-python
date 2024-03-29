# -*- coding: utf-8 -*-
"""Day1_HW_set_tuples

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ThgoZisZrx993QQtzhcsju7Q25GELZ6X
"""

#creating a set
s={'a','e','i','o','u','a','e'}
print(s)

#creating a set using set keyword
list=[1,2,3,4,5]
s=set(t)
print(s)

#No duplicate elements in a set
s={1,2,3,4,5,6,7,8,9,2,4,6,8}
print(s)

#adding a element to a set
s={'a','e','i','o'}
s.add('u')
print(s)
s1={1,2,3,4,5}
s1.add(6)
print(s1)

#add set of elements to another set
s={'a','e','i','o','u'}
s1={1,2,3,4,5}
s.update(s1)
print(s)

#Remove pop clear in a set
s={1,2,3,'o','u',4,5,'a','e','i'}
print(s.pop())
print(s)
s.remove('u')
print(s)
s.clear()
print(s)

#Set operations
s1={1,2,3,4,5,8}
s2={6,7,8,9,2,5}
uni=s1.union(s2)
print(uni)
intersec=s1.intersection(s2)
print(intersec)
diff=s1.difference(s2)
print(diff)
sub=s1.issubset(s2)
print(sub)
super=s1.issuperset(s2)
print(super)

#disjoint of sets
A = {1, 2, 3,4}
B = {4, 5, 6}

# checks if set A and set B are disjoint
print(A.isdisjoint(B))

#Creating a tuple :
t=(1,2,3,4,5)
print(type(t))

#tuple functions
tup=(1,'o',2,3,'o','u',4,5,'a','e','i','o',)
print(len(tup))
print(tup.count('o'))
print(tup.index('o'))

#tuple functions
tup1=(1,5,7,2,8,9,3,5,4)
print(sorted(tup1))
tup2=('a','e','i','o','u')
print(sorted(tup2))

#tuple functions
tup=(925,76,14,59,0,13,600)
print(min(tup))
print(max(tup))

#adding two tuples
t1=(1,2,3,4,5)
t2=('triveni','reshma','sri','varsha','siva')
print(t1+t2)

#converting list to tuple
l1=['a',1,'e',2,'i',3,'o',4,'u',5]
tup=tuple(l1)
print(tuple(tup))
print(type(tup))

#updating a value in tuple
t = ('triveni', 'reshma', 'sri', 'varsha', 'siva')
x = list(t)
x[3] = 'kavya'  # Update the value in the list
y = tuple(x)
print(y)

#replicating tuple
tup=(1,2,3,4,5)
print(tup*2)

#sort function in list
a=[8,6,7,12,3,5]
a.sort()
print(a)

#sorted function in list
a=[8,6,7,12,3,5]
sorted(a)
print(a)
b=sorted(a)
print(b)

a=(8,6,7,12,3,5)
b=sorted(a)
print(a)
print(b)

#deleting tuple
tup=(1,2,3,4,5)
del tup