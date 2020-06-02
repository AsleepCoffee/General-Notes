
<img width="893" alt="2" src="https://user-images.githubusercontent.com/46513413/82864109-bdfcf500-9ef1-11ea-89ac-1ac5276e1fce.PNG">


The Stack grows downward from high memory address to lower memory addresses. 
 
 *Note:* probably due to historical reasons when memory in old computers was limited and divided into tweo parts: heap and stack. It was decided that the Heap would start from the lower adresses and grow upwards and the Stack would start from the end of the memory and grow downwards.

The Stack is LIFO. the most fundamental operations are the PUSH and the POP. The main pointer for these operations is the ESP (stack pointer) which contains the memory address for the top fo the stack and changes during each PUSH and POP operation. 


**PUSH and POP operations**

PUSH: subtracts 4 (in 32-bit) or 8 (in 64-bit) from the ESP and writes the data to the memory addr in the ESP, then updates the ESP to the top of the stack. Since the stack grows backward the PUSH subtracts 4 or 8 in order to point to a lower memory location on the stack. If we do not subtract it, the PUSH operation will overwrite the current location pointed by ESP and we would lose data. 

  ESP = a memory location. We want to PUSH a value into the stack. We will subtract the memory needed from the top of the stack and subtract that value from the ESP so the ESP points to a lower point in memory as the top of the stack. ESP will point to a lower memory location to account for the new data we PUSH into the stack.


POP: It retrieves data from the top of the stack. The data contained at the address location in ESP (the top of the stack) is retrieved and stored (usually in another register).
 After a POP operation, the ESP value is incremended, in x86 by 4 or in x64 by 8. Note that the data is not deleted (or zeroed), it is just able to be overwritten now by another instuction.


## Stack frames 

The Stack consists of logical stack frames (portions/areas of the Stack), that are PUSHed when calling a function and POPped when returning a value.

Functions contain components:

prologue: prepares the stack to be used (like a book mark in a book)

epilogue: When the function has finished, this resets the stack to the prologue settings. 


When a subroutine starts (function, procedure) a stack frame is created and assigned to the current ESP location (top of the stack). Allows the subroutine to operatre independently in its own location in the stack

When subroutine ends 2 things happen: 

- program receives the parameters passed from the subroutine
- the Instruction pointer (EIP) is reset to the location at the time of the initial call

i.e stack frame keeps track of the location where each sub routine should return the control when it terminates.










