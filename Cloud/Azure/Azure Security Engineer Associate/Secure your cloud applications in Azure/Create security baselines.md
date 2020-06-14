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

**Level 2** - Application options - Allow users to register apps**
Require administrators to register custom applications.


## Create an Azure Security Center baseline:






















