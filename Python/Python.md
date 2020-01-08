hashbang: #!/bin/python3

## import os commands

  import os

  #use 
    
    os.system("Command")
 
 ## base64
 
 import base64
 
 base64.encodestring("").strip()
 base64.decodestring("")


 ## Math
  
  print(X + Y)
   
  + add
  - subtract
  * multiply
  / divide
  
  Note: intiger has no decimal point. Float has a decimal point.
  
  print(int(x)) #will round
  print(float(x.y)) # will not round
  
  if you need to print an int and a float together you can make the int into a string with str()
  
  str("30")
  
  Increase variable number
  
  age = 15 
  
  age += 1 

 ## Methods
 
 print(.upper()) # upper case
 
 print(.lower()) # lower case
 
 print(string.title()) # title font
 
 print(len(string)) #counts letters
 
## functions
  #note the unless specified to be global, funtions defined in a funtion is ONLY in the function
  
    def fun():   #define function and function name
       var1 =    #start to define what the function does
       var2 =
      print(var1 + var2)
    
    
     fun()       #calling the function to run

    def add(num):
       print(num + 1)
      
      
    add(3)   #this will print 3+1


 ## Boolean expressions

 True or False
 
 NOTE: "TRUE" is a string and TRUE is a boolean
 
 bool<number>
  
    bool1 = True  # will return TRUE if printed
  
    bool2 = False # Will return FALSE if printed
  
     bool3 = 3*3 == 9 # Will return TRUE if printed
  
     Y > Z  Y < Z (greater than / less than)
   
      and 
   
       or 
   
       not
   
   Google truth table for help
   
   Example:
    
     def drink(money):
        if money >= 2:
          return "You got drink!"
      else
          return "NO drink fo you"
          
      print(drink(3))
 
 
 ## if else and elif 

if

    if (X >= Y): 
         return "output"
     else
     
    fi
    
  elif  
    
    if (X >= Y) and (z = G): 
        return "output"
    elif (X != Y) and (z = G):
        return "output"
    elif (X != Y) and (z != G):
        return "output"
        
 
 ## Lists
 
 Live in square brakets []
 
 List is refered to numerically starting at 0.
 
     drinks = ["Cofee", "water", "Wine"]
  
     print(drinks(1))
    
     water
     
     1:3  grab 1 through 3
     
     1:  #grab starting at 1 to the end of the list
     
     :1  #everything before 1
     
     -1 #last item
     
     drinks.append("OJ")   #append to list
  
     drinks.pop(0)  #remove item 0 from list
     
   
  ## Tuples 
  
   Do not change once you have, unlike lists
   
   live inside brackets ()
   
 ## Looping
 
  ### For loops - start to finish of an iterate
  
    veg = [1, 3, 5]
    for x in veg: 
        print(x)
    
  ### While loops - Execute as long as true
  
    i = 1
    
    while 1 < 10
         print(i)
         i += 1
         
      
      
      
      
      
    
