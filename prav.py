a=["September","Praveen",123,2.333,True]

print(a)
print(type(a))

#Indexing
print(a[3])

print(a[-1])

print(a[0])

print(a[-3])

#Updating the list
a[1]="Deepthi"
print(a)

#Appending 
a.append("Nithin")
print(a)

#inserting
a=["September","Praveen",123,2.333,True]
a.insert(24,5.7)
print(a)

#deleting the data
del a[2]
print(a)

a.pop(1)
print(a)

a.remove(5.7)
print(a)

l=('Praveen',33.3,True,234)
print(type(l))
print(l)

#l.('Sarika')
print(l)

print(l[0])

#del l[0]
print(l)

#Dictionary
mydic= {
        "Name":"Praveen",
        "Roll no":"20211csg0016",
        "Branch":'Computer science and technology',
        "Place": 'Bangalore',
       }
print(mydic)
print(type(mydic))

print(mydic["Name"][1])

print(mydic["Name"][-1])
