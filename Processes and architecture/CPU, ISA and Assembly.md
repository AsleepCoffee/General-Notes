**CPU:** device that executes machine code.

Machine code (machine language) is the set of instructions that the CPU processes. 

Each instruction is a primitiave command that executes a specific operation (i.e move data, change execution flow of program, perform arithmetic or logic operationns, etc). Instructions are rep in HEX. due to its complexity the machine code gets translated to a more readable language called assembly language (ASM). 

The two most popular ASM are NASM (Netwide Assembler) and MASM (Microsoft Macro Assembler). 

**ISA:** is the instruction set architectue for a specific CPU. It is the set of instructions that a programmger (or compiler) must understand and use to write a program correctly for that specific CPU and machine. It is what a programmer can see: memory, registers, instructions, etc. 

Types: 

x86 instruction set: Originated from the Intel 8086. Identifies 32 bit processors.

x64 (x86_64 or AMD64) identifies 64 bit processors.

**Registers:**

32 or 64 bit refers to the width of the CPU registers. Each CPU has its fixed set of registers that are accessed when required. They are like a temporary variable (small portion of memory in the CPU) used by the CPU to get and store data. 


The General Purpose Registers (GPRs): 

for x86 

<img width="1474" alt="Capture" src="https://user-images.githubusercontent.com/46513413/82863348-e552c280-9eef-11ea-8838-bb5a2c5c1887.PNG">


