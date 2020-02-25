# Functions

Functions are blocks of statements defined under a name. In other words, it is a group of statements that get executed when this name is called in the program.


      type function_name(paramenter1, parameter2,...){
          statements;
      }



       •type specifies the type of data that the function returns 
       •function_name is the identifier used to call that function
       •parameters is a comma-separated list of variables and their associated types. Those variables receive the values when the function is called. 

Note that functions may have no parameters, but they still require parentheses ‘()’.

![1](https://user-images.githubusercontent.com/46513413/75294756-340c9580-57f7-11ea-9fd1-8df7cde3756f.png)

Since this function uses two arguments, we have to declare two variables (int x,int y) that will accept the values from the caller. These variables are called formal parameters of the function. They are like any other local variable inside the function, and they are declared when the function is called and destroyed when the function returns.

There are typically two ways in which we can pass arguments to a function: By value and by reference.

The first method, call by value, copies the value of an argument into a parameter. In this case, changes made to the parameter do not affect the argument. By default, C++ uses call by value; this means that the code in the function does not alter the arguments used by the caller.

![1](https://user-images.githubusercontent.com/46513413/75296366-f6117080-57fa-11ea-8d17-0029f9e48b43.png)

The second method, call by reference,passes arguments in a different way. With this method, the addressof an argument (not the value) is copied into the parameter. Inside the function, the address is used to access the actual argument used in the call, so changes made to the parameter affectthe argument.

We can create a call by reference by passing a pointer to an argument instead of the argument itself.

In the declaration of the function, the type of each parameter is followed by an ampersand sign that specifies that their corresponding arguments are to be passed by reference; this means that we are passing the variable itself and not its value.

**swap**
The swapfunction exchanges the values of the two variables iand jbecause we pass the variables and not just their values.

Any modification to local variables in the swap function will have an affect on the variables passed as argument (&iand &j).
 

