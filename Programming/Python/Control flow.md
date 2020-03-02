## Control flow

Different ways to rep boolean values:

 0 
 False
 None
 "" - empty string
 [] - empty list
 
 All else is true
 
 


        if <expression>:

            statement

        elif <expression>:

            statement

        else:

            statement


elif: With the elif statement, we can check several expressions until we find one that evaluates to true. Once an expression is evaluated to true, its corresponding block will be executed.


![ex1](https://user-images.githubusercontent.com/46513413/75724489-8133b000-5cac-11ea-907b-0c8ef50f2228.png)


## while and for loops


      while <condition>:
          statment
      post while statment    
          
   While condition is true, the loop remains. If the condition is not true, then the loop exits and mvoes onto the next statment.
   
      for <item in seq>
            statments
      post for loop statment

 The forloop does not increment and test a variable against a condition on each iteration. It simply iterates through the values of a sequence object, such as strings, lists or function like range. The body of the forloop will be executed for each element in the sequence.


 range()
  
   returns a seq of given numbers. This is very useful if we want to iterate with explicit indices. range(5) returns an iterableobject that contains values from 0 to 4.
   
   list(range(0,10)) list() can be used to print all elements within the range.
   
   With 2 arguments ( range(x,y)), we are saying which is the starting number (x) of the sequence and which is the last number (y) of the sequence. With 3 arguments ( range(x,y,z)), we can also choose the step value between each item in the sequence.




