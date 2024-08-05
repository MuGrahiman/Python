# TUPLE used to store multiple items in ()
#Tuple items are ordered, unchangeable, and allow duplicate values.
myTuple = ('apple','orange','grapes')#packing / creating
lenTuple = len(myTuple)
oneValueTuple = ('one',)# need to add coma for create one value tuple.with out the coma consider as string
type(oneValueTuple) #checking the type
tuple1 = tuple(("male"))

#ACCESSING INTO TUPLE
myTuple[1]
myTuple[-1]
myTuple[1:2]
if 'Apple' in myTuple:#check the value in the tuple
    print(True)
# UPDATING TUPLE
x = ("apple", "banana", "cherry") # cant update directly
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# ADDING VALUE INTO TUPLE
thistuple = ("apple", "banana", "cherry") # cant adding directly
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
# REMOVING TUPLE VALUE
thistuple = ("apple", "banana", "cherry")# cant remove directly
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)
# DELETE THE TUPLE
del oneValueTuple
# UNPACK THE TUPLE
(b,a)= thistuple

#ASTERISK: checking chance for is there any more length
(_,n,*banana)= thistuple # you can use * to any value to avoid the error (_,*n,banana) 

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
print(multipliedTyple)