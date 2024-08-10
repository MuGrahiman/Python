#SET used to store multiple items in {}
#Set items are unordered(cannot access using index), unchangeable, and unindexed do not allow duplicates.

#CREATING AN SET
conSet = set(('orange','long','live'))
#*Note: The values (True and 1)&(False and 0) are considered as same value in sets, and are treated as duplicates:
mySet = {'apple',1,True,False,0}#*it wil only add 'apple',1 & false .others treated as dupes

#ACCESSING & LOOPING
for x in mySet:#*Note: Sets are unordered, so you cannot be sure in which order the items will appear.
    mySet.add(x)
exitValue = 'long' in conSet
notExitValue = 'long' not in conSet

#ADDING & UPDATING & REMOVING VALUES 
#*Note: Set items are unchangeable, but you can remove items and add new items 
#! cant update an value:myset.insert(in,value)
mySet.add('NEW VALUE')
arr = ['NEW', 'NEW', 'VALUE']
mySet.update(arr) #TODO you can join another set using this method by updating existing set 
mySet.remove('NEW')
mySet.discard('VALUE')#*if the item is not exit .discard do not raise any error
#*Note: Sets are unordered, so you cant define the index.
mySet.pop()
del mySet

# JOINING SETS
newSet = {'long','live','hail','hitler'}
oldSet =set(arr)
unionSet = newSet.union(oldSet)#* returns a new set
shortUnionSet = newSet | oldSet
#TODO can join multiple sets: newSet.union(conSet,newSet) || newSet | ConSet |oldSet
# JOINING TUPLE SETS  
consTuple = tuple(arr)
newSet.union(consTuple)#! cant join tuple and set using short form : newSet | consTuple

#INTERSECTION 
intersectSets = newSet.intersection(conSet) #* return new set, that only contains duplicates
shortInterSet = newSet & conSet #* only join set types
intersectSets.intersection_update(conSet)#*same as intersect .instead of returning new set it will change the original one

# DIFFERENCE :#* return a new set with unique items from the 1st set that are not in the 2nd set.    
difSet = newSet.difference(conSet)
shortDifSet = newSet - conSet #short form
difSet.difference_update(shortDifSet)#* same as diffrence but update the existing set 

# SYMMETRIC DIFFERENCE :#* return a new set with unique items only from both set. 
simSet = newSet.symmetric_difference(conSet)
shortSimSet = newSet ^ conSet #short form #* dont allow other data type.only set
simSet.symmetric_difference_update(shortDifSet)#* same as symmetric but update the existing set 


# Method	                        Shortcut	           Description

#* add()	 	                               Adds an element to the set
#* pop()	 	                               Removes an element from the set. cant define the index
#* remove()	 	                               Removes the specified element
#* discard()	 	                           As like Remove but no throw the error if not found
#* clear()	 	                               Removes all the elements from the set
#* union()	                            |	   Return a set by joining only unique values from two sets .
#* update()	                            |=	   As like union but modify original set
#* intersection()	                    &	   Returns a set, by providing only duplicate values from two sets
#* intersection_update()	            &=     As like intersection by modify the original set
#* difference()	                        -	   Returns a new set with items from the first set not in the 2nd 
#* difference_update()	                -=	   As like the difference but modify the original set
#* symmetric_difference()	            ^	   Returns a set with the unique elements only from both sets.
#* symmetric_difference_update()	    ^=	   As like the symmetric difference but modify the original set
#  copy()	 	                               Returns a copy of the set
# isdisjoint()	 	                           Returns whether two sets have a intersection or not
# issubset()	                        <=	   Returns whether another set contains this set or not
#                                       <	   Returns whether all items in this set is present in other, specified set(s)
# issuperset()	                        >=	   Returns whether this set contains another set or not
#  	                                    >	   Returns whether all items in other, specified set(s) is present in this set