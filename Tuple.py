# TUPLE used to store multiple items in ()
#Tuple items are ordered, unchangeable, and allow duplicate values.

myTuple = ('apple','orange','grapes')#packing / creating
lenTuple = len(myTuple)# finding length of an tuple
oneValueTuple = ('one',)#* need to add coma for create one value tuple.with out the coma consider as string
type(oneValueTuple) #checking the type
tuple1 = tuple(("male")) #creating tuple using constructor

#ACCESSING INTO TUPLE
myTuple[1]
myTuple[-1]
myTuple[1:2]
if 'Apple' in myTuple:#check the value in the tuple
    print(True)
    
# UPDATING TUPLE
x = ("apple", "banana", "cherry") #! cant update directly
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# ADDING VALUE INTO TUPLE
thistuple = ("apple", "banana", "cherry") #! cant add  directly
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# REMOVING TUPLE VALUE
thistuple = ("apple", "banana", "cherry")#! cant remove directly
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)

# DELETE THE TUPLE
del oneValueTuple

# UNPACK THE TUPLE
(b,a)= thistuple

#ASTERISK: #* used to handle variable lengths efficiently.
(_,n,*banana)= thistuple

#LOOPING
for i in thistuple:
    y.append(i)
    
for i in range(len(thistuple)):
    y.insert(i,thistuple[i])
    
while len(y)>0:
  y.pop()
  
# JOINING TUPLES 
joinTuple = thistuple + myTuple

# MULTIPLY TUPLES
multipliedTyple = thistuple*2


# Method	Description

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found