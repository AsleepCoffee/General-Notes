Azure doesn't monitor security or respond to security incidents within the customer's area of responsibility. Azure does provide many tools (such as Azure Security Center, Azure Sentinel) that are used for this purpose. Azure attempts make every service as secure as possible by default. Every service comes with a baseline that is already designed to help provide security for most common-use cases. Azure cannot predict how a service will be used, you should always review these security controls to evaluate whether they adequately mitigate risks.

## Understand the Azure platform security baseline

MS cybersec group + CIS dev best practises to help est sec baselines for Azure platform. 

Microsoft initially partnered with CIS for the development of an off-the-shelf hardened Azure VM. 

An initiative then began to use the CIS Benchmarks (their term for best practices) with Azure security services and tools to facilitate security and compliance for customer applications running on Azure services.

The [CIS MS Azure Foundations Security Benchmark](https://azure.microsoft.com/en-us/resources/cis-microsoft-azure-foundations-security-benchmark/) guide provides prescriptive guidance for establishing a secure baseline configuration for Azure. This guide was tested against the listed Azure services as of March 2018. The scope of this benchmark is to establish the foundational level of security for anyone adopting Azure.

**Create a platform security baseline**

A variety of security standards can help cloud service customers to achieve workload security when using cloud services. The following are recommended technology groupings to help create secure cloud-enabled workloads. These recommendations should not be considered an exhaustive list of all possible security configurations and architectures but just as a starting point.

CIS has two implementation levels, and several categories of recommendations.

    Level 1 - Recommended minimum security settings
        These should be configured on all systems.
        These should cause little or no interruption of services nor reduced functionality.

    Level 2 - Recommendations for highly secure environments:
        These might result in reduced functionality.

The following table provides the categories and number of recommendations made for each.

![azure](https://user-images.githubusercontent.com/46513413/83955864-9da03500-a825-11ea-9c14-b9c8c1b7bf30.PNG)

The following will examine each.

**Create an Identity & Access Management (IAM) baseline**

Identity management is key to granting access and to the security enhancement of corporate assets. To secure and control your cloud-based assets you must manage identity and access for your Azure administrators, application developers, and application users.

IAM recommendations

Here are the recommendations for identity and access management. Included with each recommendation are the basic steps to follow in the Azure portal. You should perform these steps on your own subscription with your own resources to validate the security for each. Keep in mind that Level 2 options might restrict some features or activity, so carefully consider which security options you decide to enforce.

Important

You must be an administrator for the Azure Active Directory to perform some of these checks.

**Level 1 - Restrict access to the Azure AD administration portal**
All non-Administrators should not have access due to the sensitive data and the rules of least privilege.

**Level 1 - About guests**
Ensure that no guest users exist, or alternatively if the business requires guest users, ensure to limit their permissions.

**Level 2 - Enable Azure Multi-Factor Authentication (MFA)**
Enable it for privileged and non-privileged users.

**Level 2 - Block remembering MFA on trusted devices**
Remember Multi-Factor Authentication feature for devices and browsers that are trusted by the user is a free feature for all Multi-Factor Authentication users. Users can bypass subsequent verifications for a specified number of days, after they've successfully signed-in to a device by using Multi-Factor Authentication. If an account or device is compromised, remembering Multi-Factor Authentication for trusted devices can negatively affect security.

**Password options**

Notify users on password resets - Level 1
Notify all admins when other admins reset passwords - Level 2
Require two methods to reset passwords - Level 1

With dual identification set, an attacker would require compromising both the identity forms before they could maliciously reset a user's password.

**Level 1 - Establish an interval for reconfirming user authentication methods**
If authentication reconfirmation is set to disabled, register users will never be prompted to re-confirm their authentication information.

**Level 2 - Members and guests can invite**
This should be set to No. Restricting invitations through administrators only ensures that only authorized accounts have access Azure resources.

**Level 2 - Users to create and manage security groups**
When this feature is enabled, all users in AAD are allowed to create new security groups. Security Group creation should be restricted to administrators.

**Level 2 - Self-service group management enabled**
Until your business requires this delegation to various users, it is a best practice to disable this feature.

**Level 2 - Application options - Allow users to register apps**
Require administrators to register custom applications.


## Create an Azure Security Center baseline:

Azure Security Center provides unified security management and ATP for workloads running in Azure, on-premises, and in other clouds. 

Azure Security Center recommendations

Included with each recommendation are the basic steps to follow in the Azure portal. Level 2 options might restrict some features or activity, so carefully consider which security options you decide to enforce.

**Enable the Standard pricing tier - Level 2**

ASC is offered in two pricing tiers, Free and Standard. The Standard tier extends the capabilities of the Free tier to workloads running in private and other public clouds, providing unified security management and threat protection across your hybrid cloud workloads. The Standard tier also adds advanced threat detection capabilities, which uses built-in behavioral analytics and machine learning to identify attacks and zero-day exploits, access and application controls to reduce exposure to network attacks and malware, and more. Azure Security Center Standard supports Azure resources including VMs, Virtual machine scale sets, App Service, SQL servers, threat detection provided with Microsoft Security Response Center, and Storage accounts.

**Enable the automatic provision of a monitoring agent - Level 1**

When automatic provisioning is enabled, Security Center installs the Microsoft Monitoring Agent on all supported Azure VMs and any new ones that are created. Automatic provisioning is strongly recommended.


**Enable System Updates - Level 1**

ASC monitors daily Windows and Linux virtual machines (VMs) and computers for missing operating system updates. Security Center retrieves a list of available security and critical updates from Windows Update, Windows Server Update Services (WSUS) (depending on how the windows machine is configured), and for Linux systems. If your VM or computer is missing a system update, Security Center will recommend that you apply system updates.

**Enable Security Configurations - Level 1**

ASC monitors security configurations by applying a set of over 150 recommended rules for hardening the OS, including rules related to firewalls, auditing, password policies, and more. If a machine is found to have a vulnerable configuration, Security Center generates a security recommendation.

 *Note:All of the following policies that have a* (*) *in their title are listed in the* **Security policies** *pane*
 
**Enable Endpoint Protection (*) - Level 1**

Endpoint protection is recommended for all virtual machines.

**Enable Disk Encryption (*) - Level 1**

ASC recommends that you apply disk encryption if you have Windows or Linux VM disks that are not encrypted using Azure Disk Encryption. Disk Encryption lets you encrypt your Windows and Linux IaaS VM disks. Encryption is recommended for both the OS and data volumes on your VM.

**Enable Network Security Groups (*) - Level 1**

Azure Security Center recommends that you enable a network security group (NSG) if one is not already enabled. NSGs contain a list of ACL rules that allow or deny network traffic to your VM instances in a Virtual Network. NSGs can be associated with either subnets or individual VM instances within that subnet. When an NSG is associated with a subnet, the ACL rules apply to all the VM instances in that subnet. In addition, traffic to an individual VM can be restricted further by associating an NSG directly to that VM.

**Enable Web Application Firewall (*) - Level 1**

Azure Security Center may recommend that you add a web application firewall (WAF) from a Microsoft partner to secure your web applications.

**Enable Vulnerability Assessment (*) - Level 1**

The vulnerability assessment in Azure Security Center is part of the Security Center virtual machine (VM) recommendations. If Security Center doesn't find a vulnerability assessment solution installed on your VM, it recommends that you install one. A partner agent, after being deployed, starts reporting vulnerability data to the partner's management platform. In turn, the partner's management platform provides vulnerability and health monitoring data back to Security Center.

**Enable Storage Encryption (*) - Level 1**

When this setting is enabled, any new data in Azure Blobs and Files will be encrypted.

**Enable JIT Network Access (*) - Level 1**

Just-in-time (JIT) virtual machine (VM) access can be used to lock down inbound traffic to your Azure VMs, reducing exposure to attacks while providing easy access to connect to VMs when needed.

**Enable Adaptive Application Controls (*) - Level 1**

Adaptive application control is an intelligent, automated end-to-end application whitelisting solution from Azure Security Center. It helps you control which applications can run on your Azure and non-Azure VMs (Windows and Linux), which, among other benefits, helps harden your VMs against malware. Security Center uses machine learning to analyze the applications running on your VMs and helps you apply the specific whitelisting rules using this intelligence. This capability greatly simplifies the process of configuring and maintaining application whitelisting policies.

**Enable SQL Auditing & Threat Detection (*) - Level 1**

ASC will recommend that you turn on auditing and threat detection for all databases on your Azure SQL servers if auditing is not already enabled. Auditing and threat detection can help you maintain regulatory compliance, understand database activity, and gain insight into discrepancies and anomalies that could indicate business concerns or suspected security violations.

**Enable SQL Encryption (*) - Level 1**

ASC will recommend that you enable Transparent Data Encryption (TDE) on SQL databases if TDE is not already enabled. TDE protects your data and helps you meet compliance requirements by encrypting your database, associated backups, and transaction log files at rest, without requiring changes to your application.

**Set Security Contact Email and Phone Number - Level 1**

ASC will recommend that you provide security contact details for your Azure subscription if you haven't already. This information will be used by Microsoft to contact you if the Microsoft Security Response Center (MSRC) discovers that your customer data has been accessed by an unlawful or unauthorized party. MSRC performs select security monitoring of the Azure network and infrastructure and receives threat intelligence and abuse complaints from third parties.

**Enable Send me emails about alerts - Level 1**

ASC will recommend that you provide security contact details for your Azure subscription if you haven't already.

**Enable Send email also to subscription owners - Level 1**

ASC will recommend that you provide security contact details for your Azure subscription if you haven't already.

## Create an Azure Storage accounts baseline

An Azure storage account provides a unique namespace to store and access your Azure Storage data objects.

Azure Storage account recommendations

Keep in mind that Level 2 options might restrict some features or activity.

**Require security-enhanced transfers - Level 1**

Another step you should take to ensure the security of your Azure Storage data is to encrypt the data between the client and Azure Storage. The first recommendation is to always use the HTTPS protocol, which ensures secure communication over the public Internet. You can enforce the use of HTTPS when calling the REST APIs to access objects in storage accounts by enabling Secure transfer required for the storage account. Connections using HTTP will be refused once this is enabled.

**Enable binary large object (blob) encryption - Level 1**

Azure Blob storage is Microsoft's object storage solution for the cloud. Blob storage is optimized for storing massive amounts of unstructured data. Unstructured data is data that does not adhere to a particular data model or definition, such as text or binary data. Storage service encryption protects your data at rest. Azure Storage encrypts your data as it's written in its datacenters, and automatically decrypts it for you as you access it.

**Periodically regenerate access keys - Level 1**

When you create a storage account, Azure generates two 512-bit storage access keys, which are used for authentication when the storage account is accessed. Rotating these keys periodically ensures that any inadvertent access or exposure to these keys could be undermined.

**Require Shared Access Signature (SAS) tokens to expire within an hour - Level 1**

A shared access signature (SAS) is a URI that grants restricted access rights to Azure Storage resources. You can provide a shared access signature to clients who should not be trusted with your storage account key but to whom you wish to delegate access to certain storage account resources. By distributing a shared access signature URI to these clients, you can grant them access to a resource for a specified period of time, with a specified set of permissions.
Currently verification of a SAS token expiry times cannot be accomplished. Until Microsoft makes token expiry time as a setting rather than a token creation parameter, this recommendation would require a manual verification.

**Require SAS tokens to be shared only via HTTPS - Level 1**

Shared access signature tokens should be allowed only over https protocol.

**Enable Azure Files encryption - Level 1**

Azure Disk Encryption is used to encrypt the OS and data disks in IaaS Virtual Machines. Client-side Encryption and SSE are both used to encrypt data in Azure Storage.

**Require only private access to blob containers - Level 1**

You can enable anonymous, public read access to a container and its blobs in Azure Blob storage. By doing so, you can grant read-only access to these resources without sharing your account key, and without requiring a shared access signature (SAS). By default, a container and any blobs within it may be accessed only by a user that has been given appropriate permissions. To grant anonymous users read access to a container and its blobs, you can set the container public access level. When you grant public access to a container, then anonymous users can read blobs within a publicly accessible container without authorizing the request.


## Create an Azure SQL Database baseline

Azure SQL Server is a cloud-based relational database server that supports many of the same features as Microsoft SQL Server. It provides an easy transition from an on-premises database into a cloud-based one with built-in diagnostics, redundancy, security and scalability.

Azure SQL Server recommendations

Keep in mind that Level 2 options might restrict some features or activity, so carefully consider which security options you decide to enforce.

**Enable auditing - Level 1**

Auditing for Azure SQL Database and SQL Data Warehouse tracks database events and writes them to an audit log in your Azure storage account, OMS workspace or Event Hubs. Auditing also:

    - Helps you maintain regulatory compliance, understand database activity, and gain insight into discrepancies and anomalies that could indicate business concerns or suspected security violations.
    - Enables and facilitates adherence to compliance standards, although it doesn't guarantee compliance.

**Enable a threat detection service - Level 1**

Threat detection for single and pooled databases detects anomalous activities indicating unusual and potentially harmful attempts to access or exploit databases. Threat detection can identify Potential SQL injection, Access from unusual location or data center, Access from unfamiliar principal or potentially harmful application, and Brute force SQL credentials. Threat detection is part of the advanced data security (ADS) offering, which is a unified package for advanced SQL security capabilities. Threat detection can be accessed and managed via the central SQL ADS portal.

**Enable all threat detection types - Level 1**

Advanced data security (ADS) provides a set of advanced SQL security capabilities, including data discovery & classification, vulnerability assessment, and Advanced Threat Protection (ATP).

Advanced Threat Protection is part of the advanced data security (ADS) offering, which is part of the defense in depth SQL security strategy. Advanced Threat Protection can be accessed and managed via the central SQL ADS portal.

**Enable the option to send security alerts - Level 1**

You can receive notifications about the detected threats via email notifications or Azure portal.

**Enable the email service and co-administrators - Level 1**

Providing the email address to receive alerts ensures that any detection of anomalous activities is reported as soon as possible, making it more likely to mitigate any potential risk sooner.

**Configure audit retention for more than 90 days - Level 1**

Audit logs should be preserved for security, discovery, and to meet legal and regulatory compliance.

**Configure threat detection retention for more than 90 days - Level 1**

A retention of zero days means logs are kept forever. Otherwise, the value can be any number of days between 1 and 2147483647. You should consider keeping the logs for at least 90 days to be able to go backwards to spot thread patterns.






