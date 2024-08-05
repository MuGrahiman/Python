# list used to store multiple items in []
myList = ['apple',1,True]
# List are indexed , ordered , mutable , duplicate
myList.append('apple')
# accessing an item in list
firstIndex = myList[0]
lastIndex = myList[-1]
# Length of an list
listLen = len(myList)
# type of an list  
listType = type(myList)
# list contructor 
newList = list(('banana',False,6))
# range of index
rangeList = newList[:3] # the return value must be  a new list
#  check item exist in an list 
if 'banana' in newList:
    x = 'banana'
# change value using index number
rangeList[0] = 'baffallo'
# change value using range
rangeList[1:2] = 'al'
rangeList[:2] = 'mal'
rangeList[4:] = 'malayalam' # when we try to mutate the value using range we need to use iterable value like string , list etc.not just single numbers

x = ['apple',5,True]
# ADDING VALUE TO LIST
x.append('appe') # added into the end 
x.insert(1,'mango') # index based value adding 
y = ['yellow','orange','red'] 
# JOINING TWO LIST
x.extend(y)# you can join any sequence/iterable (string,tuple,sets,dictionaries etc)type . 
z = x + y
# REMOVING VALUE FROM LIST
x.remove('appe') # expecting an value
x.pop() # can use  with & without index (remove last value)
del x[5] # can use  with & without index (delete the list entirely)
x.clear() # used to wipe out the list value. but the list still there

#  LOOPING THROUGH LIST

for i in y:
#  print(y)
 x.append(i)

for i in range(1,len(y)): # defining from to where need to iterate;
    y.insert(i,y[i])
    
while len(y) > 0 :# using while loop
  y.pop()

# LIST COMPREHENSION
# [expression for item in iterable if condition == True]shorter syntax for new list based on an existing list.
[y.append(i) for i in x]
new_List  =  [i for i in x if 'a' in i]

# LIST SORTING
x.sort()
x.sort(reverse=True)

# sorting based on function
def myfunc(n): 
  return abs(n - 50)#how close the number is to 50

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)

x.sort(key=str.lower)#check without case sensitive

x.reverse()# reversing the string

# COPYING THE LIST

#  cannot copy a list  by  list2 = list1, because: it will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

copyList =  thislist.copy()
copyList = list(thislist)
copyList = thislist[:]
