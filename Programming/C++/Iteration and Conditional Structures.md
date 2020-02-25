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

<img width="804" alt="1" src="https://user-images.githubusercontent.com/46513413/75103156-017b5680-55c5-11ea-8e39-54443d683c13.PNG">


## Iteration

 Iteration statements, also called loops allow a set of instructions to be executed repeatedly for a fixed number of times or until a certain condition is reached. While in for loops the condition is predefined, in do-while loops are open-ended.
 
 **for**
 
 <img width="830" alt="1" src="https://user-images.githubusercontent.com/46513413/75103184-5a4aef00-55c5-11ea-8754-e08b07db9e6e.PNG">

 
  for loop can be infinite by leaving initialization, condition,and increment empty. 
  
      for( ; ; ) {
          statement;
      }
 
 When the conditional expression is left empty, it is processed as true. Note that the for( ; ; ) construct can exit from an infinite loop through a breakstatement present anywhere in the body of the loop. The break statement causes the termination of the loop, and the program control resumes from the next instruction following the loop.
 
 In the same way as with other statements, for loops can be nested. Nested loops are very common in programming since they add power and flexibility to complex algorithms.
 
**while**

The loop continues while the condition evaluates to true. When the condition evaluates to false, the program control goes to the line of code right after the loop

     while(condition) {
       statement;
      }
 
 <img width="828" alt="1" src="https://user-images.githubusercontent.com/46513413/75103259-4f448e80-55c6-11ea-9c7c-eef38d13c491.PNG">

**do-while**

Unlike for and while loops, which test the condition at the beginning of the loop, the do-whileloop checks its condition at the end of the loop; a do-while loop always executes at least once. Iterates until the condition evaluates to false. 
 
 
    do{
      statement;
    }while(condition);
 
 

C++ has four statements that can change the normal execution flow: return, goto, breakand continue. While return and goto are mostly used anywhere in your program, breakand continue statements are often used in conjunction with any of the loop statements.
 
**return**
 
Used to return from a function. Might have a vlaue associated with it. The expressionmust be used only if the function has a returning value. In this case, the value of the expression will become the return value of the function and can be associated with a variable. Can use as many return statements as we like within a function. However, the function stops executing as soon as it encounters the first return
 
     retrun <expression>;
     
**goto**

 It can be used to jump to a specific statement, such as jumping out of a set of deeply nested loops. The gotostatement requires a label. A labelis an identifier followed by a colon.  Note that the label must be in the same block of statements as the gotothat uses it, so we cannot jump between functions.
 
 
    gotolabel;
    ...
    ...
    label:

**break**

Has two uses: 
  •Terminates a case in the switch statement 
  •Forces the termination of a loop, bypassing the normal loop conditional test.

When we use the break statement within a loop, the loop terminates, and the program control resumes at the statement after the loop

![1](https://user-images.githubusercontent.com/46513413/75292384-0cff9500-57f2-11ea-982e-46eb177b9b19.png)


**Continue**

The continuestatement works similarly to the break statement. Instead of forcing termination, it forces the code to continue to the next iteration of a loop, skipping any code in between. 

![2](https://user-images.githubusercontent.com/46513413/75292537-64056a00-57f2-11ea-96a0-251c800f5635.png)












 
