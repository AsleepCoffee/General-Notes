# C++

 Usually edited with an IDE (Integrated Development Environment)

**Syntax: **

  ;   Terminator. It tells the compiler that it has reached the end of a command.

**Comments: **
 
   // 

**Directives: **

  Instructs the compiler to include the code of libraries. A library is a collection of routines that a program can use.

   #
 
 **Namespaces: **
   
   Used to group a set of classes, functions etc under a name. Since all the elements in the standard C++ library are declared within the stdnamespace, we need this command to access its functionalities
   
**main function:**

  Here is the declaration of the main function of our program. The mainfunction is where our program execution starts. In other words, wherever the main function is declared in our source code, it will be the first code to be executed.
    
    int main ()
    { Function body
    }

### Input/Output

**cout**   
   
   Is the name of the standard output. Most of the time, the standard output is the console. The cout<<statement tells the compiler to put a sequence of characters, ‘Hello World!’ in our example, onto the standard output stream (the console). In other words, it prints the string ‘Hello World!’on the screen.
   
    cout << "string";
    
    << tells the program to insert the nest data into the stream.
  
    endl  inserts a new line character and flushes the buffer. Next output will print on the next line.
    
    cin >>   to get the users input
    
    
    cin.ignore();  will clear the buffer from user input. Following one will prevent use program from closing. 
______________________________________________________________________________________  
  
**Return:**
  
   Causes the main function to end. The return statement can have different values.
   
    return 0; = the program has completed its execution without any errors.

**Variables**

  Portions of memory where values are stored. We have to specify the type of data we are going to store in it.
   
   When declaraing new variables:
   
     <type> <variable name> = <value>;
     
   When changing values of an exisitng variable
   
     <variable name> = <value>;
     
   List of [data types](https://www.geeksforgeeks.org/c-data-types/)
   
   Depending on the position where it is declared it has a different scope: 
   
    global: Declared in the body of the source code (not in a function) and can be referred from anywhere.
    
    local: Declared inside a function body or block enclosed in curly brackets “{}” (main function in our case) and their scope is limited to the block where they are declared.
 
**Other:**

  -   output will no longer have the "press any button to continue"
   
