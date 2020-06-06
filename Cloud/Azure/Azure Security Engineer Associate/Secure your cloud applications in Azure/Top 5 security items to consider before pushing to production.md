## Azure center

Helps you see all the areas you need to protect. 

A monitoring service that provides threat protection across all of your services both in Azure, and on-premises. It can:

-  Provide security recommendations based on your configurations, resources, and networks.
-  Monitor security settings across on-premises and cloud workloads and automatically apply required security to new services as they come online.
-  Continuously monitor all your services and perform automatic security assessments to identify potential vulnerabilities before they can be exploited.
-  Use machine learning to detect and block malware from being installed in your services and virtual machines. You can also allowlist applications to ensure that only the apps you validate are allowed to execute.
-  Analyze and identify potential inbound attacks and help to investigate threats and any post-breach activity which might have occurred.
-  Just-In-Time access control for ports, reducing your attack surface by ensuring the network only allows traffic you require.


Two tiers: 

- free: provides security policies, assessments, and recommendations. Limited to assessments and recommendations of Azure resources only.

- standard: a robust set of features, including 41threat intelligence.


## input and outputs 

Most revalent security weakness of applications is a failure to correctly process data that is received from external sources, particularly user input. Make sure it has been validated before it is used. Failing to analyze user input for possible attacks can result in data loss or exposure, elevation of privilege, or even execution of malicious code on other users' computers.

Always encode user output

Alwasys sanitize and validate input.

## Secrets in key vault

Secrets aren't secrets if they are shared with everyone. Never store confidential data, tokens , passwords, etc inside place such as web pages, web configs or any other places that are not properly protecting data at rest (no matter where the web pages are, its still not properly stored). 

Instead, you should always put these secrets into Azure Key Vault.

**Azure key vault**

Is a secret store. A centralized cloud service for storing application secrets. Key Vault keeps your confidential data safe by keeping application secrets in a single central location and providing secure access, permissions control, and access logging. Secrets are stored in individual vaults, each with their own configuration and security policies to control access. You can then get to your data through a REST API, or through a client SDK available for most languages.

Note: Key Vault is designed to store configuration secrets for server applications. It's not intended for storing data belonging to your app's users, and it shouldn't be used in the client-side part of an app. This is reflected in its performance characteristics, API, and cost model. User data should be stored elsewhere, such as in an Azure SQL database with Transparent Data Encryption, or a storage account with Storage Service Encryption. Secrets used by your application to access those data stores can be kept in Key Vault.

Key management and storing secrets can be complicated and error-prone when performed manually. Rotating certificates manually means potentially going without for a few hours, or days. As mentioned above, saving your connections strings in your configuration file or code repository means someone could steal your credentials.

Key Vault allows users to store connection strings, secrets, passwords, certificates, access policies, file locks (making items in Azure read-only), and automation scripts. It also logs access and activity, allows you to monitor access control (IAM) in your subscription, and it also has diagnostic, metrics, alerts and troubleshooting tools, to ensure you have the access you need.


## Framework updates

Framework that you choose is an important decision, from a design, and security perspective. Choosing a framework with modern security features and keeping it up-to-date is one of the best ways to ensure your apps are secure.

**Choosing the framework**

How well supported the framework is. The best frameworks have stated security arrangements and are supported by large communities who improve and test the framework. No software is 100% bug-free or totally secure, but when a vulnerability is identified, we want to be certain that it will be closed or have a workaround provided quickly.

Often "well supported" is synonymous with "modern". Older frameworks (potentually EoL and contains vulns) tend to either be replaced or eventually fade in popularity, as they should be replaces, no matter how much experience you have with it. Modern frameworks tend to build on the lessons learned by earlier iterations which makes choosing them for new apps a form of threat surface reduction.

More info: https://docs.microsoft.com/learn/modules/design-for-security-in-azure/

**Keep framework updated**

When we allow our frameworks to become out of date, it creates "technical debt". The further out of date we get, the harder and riskier it will be to bring our code up to the latest version. In addition, much like the initial framework choice, staying on older versions of the framework open you up to more security threats which have been fixed in newer releases of the framework.

**Advantage of built in security**

Always check to see what security features your frameworks offer. Never roll your own security if there's a standard technique or capability built in. In addition, rely on proven algorithms and workflows because these have often been scrutinized by many experts, critiqued and strengthened so you can be assured that they are reliable and secure.

Note: Writing your own security controls, instead of using those provided by your framework, is not only wasting time, it's less secure.

**Azure Security Center**

If you are using this to host web apps, security center will warn you if any frameworks are out of date in the recommendations tab. 


## Safe Dependancies

A large percentage of code present in modern applications are the libraries and dependencies chosen by you: the developer. This is a common practice that saves time and money. However, the downside is that you are now responsible for this code, even though others wrote it, because you used it in your project. If a researcher (or worse, a hacker) discovers a vulnerability in one of these 3rd party libraries, then the same flaw will likely also be present in your app.

Using components with known vulnerabilities is a huge problem in our industry. It is so problematic that is has made the OWASP top ten list of worst web application vulnerabilities, holding at #9 for several years.

**Track known security vulnerabilties**

The problem we have is knowing when an issue is discovered. Keeping our libraries and dependencies updated (#4 in our list!) will of course help, but it's a good idea to keep track of identified vulnerabilities that might impact your application.

Note: When a system has a known vulnerability, it is much more likely also to have exploits available, code that people can use to attack those systems. If an exploit is made public, it is crucial that any affected systems are updated immediately.

How to verify if you have known vulnerabilities in your 3rd party components

You could put a daily task into your phone to go and check this list, there are also many tools exist to allow us to verify if our dependencies are vulnerable. You can run these tools against your codebase, or better yet, add them to your CI/CD pipeline to automatically check for issues as part of the development process.

When you use libraries or other 3rd party components as part of your application you are also taking on any risks they may have. The best way to reduce this risk is to ensure that you are only using components that have no known vulnerabilities associated with them.
