When a program runs on a machine, the computer runs the program as a process. Current computer architecture allows multiple processes to be run at the same time by a computer. While these processes may appear to run at the same time, the computer actually switches between the processes very quickly and makes it look like they are running at the same time. Switching between processes is called a **context switch**. Since each process may need different information to run(e.g. The current instruction to execute), the operating system has to keep track of all the information in a process. The memory in the process is organised sequentially and has the following layout: 

![1](https://user-images.githubusercontent.com/46513413/80920034-36312a00-8d3b-11ea-9869-e135c17bd68b.png)

- **User stack** contains the information required to run the program. This information would include the current program counter, saved registers and more information. The section after the user stack is unused memory and it is used in case the stack grows(downwards). A program would usually comprise of multiple functions and there needs to be a way of tracking which function has been called, and which data is passed from one function to another. The stack is a region of contiguous memory addresses and it is used to make it easy to transfer control and data between functions. The top of the stack is at the lowest memory address and the stack grows towards lower memory addresses. The most common operations of the stack are: **Pushing:** used to add data onto the stack and **Popping:** used to remove data from the stack.

    push var

- **Shared library regions** are used to either statically/dynamically link libraries that are used by the program

- **The heap** increases and decreases dynamically depending on whether a program dynamically assigns memory. Notice there is a section that is unassigned above the heap which is used in the event that the size of the heap increases.

- The program code and data stores the program executable and initialised variables.


















