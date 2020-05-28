
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












