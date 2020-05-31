
Zero Trust model: Never assume trust, continue to validate it.

[Defense in depth:](https://docs.microsoft.com/en-us/learn/modules/azure-well-architected-security/2-defense-in-depth) Defense in depth is a strategy that employs a series of mechanisms to slow the advance of an attack aimed at acquiring unauthorized access to information. Each layer provides protection so that if one layer is breached, a subsequent layer is already in place to prevent further exposure. The common principles used to define a security posture is the CIA triad. Defense in depth can be visualized as a set of concentric rings, with the data to be secured at the center. Each ring adds an additional layer of security around the data. 

 
 Identity management: 
 
 - Single sign-on: With single sign-on, users only need to remember one ID and one password. Access across applications is granted to a single identity tied to a user, simplifying the security model. As users change roles or leave an organization, access modifications are tied to the single identity, greatly reducing the effort needed to change or disable accounts. Using single sign-on for accounts will make it easier for users to manage their identities, and will increase the security capabilities in your environment.
 
 
 Azure AD (SSO with Azure): cloud-based identity service. It has built-in support for synchronizing with your existing on-premises Active Directory or can be used stand-alone. By leveraging Azure AD for SSO, you'll also have the ability to combine multiple data sources into an intelligent security graph. This security graph enables the ability to provide threat analysis and real-time identity protection to all accounts in Azure AD, including accounts that are synchronized from your on-premises AD. By using a centralized identity provider, you'll have centralized the security controls, reporting, alerting, and administration of your identity infrastructure.
 

Azure AD Connect (replaces older versions of identity integration tools such as DirSync and Azure AD Sync. Can integrate on-premises directories with Azure Active Directory (i.e can basiaclly replicate groups, user, password hashes ETC from your AD to Azure and be able to SSO it between both.).

Azure AD supports MFA and Conditional access policies: 

- MFA: Requires two or more of the following elements:
    
    something you know
    something you possess
    something you are


- Conditional access policies: 

   Used along side MFA. Blocks logins from susicious IPs or denies access from devices without malware protection. Includes support for policies based on group, location, or device state.


**Azure AD App proxy:**
 Can quickly, easily, and securely allow the application to be accessed remotely without any code changes. Composed of two components: a connector agent that sits on a Windows server within your corporate network and an external endpoint, either the MyApps portal or an external URL. When a user navigates to the endpoint, they authenticate with Azure AD and are routed to the on-premises application via the connector agent.

Azure AD B2C provides a social identity login experience, while at the same time protecting your customer identity profile information. Azure AD B2C directories are distinct from standard Azure AD directories and can be created in the Azure portal.

## Infrastructure protection

 It is critical to ensure people and processes have only the rights they need to get their job done. Assigning incorrect access can result in data loss, data leakage, or cause services to become unavailable.
 
- RBAC (Role-based access control): Roles are defined as collections of access permissions. Security principals are mapped to roles directly or through group membership. Separating security principals, access permissions, and resources provides simplified access management and more fine-grained control.

   - On Azure, users, groups, and roles are all stored in Azure AD. The Azure Resource Manager API uses role-based access control to secure all resource access management within Azure.

Roles are a set of permissions. Roles can be granted at the individual service instance level, but they also flow down the Azure Resource Manager hierarchy. Roles assigned at a higher scope, like an entire subscription, are inherited by child scopes, like service instances.

Management groups are an additional hierarchical level in the RBAC model. Management groups add the ability to group subscriptions together and apply policy at an even higher level.

The ability to flow roles through an arbitrarily defined subscription hierarchy also allows administrators to grant temporary access to an entire environment for authenticated users. For example, an auditor may require temporary read-only access to all subscriptions.


## Privileged identity management

In additon to RBAC should be the ongoing auditing of role members as their organization changes and evolves. 

Azure AD Privileged Identity Management (PIM) ,additional $ offering that provides oversight of role assignments, self-service, and just-in-time role activation and Azure AD & Azure resource access reviews. Can manage, control, and monitor access to important resources in your organization. This includes access to resources in Azure AD; Azure; and other Microsoft Online Services, like Office 365 and Microsoft Intune. This control does not eliminate the need for users to carry out privileged operations in Azure AD, Azure, Office 365, and Software as a Service (SaaS) apps.

Key PIM features

    Providing just-in-time privileged access to Azure AD and Azure resources
    Assigning time-bound access to resources by using start and end dates
    Requiring approval to activate privileged roles
    Enforcing Azure Multi-Factor Authentication (MFA) to activate any role
    Using justification to understand why users activate
    Getting notifications when privileged roles are activated
    Conducting access reviews to ensure that users still need roles
    Downloading an audit history for an internal or external audit

To use PIM, you need one of the following paid or trial licenses:

    Azure AD Premium P2
    Enterprise Mobility + Security (EMS) E5


## Providing identities to services

Azure AD addresses the problem of credentials stored in configs that may be accessible through two methods: 

  Background: 

    - identity: a thing that can be authenticated. i.e a user to username / password. Can also be apps or other servers which might authenticate with secret keys or certs. An account is associated with an identity.

     - principle: Is an identity acting with certain roles or claims. example sudo, you are still logged in as the same identity, buy you have changed the role under which you are executing.

- service principals: An identity used by a service or app that can be assigned roles.

- managed identities for Azure services: A managed identity can be instantly created for any Azure service that supports it. When you create a managed identity for a service, you are creating an account on the Azure AD tenant. Azure infrastructure will automatically take care of authenticating the service and managing the account. You can then use that account like any other AD account including securely letting the authenticated service access other Azure resources.


## Encryption: 

Process of making data unreadable and unusable. It must be decrypted, which requires the use of a secret key. There are two top-level types of encryption: symmetric and asymmetric.

Symmetric encryption uses the same key to encrypt and decrypt the data. 

Asymmetric encryption uses a public key and private key pair. Either key can encrypt but cannot decrypt its own encrypted data. To decrypt, you need the paired key.

Encryption is typically approached in two ways: 

- encryption at rest: Data stored on a physical medium (disk, DB). Ensures that the stored data is unreadable without the keys and secrets needed to decrypt it. 

- encryption in transit:

 Data in transit is the data actively moving from one location to another (network). 

## Encryption on Azure: 

- Encrypt raw storage (Azure SSE): For data at rest.256-bit AES encrypt before data is persisted to disk and decrypted at retreival. Transparent to apps using this service, no need to add code or turn on features. Can use Microsoft-managed encryption keys with SSE, or you can use your own encryption keys by selecting the option in the Azure portal. SSE automatically encrypts data in: All Azure Storage services including Azure Managed Disks, Azure Blob storage, Azure Files, Azure Queue storage, and Azure Table storage, Both performance tiers (Standard and Premium) and Both deployment models (Resource Manager and classic).

    - SSE means that whenever they are using services that support storage service encryption, their data is encrypted on the physical medium of storage. 


- Encrypting VMs: 

Azure Disk Encryption (ADE) is a capability that helps you encrypt your VHD. ADE leverages the industry standard BitLocker feature of Windows and the DM-Crypt feature of Linux to provide volume encryption for the OS and data disks. The solution is integrated with Azure Key Vault to help you control and manage the disk-encryption keys and secrets (and you can use managed identity for Azure services for accessing the key vault).

When you apply the Disk Encryption management solution, you can satisfy the following business needs:

    IaaS VMs are secured at rest by using industry-standard encryption technology to address organizational security and compliance requirements.
    IaaS VMs boot under customer-controlled keys and policies. You can audit their usage in your key vault.

If you use Azure Security Center, you're alerted if you have VMs that aren't encrypted. The alerts display as High Severity, and the recommendation is to encrypt these VMs. Your organization can apply ADE to their virtual machines to be sure any data stored on VHDs is secured to their organizational and compliance requirements. Because boot disks are also encrypted, they can control and audit usage.

## Encrypting databases

TDE (Transparent data encryption) helps protect Azure SQL and Azure Data warehouse against the threat of malicious activity. 
  
   - Real time encryption / decryption of DB, associated backups, and transaction log files at rest
   - No changes to app
   - TDE is enabled by default
   - Encryption of DB using symmetric key called the DB Encryption Key. 
   - Default: Azure provides a unique encryption key per logical SQL Server and handles all the details
   - Bring-your-own-key is also supported with keys stored in Azure Key Vault.

   - For on premises MSSQL server DB: 
       - Turn on the SQL Server Always Encrypted feature. (protects column data at rest and transit by having the client app handle encryption/decryption outside the SQL server DB through an installed driver). 
       - This means the DB never works with unencryptied data.
       - The Always Encrypted client driver performs the actual encryption and decryption, rewriting the T-SQL queries as necessary to encrypt data passed to the DB and decrypt the results.
       - Transparent to the app
       
## Encrypting secrets (keys, passwords, strings, etc)

  - Azure Key Vault: secure secrets store.
  - Key vaults create multiple secure containers, called vaults that are backed by hardware security modules (HSMs). 
  - Vaults help reduce the chances of accidental loss of security information by centralizing the storage of application secrets. 
  - Key Vaults also control and log the access to anything stored in them. 
  - Azure Key Vault can handle requesting and renewing Transport Layer Security (TLS) certificates, providing the features required for a robust certificate lifecycle management solution. 
  - Key Vault is designed to support any type of secret. These secrets could be passwords, database credentials, API keys and, certificates.
  - Azure AD identities can be granted access to use Azure Key Vault secret
  - Key Vault for the storage of all their sensitive application information, including the TLS certificates they use to secure communication between systems.
        

## Encrypting backups  

- Data is stored encrypted at rest.
- local backups sing AES256 + key created by passphrase
- Data is transfered to Azure using HTTPS


# Network Security

- Securing traffic flow between applications and the internet focuses on limiting exposure outside your network.
- Securing traffic flow amongst applications focuses on data between applications and their tiers, between different environments, and in other services within your network. 
- Securing traffic flow between users and the application focuses on securing the network flow for your end users. 


## Layered approach to network security

Universal: 
  - Only needed ports are open
  - 

- Internet protection
   - perimeter
      - App layer 7 load balancer that includes a WAF
      - For none HTTP protection you can use a network virtual applicance (NVA). These are similar to firewall applicances and are available from many of the most popular network security vendors. NVAs can provide greater customization of security for applications. However are complex. 
      
       - Azure DOS protection.
       - Azure monitor metrics will notify you of attacks
       
 - Virtual network security (behind perimeter)
    - Limit comms between resources that only require it
    - Network security groups (operate at layer 3 and 4)
       - provide a list of allowed and denied communication to and from NICs and subnets.
       - Similar to VLANs (can isolate apps between env, tiers, and services.  
     - Virtual network service endpoints
        - To make Azure services only comm from virtual networks
        - Azure service resources can be secured to your virtual network
        - fully removes public internet access to resources and only allows traffic from your virtual net
       
  - Network integration 
     - From on-prem to Azure or between services. 
        - VPN between on-prem and Azure such as ExpressRoute. 
        - ExpressRoute allows connections to MS cloud services, Azure, Office 365, and Dynamics 365 to send traffic.
        - This make it so these cloud services can be access, but not just straight from the internet.
        - Integrate with virtual network peering, which est a direct conn between virtual networks
          - once integrated, can use network security groups to provide isolation between resources in the same way you would within a virtual network. 
        - Comm is only allowed between directly connected virtual networks


# Application security

- Cloud makes physical, building and host level attacks very difficult and have none rewarding returns.
- Attacks are going to be better against apps
- Security apps early through Security Dev Lifecycle (SDL)
-  once app has been deployed, continually evaluate its security posture, determine how to mitigate any issues that are discovered, and feed the knowledge back into the SDL.
- Security vulnerability scanning software services are available to help automate this process and assess security concerns on a regular cadence, without burdening teams with costly manual processes, such as pentest.
- Azure Security Center is a free service, now enabled by default for all Azure subscriptions, that is tightly integrated with other Azure application level services, such as Azure Application Gateway and Azure Web Application Firewall. By analyzing logs from these services, Security Center can report on known vulnerabilities in real time, recommend responses to mitigate them, and even be configured to automatically execute playbooks in response to attacks.

Restricting access to a web application by authenticating and authorizing sessions. Azure AD and Azure AD B2C offer an effective way to offload the responsibility of identity and access to a fully managed service. Azure AD conditional access policies, privileged identity management, and Identity Protection controls further enhance a customer's ability to prevent unauthorized access and audit changes.



