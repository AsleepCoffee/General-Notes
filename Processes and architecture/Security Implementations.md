Security Implementations developed to prevent or impede the exploitation of vulns such as Buffer Overflows. 

**ASLR (Address Space Layout Randomization):** Goal is to introduce randomness for executables, libraries, and stacks in the memory address  space. Makes it more difficult for an attacker to predict memory addresses and cuases exploits to fail and crash in the process. 

When ASLR is activated, the OS loads the same executable at different locations in memory every time. 

Note: ASLR is not enabled for all modules meaning that even if a process has ASLR enabled, there could be a DLL in the address space without this protection which could make the process vulnerable to the ASLR bypass attack. 

Verify what programs are using ASLR with Process Explorer. 

**DEP (Data Execution Prevention):**

**Stack Cookies (Canary):**
