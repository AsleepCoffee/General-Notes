**Registers:**

32 or 64 bit refers to the width of the CPU registers. Each CPU has its fixed set of registers that are accessed when required. They are like a temporary variable (small portion of memory in the CPU) used by the CPU to get and store data. 


The General Purpose Registers (GPRs): 

for x86 

<img width="1474" alt="Capture" src="https://user-images.githubusercontent.com/46513413/82863348-e552c280-9eef-11ea-8838-bb5a2c5c1887.PNG">


Naming conventions: 

8-bit CPU had 16-bit register divided into two parts: 

 - Low byte ID'd by an L at the end of the name
 
 - High byte, ID'd by and H at the end of the name

16-bit combines L and H and replaces it with an X. While for the Stack Pointer, Base Pointer, Source and Destination registers it simply removes the L. 

32-bit, the register acronym is prefixed with an E (extended). 

64-bit, the register acronym is prefixed with an R.

<img width="1477" alt="2" src="https://user-images.githubusercontent.com/46513413/82863791-0a940080-9ef1-11ea-87ce-4843199a2c97.PNG">


Another important register that is important is the EIP(Extended Instruction Pointer x86). It controls the program execution by storing a pointer to the address of the next instruction(machine code) that will be executed (i.e tells the CPU where the next instruction is).  


EIP - Points to the next instruction

ESP - points to the top of the stack




