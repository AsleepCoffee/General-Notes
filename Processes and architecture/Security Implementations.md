Security Implementations developed to prevent or impede the exploitation of vulns such as Buffer Overflows. 

**ASLR (Address Space Layout Randomization):** Goal is to introduce randomness for executables, libraries, and stacks in the memory address  space. Makes it more difficult for an attacker to predict memory addresses and cuases exploits to fail and crash in the process. 

When ASLR is activated, the OS loads the same executable at different locations in memory every time. 

Note: ASLR is not enabled for all modules meaning that even if a process has ASLR enabled, there could be a DLL in the address space without this protection which could make the process vulnerable to the ASLR bypass attack. 

Verify what programs are using ASLR with Process Explorer. 

**EMET(Enhanced Mitigation Experience Toolkit):** ability to deploy security mitigation technologies to all applications. 

**DEP (Data Execution Prevention):** Defensive hardware and software measure that prevents the execution of code from pages in memory that that are not explicitly marked as executable. tje code injected intomemory cannot be run from that region. This makes buffer overflow exploitations even harder. 

**Stack Cookies (Canary):** Places a value next to the return address on the stack. The function prologue loads a value into this location, while the epiloague makes sure that the value is intact. As a result, when the epilogue runs, it checks the value is still there and that it is correct. If not a buffer overflow proabably taken place, this is BC a buffer overflow usually overwrites data in the stack. 
