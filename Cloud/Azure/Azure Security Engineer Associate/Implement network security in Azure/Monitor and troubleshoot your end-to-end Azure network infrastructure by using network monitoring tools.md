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






