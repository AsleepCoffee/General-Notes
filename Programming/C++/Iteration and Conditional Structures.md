## Iteration and conditional structures

These structures are useful to instruct the program to execute or to repeat a specific operation when some condition is matched.

A statement is part of our program that can be executed and specifies an action. 

Three main statements: 

 - **SELECTION:** if, switch
 
 - **ITERATION:** while, for, do-while
 
 - **JUMP:** break, continue, goto, return
 

## SELECTION 

**if else** statements. Can be nested, nested else applies to neares if that is not already associated to an else.

**switch** 

  [Switches](https://www.w3schools.com/cpp/cpp_switch.asp)
  
  The value of the expression is sequentially tested against the values specified in the casestatements. When a match is found, the statement block associated is executed until the break statement, or the end of the switch is reached. The defaultstatement is executed if no matches are found. Note that defaultis optional, so if it is not defined, there is no action if all matches fail. 
  
   Note: the break statement is one of the jump statements. can be used in loops as well. When break is encountered in a switch, the execution “jumps” to the line of code following the switch statement.
  
    switch (<expresion>) {
   
       case <constant1>:
          statement sequence
       break
       
       case2 <constant2>:
          statement sequence
       break
       .
       .
       .
       default
          statement sequence
     }
