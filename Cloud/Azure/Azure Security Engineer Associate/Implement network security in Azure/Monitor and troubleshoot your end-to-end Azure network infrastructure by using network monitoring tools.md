# Troubleshoot a network by using Network Watcher monitoring and diagnostic tools

Azure Network Watcher includes several tools that you can use to monitor your virtual networks and VMs. To effectively make use of Network Watcher, it's essential to understand all the available options and the purpose of each tool.

Here, we'll look at the Network Watcher tool categories, the tools in each category, and how each tool is applied in example use cases.

What is Network Watcher?

Network Watcher is an Azure service that combines tools in a central place to diagnose the health of Azure networks. The Network Watcher tools are divided into two categories:

    Monitoring tools
    Diagnostic tools

With tools to monitor for and diagnose problems, Network Watcher gives you a centralized hub for identifying network glitches, CPU spikes, connectivity problems, memory leaks, and other issues before they affect your business.
Network Watcher monitoring tools

Network Watchers provides three monitoring tools:

    Topology
    Connection Monitor
    Network Performance Monitor

Let's look at each of these tools.
What is the topology tool?

The topology tool generates a graphical display of your Azure virtual network, its resources, its interconnections, and their relationships with each other.

Suppose you have to troubleshoot a virtual network created by your colleagues. Unless you were involved in the creation process of the network, you might not know about all the aspects of the infrastructure. You can use the topology tool to visualize and understand the infrastructure you're dealing with before you start troubleshooting.

You use the Azure portal to view the topology of an Azure network. In the Azure portal:

    On the Azure portal menu, select All services. Then go to Networking > Network Watcher.

    Select Topology.

    Select a subscription, the resource group of a virtual network, and then the virtual network itself.

    Note

    To generate the topology, you need a Network Watcher instance in the same region as the virtual network.



How to use the network watcher and diagnostic tools: https://docs.microsoft.com/en-us/learn/modules/troubleshoot-azure-network-infrastructure/3-exercise-troubleshoot-networking-with-network-watcher

Network watcher allows you to see the topology

1. Sign in to the Azure portal by using the account that you used to activate the sandbox.

2. On the Azure portal menu, select All services. Then go to Networking > Network Watcher.

3. Select Topology.

4. In the drop-down lists, select the subscription and resource group. Network Watcher displays your network topology


Use connection monitor to run tests. You can use this to run connection tests between VMs. 

1. Under Monitoring, select Connection Monitor, and then select + Add.

2. Configure Connection Monitor with the values you want to test, and then select Add

3. In the list of tests, select Back-to-front-RDP-test, select the ellipsis (...), and then select Start.

4. Examine the results.

use IP flow verify to test the connection.

1. Under Network diagnostic tools, select IP flow verify.

2. Configure the test with the same values as the tests you ran, and then select Check.

3. The results should show why there is an issue (if any).


## Troubleshoot a network by using Network Watcher metrics and logs

If you want to diagnose a problem quickly, you have to understand the information that's available in the Azure Network Watcher logs.

You want to ensure you know which information is available in which logs.

In this module, you'll focus on flow logs, diagnostic logs, and traffic analytics. You'll learn how these tools can help to troubleshoot the Azure network.

**Usage and quotas**

Each Microsoft Azure resource can be used up to its quota. Each subscription has separate quotas, and usage is tracked per subscription. Only one instance of Network Watcher is required per subscription per region. This instance gives you a view of usage and quotas so that you can see if you're at risk of hitting a quota.

To view the usage and quota information, go to All Services > Networking > Network Watcher, and then select Usage and quotas. You'll see granular data based on usage and resource location. Data for the following metrics is captured:

    Network interfaces
    Network security groups (NSGs)
    Virtual networks
    Public IP addresses

**Logs**

Network diagnostic logs provide granular data. To understand connectivity and performance issues better. There are three log display tools in Network Watcher:

    Flow logs
    Diagnostic logs
    Traffic analytics

Let's look at each of these tools.

*Flow logs*

In flow logs, you can view information about ingress and egress IP traffic on network security groups. Flow logs show outbound and inbound flows on a per-rule basis, based on the network adapter that the flow applies. NSG flow logs show whether traffic was allowed or denied based on the 5-tuple information captured. This information includes:

    Source IP
    Source port
    Destination IP
    Destination port
    Protocol

This diagram shows the workflow that the NSG follows:

![Capture](https://user-images.githubusercontent.com/46513413/90074269-d8f92d00-dcc8-11ea-8e0e-2d88b84299b2.PNG)

Flow logs store data in a JSON file. It can be difficult to gain insights into this data by manually searching the log files, especially if you have a large infrastructure deployment in Azure. You can solve this problem by using Power BI.

In Power BI, you can visualize NSG flow logs by (for example):

    Top talkers (IP address)
    Flows by direction (inbound and outbound)
    Flows by decision (allowed and denied)
    Flows by destination port

You can also use open-source tools to analyze your logs, such as Elastic Stack, Grafana, and Graylog.

Note: NSG flow logs don't support storage accounts on the Azure classic portal.

*Diagnostic logs*

In Network Watcher, diagnostic logs are a central place to enable and disable logs for Azure network resources. These resources might include NSGs, public IPs, load balancers, and application gateways. After you've enabled the logs that interest you, you can use the tools to query and view log entries.

You can import diagnostic logs into Power BI and other tools to analyze them.

*Traffic analytics*

Use traffic analytics to investigate user and application activity across your cloud networks.

The tool gives insights into network activity across subscriptions. You can diagnose security threats such as open ports, VMs communicating with known bad networks, and traffic flow patterns. Traffic analytics analyzes NSG flow logs across Azure regions and subscriptions. You can use the data to optimize network performance.

This tool requires Log Analytics. The Log Analytics workspace must exist in a supported region.

**Use case scenarios**

Now let's look at some use case scenarios where Azure Network Watcher metrics and logs can be helpful.
Customer reports of slow performance

To resolve slow performance, you need to determine the root cause of the problem:

    Is there too much traffic throttling the server?
    Is the VM size appropriate for the job?
    Are the scalability thresholds set appropriately?
    Are any malicious attacks happening?
    Is the VM storage configuration correct?

First, check that the VM size is appropriate for the job. Next, enable Azure Diagnostics on the VM to get more granular data for specific metrics, such as CPU usage and memory usage. To enable VM diagnostics via the portal, go to the VM, select Diagnostics Settings, and then turn on diagnostics.

Let's assume you have a VM that has been running fine. However, the VM's performance has recently degraded. To identify if you have any resource bottlenecks, you need to review the captured data.

Start with a time range of captured data before, during, and after the reported problem to get an accurate view of performance. These graphs can also be useful for cross-referencing different resource behaviors in the same period. You'll check for:

    CPU bottlenecks
    Memory bottlenecks
    Disk bottlenecks

CPU bottlenecks

When you're looking at performance issues, examine trends and understand if they affect your server. Use the monitoring graphs from the portal to spot trends. You might see different types of patterns on the monitoring graphs:

    Isolated spikes. A spike might be related to a scheduled task or an expected event. If you know what this task is, does it run at the required performance level? If the performance is OK, you might not need to increase capacity.
    Spike up and constant. A new workload might cause this trend. Enable monitoring in the VM to find out what processes cause the load. The increased consumption might be due to inefficient code or normal consumption. If the consumption is normal, does the process operate at the required performance level?
    Constant. Has your VM always been like this? If so, you should identify the processes that consume most resources and consider adding capacity.
    Steadily increasing. Do you see a constant increase in consumption? If so, this trend might indicate inefficient code or a process taking on more user workload.

If you do observe high CPU utilization, you can either:

    Increase the size of the VM to scale with more cores.
    Investigate the issue further. Locate the application and process, and troubleshoot accordingly.

If you scale up the VM and the CPU is still running at above 95 percent, is this offering better performance or higher application throughput to an acceptable level? If not, troubleshoot that individual application.
Memory bottlenecks

You can view the amount of memory that the VM uses. Logs will help you understand the trend and if it maps to the time at which you see issues. You should not have less than 100 MB of available memory at any time. Watch out for the following trends:

    Spike up and constant consumption. High memory utilization might not be the cause of bad performance. Some applications, such as relational database engines, are memory intensive by design. But if there are multiple memory-hungry applications, you might see bad performance because memory contention causes trimming and paging to disk. These processes will cause a negative performance impact.
    Steadily increasing consumption. This trend might be an application warming up. It's common when database engines start up. However, it might also be a sign of a memory leak in an application.
    Page or swap file usage. Check if you're using the Windows page file heavily, or the Linux swap file, located in /dev/sdb.

To resolve high memory utilization, consider these solutions:

    For immediate relief or page file usage, increase the size of the VM to add memory, and then monitor.
    Investigate the issue further. Locate that application or process and troubleshoot it. If you know the application, see if you can cap the memory allocation.

Disk bottlenecks

Network performance might also be related to the storage subsystem of the VM. You can investigate the storage account for the VM in the portal. To identify issues with storage, look at performance metrics from the storage account diagnostics and the VM diagnostics. Look for key trends when the issues occur within a particular time range.

    To check for Azure Storage timeout, use the metrics ClientTimeOutError, ServerTimeOutError, AverageE2ELatency, AverageServerLatency, and TotalRequests. If you see values in the TimeOutError metrics, an I/O operation took too long and timed out. If you see AverageServerLatency increase at the same time as TimeOutErrors, it might be a platform issue. Raise a case with Microsoft technical support.
    To check for Azure Storage throttling, use the storage account metric ThrottlingError. If you see throttling, you're hitting the IOPS limit of the account. You can check this problem by investigating the metric TotalRequests.

To remediate high disk utilization and latency issues:

    Optimize VM I/O to scale past virtual hard disk (VHD) limits.
    Increase throughput and reduce latency. If you find that you have a latency-sensitive application and require high throughput, migrate your VHDs to Azure Premium Storage.

Virtual machine firewall rules that block traffic

To troubleshoot an NSG flow issue, use the Network Watcher IP flow verify tool and NSG flow logging to determine whether an NSG or User Defined Routing (UDR) is interfering with traffic flow.

Run IP flow verify, and specify the local VM and the remote VM. After you select Check, Azure runs a logical test on rules in place. If the result is that access is allowed, use NSG flow logs.

In the portal, go to the NSGs. Under the flow log settings, select On. Now try to connect to the VM again. Use Network Watcher traffic analytics to visualize the data. If the result is that access is allowed, there's no NSG rule in the way.

If you've reached this point and still haven't diagnosed the problem, there might be something wrong on the remote VM. Disable the firewall on the remote VM, and then retest connectivity. If you can connect to the remote VM with the firewall disabled, verify the remote firewall settings. Then re-enable the firewall.
Inability of the front-end and back-end subnets to communicate

By default, all subnets can communicate in Azure. If two VMs on two subnets can't communicate, there must be a configuration that's blocking communication. Before you check the flow logs, run the IP flow verify tool from the front-end VM to the back-end VM. This tool runs a logical test on the rules on the network.

If the result is an NSG on the back-end subnet blocking all communication, reconfigure that NSG. For security purposes, you must block some communication with the front end because the front end is exposed to the public internet.

By blocking communication to the back end, you limit the amount of exposure in the event of a malware or security attack. However, if the NSG blocks everything, then it's incorrectly configured. Enable the specific protocols and ports that are required.


## Scenario 

In Azure Network Watcher, metrics and logs can diagnose complex configuration problems.

Suppose you have two virtual machines (VMs) that can't communicate. You want to obtain as much information as you can to diagnose the problem.

In this unit, you'll troubleshoot by using Network Watcher metrics and logs. You'll then use the network security group (NSG) flow logs to diagnose the connectivity issue between the two VMs.
Register the Microsoft.Insights provider

NSG flow logging requires the Microsoft.Insights provider. Complete the following steps to register for that provider.

    Sign in to the Azure portal and log in to the directory with access to the subscription you created resources in.

    In the Azure portal, search for and select Subscriptions. When Subscriptions appears in the search results, select it.

    Select the your subscription. Then under Settings, select Resource providers.

    In the search bar, enter microsoft.insights.

    If the status of the microsoft.insights provider is Unregistered, select Register.


Create a storage account

Now, create a storage account for the NSG flow logs.

    On the Azure portal menu or from the Home page, select Create a resource. Then select Storage > Storage account.
    
    On the Create storage account page, fill in the appropriate settings.

    Select Review + create, and then select Create.


Create a Log Analytics workspace

To view the NSG flow logs, you'll use Log Analytics. To install Log Analytics.

    In the Azure portal, search for and select Log analytics workspaces.

    Select + Add, complete the page with the correct values, and then select OK:

Enable flow logs

To set up flow logs, you must configure the NSG to connect to the storage account, and add traffic analytics for the NSG.

    On the Azure portal menu, select All resources. Then select the MyNSG network security group.

    Under Monitoring, select NSG flow logs.

    Select MyNSG, and then select On.

    Under Storage account, select Configure. In the Storage account drop-down list, select the storage account you created earlier. Then select OK.

    Under Traffic Analytics status, select On. Then in the Traffic Analytics processing interval drop-down list, select Every 10 mins.

    Select Log Analytics workspace, and then select testworkspace.

    Select Save.












