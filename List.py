# List used to store multiple items in []
# List are indexed , ordered , mutable , duplicate

myList = ['apple',1,True]
myList.append('apple')

# ACCESSING AN ITEM IN LIST
firstIndex = myList[0]
lastIndex = myList[-1]

# LENGTH OF AN LIST
listLen = len(myList)

# TYPE OF AN LIST  
listType = type(myList)

# LIST CONTRUCTOR
newList = list(('banana',False,6))

# RANGE OF AN INDEX
rangeList = newList[:3]#* the return value must be  a new list

# CHECK AN ITEM EXIST IN AN LIST 
if 'banana' in newList:
    x = 'banana'
    
# CHANGE VALUE USING INDEX NUMBER
rangeList[0] = 'baffallo'

# CHANGE VALUE USING RANGE
rangeList[1:2] = 'al'
rangeList[:2] = 'mal'
rangeList[4:] = 'malayalam'#* need iterable value to use range (string,list,tuple etc..)

# ADDING VALUE TO LIST
x = ['apple',5,True]
x.append('appe') # added into the end 
x.insert(1,'mango') # index based value adding 

# JOINING TWO LIST
y = ['yellow','orange','red'] 
x.extend(y)# you can join any sequence/iterable (string,tuple,sets,dictionaries etc)type . 

# REMOVING VALUE FROM LIST
z = x + y
x.remove('appe') # expecting an value
x.pop() # can use  with & without index (remove last value)
del x[5] # can use  with & without index (delete the list entirely)
x.clear() # used to wipe out the list value. but the list still there

#  LOOPING THROUGH LIST
for i in y:
 x.append(i)

for i in range(1,len(y)): # defining from to where need to iterate;
    y.insert(i,y[i])
    
while len(y) > 0 :# using while loop
  y.pop()

# LIST COMPREHENSION
#* [expression for item in iterable if condition == True]shorter syntax for new list based on an existing list.
[y.append(i) for i in x]
new_List  =  [i for i in x if 'a' in i]

# LIST SORTING
x.sort()
x.sort(reverse=True)

# SORTING USING FUNCTION
def myfunc(n): 
  return abs(n - 50)#how close the number is to 50

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)

x.sort(key=str.lower)#check without case sensitive

x.reverse()# reversing the string

# COPYING THE LIST

#! cannot copy a list  by  list2 = list1, because: it will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

copyList =  thislist.copy()
copyList = list(thislist)
copyList = thislist[:]


# Method	    Description

# append()	  Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	  Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	  Adds an element at the specified position
# pop()	      Removes the element at the specified position
# remove()	  Removes the item with the specified value
# reverse()	  Reverses the order of the list
# sort()	    Sorts the list