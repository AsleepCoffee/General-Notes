IP protocol implements a Framentation ID header that many OS increase by 1 (for each packet). 

If encapsulated data for network transmission is to large it will be split into smaller messages (fragmented).
Wehn a device sends fragments of a message, the receiver must be able to identify these fragments in order to reassemble them. 
Done by assigning a unique ID to each fragment caled the fragmentation ID. So the receiver knows the correct SEQ of the fragments so they can be reassembled. 




























