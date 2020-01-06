Always start with a hashbang 

#!/bin/bash


Legend: 
  
  - $1 = first user input argument

 ## For loops example
 
    for X in `seq 1 254`; do
    
    ping -c 1 $1.$X &
    
    done
    
  One line script
  
    for ip in $(cat iplist.txt); do namp -T4 $ip & done

 ## If else 
 
 
if [ $1 == "" ]   (example if userinput equals nothing)

then

else

fi
