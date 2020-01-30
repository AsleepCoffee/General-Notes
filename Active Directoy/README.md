# Active Directory 

Active directory stores information related to objects such as computers, users, printers, etc.

Authenticates using Kerberos with tickets. Accounts on active directory let you authenticate to any device in that active directory network.

The most commonly used identity management service used in the world.

Can exploit without any missing patches but with how active directory works and with bad policies. 


# Components 


**Domain controller**

  - Server with AD DS installed and promoted to DC. 
  
  - Host a copy of AD DS directory store
  
  - Provides authentication and authorization services
  
  - Replicate updates to other domain controllers in the domain and forest

  - Allow admin access to manage user accounts and network resources 


**AD DS Data Store**

  - Contains the database files and processes that store and manage directory information for users, services, and applications.
  
  - Contains the Ntds.dit file stored in %SystemRoot%\NTDS folder.
     - Contains all users, objects, and password hashes
        - This can lead to offline cracking, pass the hash, and golden ticket.

     - Is accessible only through the domain controller processes and protocols



 **AD DS Schema **
 
  - Defines types of objects that can be stored in the directory
  - Enforces rules regarding object creation and configuration. Like a rule book.
  
  
 **Domains**
     
     Example: MyComany.ca
 
 - What is used to group objects in a single org.
 
 - Administrative boundry for applying policies of groups
 
 - A replication boundry for replicating data between DCs
 
 - An authentication and authorization boundry that provides a way to limit the scope of access to resources
 
 
 
 **Trees**  
   
    Example: MyCompany.ca  -> dev.MyCompany.ca
                           
                           -> admin.MyCompany.ca
                           
                           -> user.MyCompany.ca
  
  - A hiearchy of domains in AD DS
  - Share namespace with parent domain
  - Can have additional child domains
  - By default create a two-way transitive trust with other domains
  
  
  **Forest**
  
  - A collection of one or more domain trees
  
  - Share a common schema
  
  - Share a common config partition
  
  - Share a common global catalog to enable searching
  
  - Enable trusts between all domains in the forest
  
  - Share the Enterprise Admins and Schema Admins group
  
  
  
 
 **Organizational Units (OUs)**
  
  - AD containers that can contain users, groups, computers, and other OUs.
  
  - Represent the ORG hierarchically and logically
  
  - Manage a collection of objects in a consistent way
  
  - Delegate permissions to administer groups of objects
  
  - Apply policies
  
  
  **Trusts**
  
  - Provides a way for users to gain access to resources in another domain
  
    - Directional Trust: One domain trusts another directly
    
    - Transitive Trust: Both trusting domains trust what the other domain trusts as well
         - Example: Trusting a domain at the top of a forest, will result in that domain trusting everything in that forest below it (that it trusts). 
  
  
  
 **Objects** 
 
 - What is inside OUs
 - Users, groups, contacts, computers, printers, shared folders. InetOrgPerson(Similar to user account, used for compatibility with other directory services)
  
  
  
  

