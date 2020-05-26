
<img width="893" alt="2" src="https://user-images.githubusercontent.com/46513413/82864109-bdfcf500-9ef1-11ea-89ac-1ac5276e1fce.PNG">


The Stack grows downward from high memory address to lower memory addresses. 
 
 *Note:* probably due to historical reasons when memory in old computers was limited and divided into tweo parts: heap and stack. It was decided that the Heap would start from the lower adresses and grow upwards and the Stack would start from the end of the memory and grow downwards.

The Stack is LIFO. the most fundamental operations are the PUSH and the POP. The main pointer for these operations is the ESP (stack pointer) which contains the memory address for the top fo the stack and changes during each PUSH and POP operation. 


**PUSH and POP operations**

PUSH: subtracts 4 (in 32-bit) or 8 (in 64-bit) from the ESP and writes the data to the memory addr in the ESP, then updates the ESP to the top of the stack. Since the stack grows backward the PUSH subtracts 4 or 8 in order to point to a lower memory location on the stack. If we do not subtract it, the PUSH operation will overwrite the current location pointed by ESP and we would lose data. 

  ESP = a memory location. We want to PUSH a value into the stack. We will subtract the memory needed from the top of the stack and subtract that value from the ESP so the ESP points to a lower point in memory as the top of the stack. 



















