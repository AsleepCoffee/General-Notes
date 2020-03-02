# lists

   list = [1,2,"three",4,"five"]

 Live in square brakets []
 
 List is refered to numerically starting at index 0.
 
     drinks = ["Cofee", "water", "Wine"]
  
     print(drinks(1))
    
     water
     
     1:3  grab 1 through 3
     
     1:  #grab starting at 1 to the end of the list
     
     :1  #everything before 1
     
     -1 #last item
     
     drinks.append("OJ")   #append to list
     drinks + ["OJ"]       # append to the end
     drinks[0] + "OJ"      #replace certain position 
  
    •append: append a new element to the target list
    •extend: allows to add one list to another 
    •insert:  add a new list element right before a specific index

  
     drinks.pop(0)  #remove item 0 from list
     del drinks[2]
     
     drinks.remove(2)   # It does not work with indices; instead, it looks for a given value within the list, and if this exists, it removes the element. Note that only the first instance of that value is removed.
     
    - list.pop(i)Removesthe item at the given position
    - list.sort()Sorts a list (they must be of the same type)
    - list.reverse()Reverses the order of the elements in thelist
    
    
  
