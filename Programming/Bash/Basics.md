## Environment

Upon the start of the shell, the operating system checks for the existence of several files like ~/.bashrc, ~/.bash_login or~/.bash_profile. These files may contain some instruction to help set up the environment properly. The same thing also happens when closing it, with the ~/.bash_logout file.



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

# Notes

Data between `` or $() will be evaluated before the whole statement and will become part of this statement
