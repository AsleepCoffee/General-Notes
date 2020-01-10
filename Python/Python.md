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
         
  ### Advanced strings
  
 Using list logic to print specific characters in a sting.
 
 test = "This is a test"
 
 print(test[:2])  # print characters 0 to 2
 
 .split #splits strings up based on a delimiter 
 
 .join #joins a string together based on a delimiter
 
 \ #escape special characters
 
 {}  .format(<variable>)  #will place the variable inside the curly brackets.
 
 
 ### Dictionaries - key/values {}
 
     var = {"coke": 3, "sprite": 4,}     #drink is key, price is value
  
  #Can have multiple values to one key
  
     work = {"HR": ["user1", "user2"], "IT": ["user3", "user4"]}
   
   #Adding new key and value pair 
   
     work[HR] = ["user5"] 
     
     work.update({"Network": ["User1", "User2"]})
     
 
  
  ### Sockets - Used to connect to open ports 
 
    import socket
   
    host = 'X.X.X.X'
 
    port = Y
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #AF_INET basically means IPv4, SOCK_STREAM for port
   
    s.connect((HOST,PORT))
 
    socket.setdefaulttimeout(1) #timeout on port connect attempt, then move on
    
   Error examples 
     
     try: 
     
     except socket.gaierror:
       print("Hostname could not be resolved")
       sys.exit()
   
     except socket.error:
        print("could not connect to server")
        sys.exit()  
    
 
  ### Keyboard interupt
  
    try:
        
    except KeyboardInterrupt:
       print("\n Exiting program")
      sys.exit()
  
 
 
 
 
      
      
      
      
    
