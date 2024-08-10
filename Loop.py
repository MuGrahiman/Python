# Python has two primitive loop commands: while & for 

i=0
while i<6: #*execute a set of statements as long as a condition is true.
    j=0
    pass #used to to avoid getting an error if there is no content in an block of code
    while j < len(range(i)):#Nested while loop
        j += 1
        if i != 3:
            print(j)
        else:
            continue #used to continue an loop without running the beneath codes 
        if i == 4 :
            break #used to stop and get out from an loop completely even the condition is true 
                #*else block will NOT be executed if the loop is stopped by a break 
    else:
      print('Finished J While Loop for ',i,' times') 
    i += 1
else :#used to run an statement if the condition is no longer true.
    print('Finished the I while loop',i)    


for item in range(5):#used for iterating over a sequence
   for value in range(0, item, 3):#nested for loop
        if item == 3 :continue #used to continue an loop without running the beneath codes
        elif item == 5 :break#used to stop and get out from an loop completely even the condition is true 
                             #*else block will NOT be executed if the loop is stopped by a break 
        else :print(value)
   else:
        print(f'Finished Value loop for {item} times')       
         
else :
        print(f'Finished Item loop for {item} times')       
    