Security Implementations developed to prevent or impede the exploitation of vulns such as Buffer Overflows. 

**ASLR (Address Space Layout Randomization):** Goal is to introduce randomness for executables, libraries, and stacks in the memory address  space. Makes it more difficult for an attacker to predict memory addresses and cuases exploits to fail and crash in the process. 

When ASLR is activated, the OS loads the same executable at different locations in memory every time. 

Note: ASLR is not enabled for all modules (.dll) meaning that even if a process has ASLR enabled, there could be a DLL in the address space without this protection which could make the process vulnerable to the ASLR bypass attack. 

Verify what programs are using ASLR with Process Explorer. 

You can also verify using mona:  !mona modules

**EMET(Enhanced Mitigation Experience Toolkit):** ability to deploy security mitigation technologies to all applications. 
   Offers things such as DEP, ASLR, SEHOP, and more: https://support.microsoft.com/en-us/kb/2458544. [Usermanual](https://www.microsoft.com/en-us/download/details.aspx?id=50802)

**DEP (Data Execution Prevention):** Defensive hardware and software measure that prevents the execution of code from pages in memory that that are not explicitly marked as executable. tje code injected intomemory cannot be run from that region. This makes buffer overflow exploitations even harder. 

**Stack Cookies (Canary):** Places a value next to the return address on the stack. The function prologue loads a value into this location, while the epiloague makes sure that the value is intact. As a result, when the epilogue runs, it checks the value is still there and that it is correct. If not a buffer overflow proabably taken place, this is BC a buffer overflow usually overwrites data in the stack. 

Purpose is to modify almost all the functions prologue and epilogue instructions in order to place a small random int value (canary) right before the return instruction, and detect if a buffer overflow occurs. When the function returns, the value is checked to make sure that it was not changed. If so, it means that a stack buffer overflow occurred. 

How it occurs:

 - The function prologue loads the random value in the canary location, and the epilogue makes sure that the value is not corrupted.
 
 

**ROP (Return-Oriented Programming)**

Consists of finding  multiple machine instructions in the program (called gadget), in order to create a chain of instructions that do something. Since the instructions are part of the stack, DEP does not apply to them. Gadgets are small groups of instructions that perform some operations (arithmetical operations on registers, check for conditional jumps, store / load data, etc) and that end with RET. RET is important, it will allow the chain to work and keep jumping to the next address after executing the small set of instructions. Purpose of the entire chain are different. Can use ROP gadgets to call a mem protection function that can be used to mark the stack as executable that will allow us to run the shellcode. Can also use ROP gadgets to execute direct command or copy data into executable regions and then jump to it. 
