# Intro

Azure offers several tools to help identify security issues, secure your services, and harden your exposed network.

Azure Security Center is one of the primary tools in Azure used to detect threats. It allows organizations to control and monitor the security of all of their running resources using intelligent threat detection to protect them from cyberattacks. As part of that threat detection, Security Center provides recommendations to close potential security holes and ensure compliance with your corporate policy and security guidelines.

Security Center provides an easy-to-read dashboard which shows compliance, security health, and security alerts. This is available right off the main Azure portal dashboard, or through the search window.

Azure Security Center pulls data from all your created resources. The level of detail presented will vary based on the running workloads in your subscription(s). This is particularly true in the Azure Sandbox which doesn't have any data.


# Explore the Azure Security Center service tiers

Free:

The free tier is automatically enabled on all Azure subscriptions and provides security policy, continuous security assessment, and actionable security recommendations to help you protect your Azure resources. It monitors the most common app resources in Azure including:

   - Compute resources such as VMs, Azure Functions and App Service
   - Network access and endpoint security
   - Data storage including Azure Storage, Redis cache for Azure, and Azure SQL
   - Identity and access including Azure Key Vault
   - IoT Hubs and resources


Standard: 

The standard tier extends the capabilities of the free tier to workloads running in private and other public clouds to provide unified security management and threat protection across all your hybrid cloud workloads.

The Standard tier adds advanced threat detection capabilities, using analytics and machine learning to identify attacks and zero-day exploits, access and application controls to reduce exposure to network attacks and malware, and more.

Migrating your Security Center subscription from the free tier to the standard tier enables the following features:

   - Security event collection. Security Center collects logs in a central place so you can search and analyze them to identify important security events that may require your attention.
   - Network Map. This feature allows you to visualize the topology of your Azure network infrastructure and the traffic to your Azure VMs. It also allows you to create filters by the severity level and recommendations.
   - Just-in-time VM access. This allows admins to grant access to a VM for a defined period of time. Limiting access helps reduce exposure to outside attacks. This feature is especially useful if you’re working with an outside agency that needs to access your VM.
   - Adaptive application controls (application whitelisting). Adaptive application controls uses artificial intelligence to recommend applications to allow. This helps protect VMs by preventing malware and unauthorized software from being installed.
   - Regulatory compliance reports. In the Regulatory compliance dashboard, you have a clear view of the status of all standard regulatory assessments within your environment.
   - File integrity monitoring. This feature examines files and registries of operating system, application software, and others in Windows and Linux (computers and VMs) for changes that might indicate an attack.
   - Adaptive Network Hardening. Adaptive Network Hardening provides recommendations to harden applied NSG rules. It uses machine learning algorithms that factors in actual traffic, known trusted configuration, threat intelligence, and other indicators of compromise, and then provides recommendations to allow traffic only from specific IP/port tuples.
   - Security alerts. Security Center supports a variety of security alerts such as detection of potential distributed denial-of-service (DDOS) attacks. Just-in-time alerts gives you the chance to investigate evolving issues before they result in a service failure.
   - Threat intelligence. This feature can help determine the nature of an attack, the attack point of origin, and more.
   - Workflow Automation. Workflow automation is a collection of procedures that can be executed from Security Center once a certain playbook is triggered from selected alert. Workflow automation can help to automate and orchestrate your response to a specific security alert detected by Security Center.

# Switch to the Standard tier

You can try the Standard tier for free for 30 days. This allows you to evaluate the additional features, see how your current environment will benefit from them, and decide whether they’re worth the investment.

You can enable Security Center on a per-subscription basis. Each subscription can choose what elements you want to enroll. Selecting the Coverage item under POLICY & COMPLIANCE will list all your available subscriptions (Not covered, Partially covered through the Free tier or partial plan, and Fully covered on the Standard tier).

Selecting a subscription allows you to control what areas you want Security Center to monitor as shown in the following screenshot.


# Customize Azure Security Center options

You can customize various global Azure Security Center settings using the Pricing & settings option on the Security Center menu. These settings are established on a per-subscription basis so you have complete control over what is monitored, what data is collected, and where it's stored.

There are four areas you can influence.

   - Pricing tier. Information about the available pricing tiers. This is the same information found on the Coverage page.
   - Threat detection. This lets you control how Security Center integrates with other Microsoft security services such as Windows Defender.
   - Data Collection. You can enable auto-provisioning to install a monitoring agent on all VMs in your subscription so Security Center can collect security information from Windows and Linux VMs.
    - Email notifications. Security contact details and email notifications for high security alerts.

Data Collection is particularly interesting. Each VM can store audit logs based on configured settings established during the VM creation process. You can collect two log sources from every VM in the subscription:

   1. Boot-time diagnostics. This includes console output and screenshots of the virtual machine running on a host to help diagnose startup issues.
   2. OS guest diagnostics. Get metrics every minute for your virtual machine. You can use them to create alerts and stay informed on your applications.

You can also activate these options when you create new VMs. These will be under the management tab when creating new virtual machines.

By default, a Storage Account will be selected (or created) to hold the logs, but you can customize that on a per-VM basis as needed.

With this collected data, Azure Security Center can start making observations about how each of your configured workloads match up to your security policy.


# Centralized policy management with Azure Security Center

Policy-based management can streamline IT operations and help to protect the organization by enforcing well-designed policies. Azure Policy lets you define requirements for your Azure subscriptions and tailor them to your type of workload or the sensitivity of your data.

Azure Security Center is fully integrated with Azure Policy. Security Center can monitor policy compliance across all of your subscriptions using a default set of security policies. A security policy defines the set of controls that are recommended for resources within the specified subscription or resource group. These security policies define the desired configuration of your workloads and help to ensure compliance with company or regulatory security requirements. These defaults can be customized and defined to match your specific organizational needs.

Here are a few of the built-in security policies that Security Center monitors:

   - Secure transfer to storage accounts should be enabled
   - Azure AD administrator for SQL server should be provisioned
   - Client authentication should use Azure Active Directory
   - Diagnostics logs in Key Vault should be enabled
   - System updates should be installed on your machines
   - Audit missing blob encryption for storage accounts
   - Just-In-Time network access control should be applied on virtual machines



















