
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

i.e stack frame keeps track of the location (i.e its variable and such) where each sub routine should return the control when it terminates.
Overview example:

When a function (example main()) is called it is PUSHed to the top of the stack , if main() calls another function, then that is no PUSHed to the top of the stack. When that function returns, it is POP from the stack and the stack pointer moved to the new top where main() until it is POPed. 

**CALLs**

When a function is CALLed. The processor PUSHes the content of the EIP to the stack and points to the first byte after the CALL instruction (important as we need t o know the address of the next instruction in order to proceed when we return from ,the function call. The caller (instruction that executes the function calls (sometimes OS)) loses control and the callee (function that is called - i.e main() for example) takes control.

Example: in main() function. A new stack frame is to be created. It is defined by the EBP (Base Pointer) and the ESP. We dont want to lose the old stack frame info, save current EBP on the Stack. If this was not done, when we returend we would not know that this info belonged to the previous stack frame(i.e the function that called main()). Once this value is stored the EBP is updated and it points to the top of the stack. 

<img width="1450" alt="Capture" src="https://user-images.githubusercontent.com/46513413/83577248-bfd24400-a501-11ea-9aa9-191adfa9e049.PNG">

## Prologue 

Sequence of instructions that take place at the beginning of a function, for all functions. 
Once the callee gets control it will execute the following instructions: 

    push ebp  
    
saves old base pointer onto the stack, so it can be restored later on when the function returns. EBP is currently pointing to the location of the top of the previous stack frame.
    
    mov ebp, esp
 Copies the value of the Stack pointer (ESP top of stack) onto the base pointer (EBP); creates a new stack frame on top of the stack. Base of new stack frame is on top of the old stack frame. Note that the copy destination is the first operand. 
    
    sub esp, X  # X is a number
Moves stack pointer (top of the stack) by decreasing its value; to make space for local variables. Similar to last , esp is destination where X is the value (source). Instruction subtracts X from esp.

Makes enough space in the stac kto copy local variables. Variables are allocated by decreasing the stack pointer (top of stack) by the amount of space required.

Once the prologue ends the stack frame for main() (example) is complete.  Local variables are copied to the stack.

Since at this point the ESP is not pointing to the memoty addr right after EBP, we cannot use PUSH since PUSH stores the value on top of the stack (addr pointed by ESP). 

Variables are hex value that is an offset from the EBP or the stack pointer

## Instructions after the prologue

are like the following: 

     MOV DWORD PTR SS: [ESP+Y] , 0B
     
  Means:move value 0B (hex of 11 - first local variable) into memory address location pointed at ESP+Y. Note: Y is a number and ESP+Y points to a memory address between EBP and ESP. 

<img width="1456" alt="Capture" src="https://user-images.githubusercontent.com/46513413/83578365-949d2400-a504-11ea-98e0-91224d926e07.PNG">


Over view of the process: 

1. PUSH function parameters in the stack

2. call the function 

3. execute the prologue (which updates the EBP and the ESP to create the new stack frame)

4. Allocate the local variable onto the stack

This gets repeated for otehr functions that gettt called inside a function. 

Will look something like this 


<img width="768" alt="Capture" src="https://user-images.githubusercontent.com/46513413/83578784-9d422a00-a505-11ea-837b-8c84c9045912.PNG">








