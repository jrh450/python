#!/usr/bin/python
# -*- coding: utf-8 _*_

print( "\n\n       Welcome to the python temperature conversion app!")
count = 0
while True:
    count += 1

    scale = (input("\nPlease indicate the temperature scale you are converting from by entering c for celcius  or f for fahrenheit. \n "))
    if scale not in ['f' , 'c']  :
        print('\nYou did not enter a letter c or letter f as requested.')
        if count == 3:
            print("\nYou have tried too many times! Good bye!")
            exit()
        continue
    else:
        break
 
if scale == "f":
        scale = "fahrenheit"
			
else:
        scale = "celcius"	
        
count = 0  
             
while True:
    count += 1
    try:
        temp = int(input("\nPlease enter a "+scale+" temperature that is less than 1000.   \n  ") )
    except ValueError:
    #if not temp:
        if count == 1:
            print("Sorry that is not a number! You have tried once!")
        else:
            print("Sorry that is not a number! You have tried",count,"times!") 
        if count == 3:
            print("\nYou have tried to many times! Good bye!")
            exit()
        continue 
    #    count = 0     
    if temp > 999:
        
        if count == 1:
            print("The number is too high! You have tried once!")
        else:            
            print("The Number is too high! You have tried",count,"times!")
        if count == 3:
            print("\nYou have tried too many times! Good bye!")
            exit()
        continue
    else:
        break
          
print()
        
if scale == "celcius":
    fahrenheit  = (9/5) * int(temp) +32
    print('It appears that',int(temp), ' degrees celcius converts to',round(fahrenheit, 2) ,' degrees fahrenheit')
	
elif scale == "fahrenheit":
    celcius  =  (int(temp)-32) *(5/9)
    print("It appears that",int(temp),"degrees fahrenheit converts to",round(celcius,2),"degrees celcius.")
print("\n\n")
