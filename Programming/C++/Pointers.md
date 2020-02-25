## Pointers

A pointer is a variable that holds a memory address. This address is the location of another object in memory. For example, if one variable (a) contains the address of another variable (b), a is said to point to b.

![3](https://user-images.githubusercontent.com/46513413/75292825-fdcd1700-57f2-11ea-9290-a9c2b5b92cf4.png)

If a variable is a pointer, it must be declared in a different way. 
We will write an * and the variable name. The general form is:

    type <operator>name;

    
      type = base type of the pointer (int, char...). Defines the type of variable the pointer can point to.
      name = identifier of the pointer variable

  Operators: There are two special pointer operators: * and &. 
 
         x = &y;
             
     The & returns the memory address of the variable. put the memory address of the variable y into x. Not the value of y but its address.

         x = *y;

     The * returns the value located at the address of the following operator. Places the value in memory pointed by y, into x. So if y contains the memory address of another variable, let us say counter, x will have the value of counter.


Example: 

![1](https://user-images.githubusercontent.com/46513413/75293592-7e404780-57f4-11ea-894d-957fff572445.png)

int defines the types of each variable. 

**p1** points to the memory address of the variable **x**.

**p2** points to the same memory address of **p1**, meaning that **p2** now points to the memory address of **x**.

The next statement assigns to variable **y**, the value located at the memory address pointed by **p2**. In other words, **y** now contains the value of the variable **x**.

With this last statement, we assign **5** to the value located at the memory address pointed by **p2**. Remember that **p2** was pointing to the memory address of **x**, so the value of **x** is now **5**.















