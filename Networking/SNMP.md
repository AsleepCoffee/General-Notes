With SNMP there is a manager and a number of agents. The agents either wait for the commands from the manager or send critical messages (trap) to the manager. 

4 types of SNMP commands used to control and monitor managed devices: 

- Read (monitor devices)
- Write (used to config devices and change device settings)
- Trap (To "trap" events from the device and report back to the monitoring system)
- Traversal Operations (Used to determine what variables a certain device supports)


## Versions 

SNMPv1: original and most vulnerable. Clear text

SNMPv2: Also just as likely to be vulnerable. 

SNMPv3: Newest. Uses encryption, susceptible to attacks like brute forcing


## specs 

SNMP receives messages on UDP port 161 and trap messeges on UDP 162. Works on the bsis that network mgmt systems send out a req and the managed devices (agents) return a response. 

Uses 4 operations: Get, GetNext, Set, and Trap. 

SNMP messages of a header and PDU. The headers consist of the SNMP version number and the community string which is used as a form of "secure" password authentication in SNMP.

 2 types of community names or strings: Private and Public
 
   - Private community strings allow access to "Write" rights
   - Public allows for "read" rights on the system

PDU depends on the type of messages that is being sent.

Get, GetNext and Set as well the PDU responses consist of PDU type, Request ID, Error status, Error index, and Object/variable fields. 

Trap contains files like Enterprise, Agent,Agent address, Generic trap type, Specific trap code, Timestmap and Object/value.

MIBs (Management Information Base) are a collection of defenitions which define the properties of the managed object on the device (such as a router, switch, etc). is a DB of info that is relevant to the network manager. They a are organized as a tree, each object has a number and a name. The complete path from top to bottom is called an OID (Object Identifier). 




