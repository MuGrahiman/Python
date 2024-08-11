# IF ELSE :statement is used to control the flow of the program based on conditions

if 10 > 0:#defining condition
  print("10 is greater than 0")
elif 10 < 0:#defining multiple condition
    print('0 is greater than10')
else:#defining code for execute if the condition is wrong
    print('0 is equal to 10') 
    if 10 == 0:#defining nested condition
        pass #used to pass the execution with out any error if there is no codes
  
# SHORT FORMS 
if not 1 < 2 :print(1<2)#if condition using not logical operator
print('1 is greater than 2') if (1 > 2) else print('1 is less than 2')# if else condition
print('1 is greater than 2') if (1 > 2) else print('1 is less than 2') if (1 < 2) else print('1 is equal to 2') # multiple condition