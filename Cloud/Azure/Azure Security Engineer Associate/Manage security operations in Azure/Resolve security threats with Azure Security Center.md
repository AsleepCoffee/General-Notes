**View security alerts**

Azure Security Center automatically collects, analyzes, and integrates log data from several sources to identify credible threats to your workloads. Data from your Azure resources, the network, and connected partner solutions (like firewalls) is correlated and processed with machine learning and advanced security analytics to reduce false positives.

This aggregation allows Security Center to detect threats such as:

    Compromised VMs communicating with known malicious IP addresses.
    Advanced malware detected by Windows error reporting.
    Brute-force attacks against VMs.
    Security alerts from integrated partner security solutions, such as anti-malware or web application firewalls.

When a threat like this is detected, Security Center will generate a security alert.

**What is a security alert?**

Alerts are the notifications that Security Center generates when it detects threats on your resources. Security Center prioritizes and lists the alerts, along with the information needed for you to investigate the problem quickly. Security Center also provides recommendations for how you can remediate an attack.

**Alert types and the Cyber Kill Chain**

Azure Security Center provides a variety of alerts that align with the stages of the cyber kill chain. The cyber kill chain is a series of steps that trace the stages of a cyberattack from the early reconnaissance stages to the exfiltration of data. The kill chain was created by Lockheed Martin and is modeled off a military framework established to identify and engage enemy targets.

The kill chain consists of eight phases as shown in the below image. Different types of attacks are associated with each stage, and they target various subsystems. All the common attack vectors from brute force logins to viruses and worms trigger activity on the cyber kill chain.

![Capture](https://user-images.githubusercontent.com/46513413/94746980-eedfb180-034b-11eb-9946-593ecaaeb0e3.PNG)


   1. Reconnaissance: The observation stage where attackers assess your network and services to identify possible targets and techniques to gain entry.
   2. Intrusion: Attackers use knowledge gained in the reconnaissance phase to get access to a part of your network. This often involves exploring a flaw or security hole.
   3. Exploitation: This phase involves exploiting vulnerabilities and inserting malicious code onto the system to get more access.
   4. Privilege Escalation: Attackers often try to gain administrative access to compromised systems so they can get access to more critical data and move into other connected systems.
   5. Lateral Movement: This is the act of moving laterally to connected servers and gain greater access to potential data.
   6. Obfuscation / Anti-forensics: To successfully pull off a cyberattack, attackers need to cover their entry. They will often compromise data and clear audit logs to try to prevent detection by any security team.
   7. Denial of Service: This phase involves disruption of normal access for users and systems to keep the attack from being monitored, tracked, or blocked.
   8. Exfiltration: The final extraction stage: getting valuable data out of the compromised systems.

Security Center alerts attempts to detect and recognize known behaviors in each phase of the kill chain and provide the SecOps team an opportunity to stop a cyberattack in progress. Post breach, Security Center can provide the necessary details to be able to identify the exfiltration and close off compromised systems.

The alerts contain valuable information about what triggered the alert, the resources targeted, and the source of the attack. The information included in an alert varies based on the type of analytics used to detect the threat. Incidents might also contain additional contextual information that might be useful during the investigation of a threat. To address attacks during these stages, Security Center has categories of alerts:

    Virtual machine behavioral analysis
    Network analysis
    SQL database and SQL Data Warehouse analysis
    Contextual information

These alerts are triggered when either a threat or suspicious activity takes place.

**Viewing security alerts**

You can view collected security alerts directly in Azure Security Center on the Overview page, through command-line tools, or using the REST API. The portal is the easiest way to view alerts - it displays a graph of your current alerts, colored by the severity level (high, medium, or low). Here's an example of a subscription with running resources being monitored.

https://docs.microsoft.com/en-us/learn/modules/resolve-threats-with-azure-security-center/media/6-security-center-dashboard-alert.png

Selecting the Threat protection tile presents more detailed information, as shown in the following image:

https://docs.microsoft.com/en-us/learn/modules/resolve-threats-with-azure-security-center/media/6-security-center-manage-alerts.png

You can filter alerts based on the date, state, and severity. Filtering alerts might be useful for scenarios where you need to narrow the scope of the security alerts. For example, you might want to address security alerts that occurred in the last 24 hours if you’re investigating a potential breach in the system.

If you have a lot of alerts, you can select Filter on the Security alerts page. The Filter area opens on the side, and you can choose the date, state, and severity values you want to see.

**Respond to alerts**

Once you have a set of alerts, you can select a security alert to learn more about the events that triggered it and what steps, if any, you need to take to repel an attack. Security alerts are grouped by type and date. Selecting a security alert opens a view containing a list of the grouped alerts, as the following figure depicts.

![Capture](https://user-images.githubusercontent.com/46513413/94748036-5b5bb000-034e-11eb-9cad-188ea846b658.PNG)

In this case, the alerts that were triggered refer to suspicious malware activity. The first column lists the attacked resources; the second displays how many times attack was detected. The third column indicates the time of the attack, the fourth displays the state of the alert, and the fifth displays the severity of the attack.

After reviewing this information, a security engineer can select an attacked resource to get specific information about:

    What happened? (Possible compromised machine detected)
    When did it happen? (Sunday, August 11 2019 3:01:00 AM)
    What resource was attacked? (vm4)
    Where is the resource located? (Azure)
    What should you do about it? (Remediation steps)

https://docs.microsoft.com/en-us/learn/modules/resolve-threats-with-azure-security-center/media/m3-asc-alerts4.png

**Responding to security alerts**

The DESCRIPTION area has more details about this event. These details offer insight into what triggered the security alert, the target resource, the source IP address (when applicable), and recommendations about how to remediate the event. In some cases, the source IP address is empty (not available), because not all Windows security event logs include the IP address.

The remediation steps suggested by Security Center vary according to the security alert. In some cases, you might have to use other Azure capabilities to implement the recommended remediation. For example, the remediation for this attack is to run a full malware scan on the machine.

From this page, you can also start an investigation to better understand the timeline of the attack, how the attack took place, which systems were potentially compromised, and which credentials were used, and you can get a graphical representation of the entire attack chain.

**Relating security alerts together**

Attacks against cloud-based resources often generate large amounts of data, and picking through all the individual alerts can be a cumbersome process to identify the root cause. As seen above, Security Center tracks individual security alerts, but it also uses big data and machine learning technologies to combine different alerts into incidents.

An incident is a collection of related individual alerts. Note that this combining of related alerts into incidents is an advanced capability of Security Center and requires at least the Standard tier for Azure Security Center.

By presenting related alerts together, a security engineer can quickly see the "big picture" of what's happening and start the process of blocking the attack.

**Define a security incident response plan**

Cyberattacks and security breaches are severe threats to your business. Every organization should have a prepared incident response plan to deal with security threats that impact their ability to provide service to customers, or jeopardize their ability to protect private/customer data.
What is an incident response plan?

An incident response plan (IRP) allows you to identify and minimize the damage, reduce the cost, and fix the cause of a security attack. A well-designed IRP provides step-by-step instructions for handling an incident and ensures that the security team responds using an established set of procedures, that the right people are involved, and that proper communication channels are informed.

**Establish an incident response team**

One of the essential steps of creating an IRP is to define a computer security incident response team (CSIRT). This team will consist of members from several areas of the company, including:

    Executive: There should be a representative of the executive leadership team that can communicate with and updates the board during and after the security incident.

    IT: The IT department should be involved in the creation and execution of any IRP.

    Communications: Different people in the company will need to be informed about the security incident, and it may become necessary to let customers or even the press know about significant data breaches. Members of the communications staff and PR team should be part of the response team to craft the communications.

    Legal: The legal department should be involved in the planning to ensure legal compliance and regulatory requirements for your data handling are met. They can also provide advice both during and after the incident has been addressed.

**Practice the plan**

Once an incident response plan has been defined, the CSIRT should run fire drills to test the plan thoroughly. This will help to identify gaps and trouble areas so they can be addressed before a real security threat emerges. The team has to respond quickly under pressure, so a clear, well-understood plan is a requirement.

**Revise the plan**

The incident response plan should be evaluated on a periodic basis to ensure it's still valid, identifies the correct parties to involve, and covers the primary threat areas defined for the company servers and data. In addition, each member of the CSIRT should periodically review the plan to ensure they understand their responsibilities during an incident and that when under pressure, they can respond efficiently.

**Phases of an incident response**

As mentioned earlier, the NIST defines a computer security incident guide that companies can use to craft a response plan. As part of that guide, they describe four primary phases of a security response that need to be planned out.

The following figure shows these four phases defined by the NIST. Note that the descriptions provided here are simple summaries - the overall document linked in the summary has more thorough descriptions of each phase and how you can plan a strategy.

![Capture](https://user-images.githubusercontent.com/46513413/94750420-015de900-0354-11eb-8d7d-48dff706dbad.PNG)



    Preparation. This phase includes defining the incident response team, documenting the response plan, and also scoping out tools and processes to help prevent incidents from occurring.

    Detection and Analysis. Security incidents come in many forms, and you can't plan for every possible contingency. However, there are common attack vectors that are well known, such as web-based and email-based attacks. These can easily be planned for, and in many cases, the response plan will incorporate standard communications and analysis. Tools such as Azure Security Center can help immensely in this area by providing a standard dashboard to detect and analyze inbound threats.

    Containment, Eradication & Recovery. Containment involves keeping the threat from growing or impacting other systems. Once it's contained, the response team can begin the steps to remove the threat altogether and then recover the affected systems. This step often involves a back-and-forth movement to the prior detection phase to ensure that the attack vector is truly mitigated and not simply moved to another system.

    Post-Incident activity. The final phase involves a post evaluation of the attack performed, the steps taken in response, and the effectiveness of the team's response. This will often lead to changes in the IRP and possible strengthening of the infrastructure to prevent future attacks of the same nature.


