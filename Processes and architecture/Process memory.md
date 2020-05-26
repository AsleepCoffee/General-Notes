When a process runs it is typically organized from lower memory (top) to highest memory address (bottom)

<img width="893" alt="2" src="https://user-images.githubusercontent.com/46513413/82864109-bdfcf500-9ef1-11ea-89ac-1ac5276e1fce.PNG">

The process is divided into four regions:

- Text(or instruction segment): is fixed by the program and contains the program code (instructions). This region is marked read-only since the program should not change during execution.


- Data: divided into:
  
   - initialized data: Include items like static and global declared variables that are pre-defined and can be modified. 
   
   - uninitialized data(aka Block Started by Symbol (BSS)):  Initlializes variabnle that are initialized to zero or do not have explicit initialization (i.e static int t).


- Heap: Starts right after the BSS segment. During execution, the program can req more space in memory via *brk* and *sbrk* system calls, which are used by *mllc*, *realloc*, and *free*. with this the size of the data region can be extended.


- Stack: LIFO block of memory. Located in the higher part of the memory. Think of it as an array used for saving a functions return address, passing args, and storing local variables. 

 The purpose of the ESP (Extended Stack Pointer x86) register is to ID the top of the stack and is modified each time a value is pushed in (PUSH) or popped out (POP). 



































