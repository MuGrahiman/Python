# Dictionaries used to store multiple value in {key:value} pair              
# Dictionary is a collection which is ordered, changeable and do not allow duplicates.
# when added new value with same key it will overrighted the exist value

myDict = {
    'brand':'Ford',
    'model':'Mustang',
    'year':'1964',
    'electric':False,
    "colors": ["red", "white", "blue"]
}

# LENGTH 
lenDict= len(myDict)

# TYPE 
typDict = type(myDict)

# CONSTRUCTOR 
conDict = dict(name = 'john',age=26,married=False)

# ACCESSING
X = myDict['model']
model = myDict.get('model')
keys = myDict.keys()#return:([])
values = myDict.values()#return:([])
items = myDict.items()#return:([(key:value)])

# CHANGING 
myDict.update({'year':2020})
if 'model' in myDict:#checking the keys
 myDict['model1'] = model
if model in myDict.values():#checking the values
 myDict['model2'] = model
 
#  ADDING 
myDict['owner'] = 'Mujeeb'#TODO we can use update for adding with new key value

# REMOVE 
popvalue=myDict.pop('owner')
popitme=myDict.popitem()#!not take any arguments
del myDict['year']#TODO without argument it will delete whole dict
myDict.clear()
#* del delete whole dictionary. clear remove all key value

# LOOP 
[myDict.update({i:conDict[i]}) for i in conDict]#loop through keys
for i in myDict.keys():# loop through keys
    print(i)
for i in myDict.values():# loop through values
    print(i)
for i , j in myDict.items():# loop through key values
    print(i,j)
    
# COPYING
#! cant copy newDic = myDict . it will be reference. any changes occure in one effect for both

newDict = myDict.copy()
newConDict = dict(myDict)

#  NESTED DICTIONARIES
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])
    
    
    
# Method	    Description

# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary