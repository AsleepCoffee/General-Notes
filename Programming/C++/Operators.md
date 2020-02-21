# Operators

Four main classes of operators:

 - Arithmetic
 
 - Relational
 
 - Logical 
 
 - Bitwise



## Assignment operator

      variable_name = expression;

 Can be used within any valid expression. The target (the left part –variable name) of the assignment must be a variable or a pointer  and can’t be a function or a constant.

In C++ literature, you will see these two terms: lvalue and rvalue.
 
   •lvalueis any label that appears on the left side of an assignment statement; in other words, we can say it is the variable name.
   
   •rvaluerefers to expressions/value on the right side of an assignment and simply means the value that will be assigned to the variable.


# Arithmetic

## Operators

 <img width="795" alt="Capture" src="https://user-images.githubusercontent.com/46513413/74990220-b1f42980-5410-11ea-854e-90b302e5b81a.PNG">
 
  There is also the increment operator (++) and decrement operator (--)
  
  
      ++a;    ++ adds 1 to the operand
      --a;    -- sub 1 from the operand

<img width="822" alt="1" src="https://user-images.githubusercontent.com/46513413/75067086-4070b580-54ba-11ea-832c-59345c035658.PNG">

<img width="791" alt="2" src="https://user-images.githubusercontent.com/46513413/75067116-58e0d000-54ba-11ea-8b68-ec973debcfc2.PNG">


The idea of true and false is the basic concept of relational and logical operators. True is any value other than zero. False is zero. Expressions that use relational or logical operators return 0 for false and 1 for true.
 We can use the booldata type and the Boolean constants true and false. So a 0 value automatically converts to false while a non-zero value automatically converts to true.

The logical operator !has only one operand (at its right i.e !x ) and it inverses this value (false if its operand is true, and true if its operand is false). 

The logical operator &&and ||evaluate two expressions in order to obtain a relational result.
  
   •&&(AND) results true if both operands are true and false otherwise
   
   •||(OR) results true if either one of its operands is true, false when both are false


## Bitwise operators 

 <img width="804" alt="3" src="https://user-images.githubusercontent.com/46513413/75067552-487d2500-54bb-11ea-9bd9-0c791fb14c53.PNG">

 <img width="798" alt="4" src="https://user-images.githubusercontent.com/46513413/75067710-a447ae00-54bb-11ea-969e-a21252870592.PNG">
 









