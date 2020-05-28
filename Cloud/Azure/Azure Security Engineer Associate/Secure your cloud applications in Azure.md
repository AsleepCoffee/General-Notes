
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


