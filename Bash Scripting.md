
Legend: 
  
  - $1 = user input argument

 ## For loops example
 
    for X in `seq 1 254`; do
    
    ping -c 1 $1.$X 
    done
