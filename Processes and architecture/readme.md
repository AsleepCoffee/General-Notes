When a program runs on a machine, the computer runs the program as a process. Current computer architecture allows multiple processes to be run at the same time by a computer. While these processes may appear to run at the same time, the computer actually switches between the processes very quickly and makes it look like they are running at the same time. Switching between processes is called a **context switch**. Since each process may need different information to run(e.g. The current instruction to execute), the operating system has to keep track of all the information in a process. The memory in the process is organised sequentially and has the following layout: 

![1](https://user-images.githubusercontent.com/46513413/80920034-36312a00-8d3b-11ea-9869-e135c17bd68b.png)

- **User stack** contains the information required to run the program. This information would include the current program counter, saved registers and more information. The section after the user stack is unused memory and it is used in case the stack grows(downwards). A program would usually comprise of multiple functions and there needs to be a way of tracking which function has been called, and which data is passed from one function to another. The stack is a region of contiguous memory addresses and it is used to make it easy to transfer control and data between functions. The **top of the stack is at the lowest memory address** and the **bottom of the stack is the highest memory address**. The most common operations of the stack are: **Pushing:** used to add data onto the stack and **Popping:** used to remove data from the stack.

 Example:

      push var
  This is the assembly instruction to push a value onto the stack. It uses var or value stored in memory location of var.
    
 **RSP (Register: Stack Pointer):** Points to the top of the current stack frame.
 
  Decrements the rsp by 8. Writes the value to new location of rsp, which is now the top of the stack (mem location 0x8)
  
      pop var
   This is an assembly instruction to read a value and pop it off the stack. It reads the value at the address given by the stack pointer.
   
   Stack Top(memory location 0x0)(rsp points here)
   Increment the stack pointer by 8.
   Store the value that was read from rsp into var.
   
 It’s important to note that the memory does not change when popping values of the stack - it is only the value of the stack pointer that changes! 
 
 Each compiled program may include multiple functions, where each function would need to store local variables, arguments passed to the function and more. To make this easy to manage, each function has its own separate stack frame, where each new stack frame is allocated when a function is called, and deallocated when the function is complete. 
 
 ![2](https://user-images.githubusercontent.com/46513413/80920675-4e0aad00-8d3f-11ea-9f16-add7fd2a10eb.png)

   
- **Shared library regions** are used to either statically/dynamically link libraries that are used by the program

- **The heap** increases and decreases dynamically depending on whether a program dynamically assigns memory. Notice there is a section that is unassigned above the heap which is used in the event that the size of the heap increases.

- The program code and data stores the program executable and initialised variables.


**Registers**


Functions take arguments. The example function takes 2 arguments(a and b). Upto 6 arguments for functions can be stored in the following registers:

    rdi
    rsi
    rdx
    rcx
    r8
    r9

Note: rax is a special register that stores the return values of the functions(if any).

If a function has anymore arguments, these arguments would be stored on the functions stack frame. 

We can now see that a caller function may save values in their registers, but what happens if a callee function also wants to save values in the registers? To ensure the values are not overwritten, the callee values first save the values of the registers on their stack frame, use the registers and then load the values back into the registers. The caller function can also save values on the caller function frame to prevent the values from being overwritten. Here are some rules around which registers are caller and callee saved:

    rax is caller saved
    rdi, rsi, rdx, rcx r8 and r9 are called saved(and they are usually arguments for functions)
    r10, r11 are caller saved
    rbx, r12, r13, r14 are callee saved
    rbp is also callee saved(and can be optionally used as a frame pointer)
    rsp is callee saved


**Called functions**

Caller vs callee: Caller is a function called by main. Callee is a function called by the caller.

Subroutines are implemented by using the CALL and RET instruction pair. 

CALL: pushes the current EIP to the stack and jumps to the function addr specified. When the function executes the RET instruction, the last element is POPped from the stack and the CPU jumps to the address. 

More info in the Stack section.













