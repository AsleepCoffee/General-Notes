## Explore Azure virtual networking

You have an on-premises datacenter that you plan to keep, but you want to use Azure to offload peak traffic using virtual machines (VMs) hosted in Azure. You want to keep your existing IP addressing scheme and network appliances, while ensuring that any data transfer is secure.
What is Azure virtual networking?

Azure virtual networks enable Azure resources, such as virtual machines, web apps, and databases, to communicate with: each other, users on the Internet, and on-premises client computers. You can think of an Azure network as a set of resources that links other Azure resources.

Azure virtual networks provide key networking capabilities:

    Isolation and segmentation
    Internet communications
    Communicate between Azure resources
    Communicate with on-premises resources
    Route network traffic
    Filter network traffic
    Connect virtual networks

**Isolation and segmentation**

Azure allows you to create multiple isolated virtual networks. When you set up a virtual network, you define a private Internet Protocol (IP) address space, using either public or private IP address ranges. You can then segment that IP address space into subnets, and allocate part of the defined address space to each named subnet.

For name resolution, you can use the name resolution service that's built in to Azure, or you can configure the virtual network to use either an internal or an external Domain Name System (DNS) server.

**Internet communications**

A VM in Azure can connect out to the Internet by default. You can enable incoming connections from the Internet by defining a public IP address or a public load balancer. For VM management, you can connect via the Azure CLI, Remote Desktop Protocol (RDP), or Secure Shell (SSH).

**Communicate between Azure resources**

You'll want to enable Azure resources to communicate securely with each other. You can do that in one of two ways:

    Virtual networks

    Virtual networks can connect not only VMs, but other Azure resources, such as the App Service Environment, Azure Kubernetes Service, and Azure virtual machine scale sets.

    Service endpoints

    You can use service endpoints to connect to other Azure resource types, such as Azure SQL databases and storage accounts. This approach enables you to link multiple Azure resources to virtual networks, thereby improving security and providing optimal routing between resources.

Communicate with on-premises resources

Azure virtual networks enable you to link resources together in your on-premises environment and within your Azure subscription, in effect creating a network that spans both your local and cloud environments. There are three mechanisms for you to achieve this connectivity:

    Point-to-site Virtual Private Networks

    This approach is like a Virtual Private Network (VPN) connection that a computer outside your organization makes back into your corporate network, except that it's working in the opposite direction. In this case, the client computer initiates an encrypted VPN connection to Azure, connecting that computer to the Azure virtual network.

    Site-to-site Virtual Private Networks A site-to-site VPN links your on-premises VPN device or gateway to the Azure VPN gateway in a virtual network. In effect, the devices in Azure can appear as being on the local network. The connection is encrypted and works over the Internet.

    Azure ExpressRoute

    For environments where you need greater bandwidth and even higher levels of security, Azure ExpressRoute is the best approach. Azure ExpressRoute provides dedicated private connectivity to Azure that does not travel over the Internet.

**Route network traffic**

By default, Azure will route traffic between subnets on any connected virtual networks, on-premises networks, and the Internet. However, you can control routing and override those settings as follows:

    Route tables: A route table allows you to define rules as to how traffic should be directed. You can create custom route tables that control how packets are routed between subnets.

    Border Gateway Protocol(BGP) works with Azure VPN gateways or ExpressRoute to propagate on-premises BGP routes to Azure virtual networks.

**Filter network traffic**

Azure virtual networks enable you to filter traffic between subnets by using the following approaches:

    Network security groups is an Azure resource that can contain multiple inbound and outbound security rules. You can define these rules to allow or block traffic, based on factors such as source and destination IP address, port, and protocol.

    Network virtual appliances is a specialized VM that can be compared to a hardened network appliance. A network virtual appliance carries out a particular network function, such as running a firewall or performing WAN optimization.

**Connect virtual networks**

You can link virtual networks together using virtual network peering. Peering enables resources in each virtual network to communicate with each other. These virtual networks can be in separate regions, allowing you to create a global interconnected network through Azure.

You can create and configure Azure virtual networks from the Azure portal, Azure PowerShell on your local computer, or Azure Cloud Shell.

**Create a virtual network**

When you create an Azure virtual network, you configure a number of basic settings. You'll have the option to configure advanced settings, such as multiple subnets, distributed denial of service (DDoS) protection, and service endpoints.

Screenshot of the Azure portal showing an example of the Create virtual network pane fields.

You'll configure the following settings for a basic virtual network:

    Network name must be unique in your subscription, but does not need to be globally unique. Make the name a descriptive one that is easy to remember and identified from other virtual networks.

    Address space, When you set up a virtual network, you define the internal address space in Classless Inter-Domain Routing (CIDR) format. This address space needs to be unique within your subscription and any other networks that you connect to.

    Let's assume, you choose an address space of 10.0.0.0/24 for your first virtual network. The addresses defined in this address space ranges from 10.0.0.1 - 10.0.0.254. You then create a second virtual network and choose an address space of 10.0.0.0/8. The address in this address space ranges from 10.0.0.1 - 10.255.255.254. Some of the address overlap and can't be used for the two virtual networks.

    However, you can use 10.0.0.0/16, with addresses ranging from 10.0.0.1 - 10.0.255.254, and 10.1.0.0/16, with addresses ranging from 10.1.0.1 - 10.1.255.254. You can assign these address spaces to your virtual networks since there's no address overlap.

    Note: You can add address spaces after creating the virtual network.

    Subscription only applies if you have multiple subscriptions to choose from.

    Resource group, like any other Azure resource, a virtual network needs to exist in a resource group. You can either select an existing resource group or create a new one.

    Location, Select the location where you want the virtual network to exist.

    Subnet

    Within each virtual network address range, you can create one or more subnets that partition the virtual network's address space. Routing between subnets will then depend on the default traffic routes, or you can define custom routes. Alternatively, you can define one subnet that encompasses all the virtual networks' address ranges.

    Note: Subnet names must begin with a letter or number, end with a letter, number or underscore, and may contain only letters, numbers, underscores, periods, or hyphens.

    Distributed Denial of Service (DDoS) protection, You can select either Basic or Standard DDoS protection. Standard DDoS Protection is a premium service. The Azure DDoS Protection Standard provides for more information on Standard DDoS protection.

    Service Endpoints. You enable service endpoints, and then select from the list which Azure service endpoints you want to enable. Options include Azure Cosmos DB, Azure Service Bus, Azure Key Vault, and so on.

When you have configured these settings, click the Create button.
Define additional settings

After creating a virtual network, you can then define further settings. These include:

    Network security group have security rules that enable you to filter the type of network traffic that can flow in and out of virtual network subnets and network interfaces. You create the network security group separately, and then associate it with the virtual network.

    Route table, Azure automatically creates a route table for each subnet within an Azure virtual network and adds system default routes to the table. However, you can add custom route tables to modify traffic between virtual networks.

You can also amend the service endpoints.

Screenshot of the Azure portal showing an example pane for editing virtual network settings.
Configure virtual networks

When you have created a virtual network, you can change any further settings from the Virtual Networks pane in the Azure portal. Alternatively, you can use PowerShell commands or commands in Cloud Shell to make changes.

Screenshot of the Azure portal showing an example pane for configuring a virtual network.

You can then review and change settings in further sub-panes. These settings include:

    Address spaces: You can add further address spaces to the initial definition

    Connected devices: Use the virtual network to connect machines

    Subnets: Add further subnets

    Peerings: Link virtual networks in peering arrangements

You can also monitor and troubleshoot virtual networks, or create an automation script to generate the current virtual network.

Virtual networks are powerful and highly configurable mechanisms for connecting entities in Azure. You can connect Azure resources to one another or to resources you have on-premises. You can isolate, filter and route your network traffic, and Azure allows you to increase security where you feel you need it.


## Create an Azure virtual network

**Create a resource group**

First, create a resource group to contain all of the resources you'll create in this module. Name it vm-networks and replace EastUS in the following command with the name of the region in which you'd like the group to be created.

    PowerShell

    $Location = "EastUS" 
    New-AzResourceGroup -Name vm-networks -Location $Location

**Create a subnet and virtual network**

To create a subnet and virtual network, run the following command.

    PowerShell

     $Subnet= New-AzVirtualNetworkSubnetConfig -Name default -AddressPrefix 10.0.0.0/24
     New-AzVirtualNetwork -Name myVnet -ResourceGroupName vm-networks -Location $Location -AddressPrefix 10.0.0.0/16 -Subnet $Subnet

**Create two virtual machines**

All Azure virtual machines are connected to a virtual network. If you create a virtual machine using Azure PowerShell and don't specify the name of an existing virtual network, Azure PowerShell creates a new virtual network automatically.

Here, we create two virtual machines and specify the virtual network.

To create the first virtual machine, run the following command to create a Windows VM with a public IP address that is accessible over port 3389 (Remote Desktop). This creates a Windows 2016 Datacenter VM named dataProcStage1 that uses the myVnet virtual network.
   
    PowerShell

    New-AzVm `
     -ResourceGroupName "vm-networks" `
     -Name "dataProcStage1" `
     -VirtualNetworkName "myVnet" `
     -SubnetName "default" `
     -image "Win2016Datacenter" `
     -Size "Standard_DS2_v2"

Port 3389 is opened automatically by default when you create a Windows VM in Azure.

Enter a user name and password for the VM. Write down user name and password. You need it later to sign in to the server.

Run the following command to get the public IP address for your VM so you can use it later. Copy the IpAddress.

    PowerShell

    Get-AzPublicIpAddress -Name dataProcStage1

    Create the second VM named dataProcStage2.
    PowerShell

    New-AzVm `
     -ResourceGroupName "vm-networks" `
     -Name "dataProcStage2" `
     -VirtualNetworkName "myVnet" `
     -SubnetName "default" `
     -image "Win2016Datacenter" `
     -Size "Standard_DS2_v2"

Enter a user name and password for the VM. Write down user name and password. You need it later to sign in to the server.

Disassociate the public IP address that was created by default for the VM.

    PowerShell

    $nic = Get-AzNetworkInterface -Name dataProcStage2 -ResourceGroup vm-networks
    $nic.IpConfigurations.publicipaddress.id = $null
    Set-AzNetworkInterface -NetworkInterface $nic 

Connect to dataProcStage1 using Remote Desktop

Open Remote Desktop and connect to dataProcStage1 with the public IP address you noted from the previous steps. If you're using PowerShell locally, use the following command and replace publicIpAddress with the VM's public IP address.
   
    PowerShell

    mstsc /v:publicIpAddress

Sign in to the remote machine with the username and the password you created.

In the remote session, open the Windows command prompt and run the following command:
   
    cmd

    ping dataProcStage2 -4

In the results, you'll see that all requests to dataProcStage2 time out. This is because the default Windows Firewall configuration on dataProcStage2 prevents it from responding to pings.

Connect to dataProcStage2 using Remote Desktop

Configure the Windows Firewall on dataProcStage2 using a new remote desktop session. You can't access dataProcStage2 from your desktop because dataProcStage2 doesn't have a public IP address. You'll use remote desktop from dataProcStage1 to connect to dataProcStage2.

In the dataProcStage1 remote session, open Remote Desktop.

Connect to dataProcStage2 by name. Based on the default network configuration, dataProcStage1 can resolve the address for dataProcStage2 using the computer name.

Sign in to dataProcStage2 with the username and the password you created.

On dataProcStage2, click the Start Menu, type Firewall, and press Enter. The Windows Firewall with Advanced Security console appears.

In the left-hand pane, click Inbound Rules.

In the right-hand pane, scroll down, and right-click File and Printer Sharing (Echo Request - ICMPv4-In), and then click Enable Rule.

Switch back to the dataProcStage1 remote session and run the following command in the command prompt.
    
    cmd

    ping dataProcStage2 -4

dataProcStage2 responds with four replies, demonstrating connectivity between the two VMs.

You successfully created a virtual network, created two VMs that are attached to that virtual network, connected to one of the VMs and shown network connectivity to the other VM within the same virtual network. You can use Azure Virtual Network to connect resources within the Azure network. However, those resources need to be within the same resource group and subscription. Next, we will look at VPN gateways, which enable you to connect virtual network in different resource groups, subscriptions, and even geographical regions.


## Explore Azure VPN Gateway

To integrate your on-premises environment with Azure, you need the ability to create an encrypted connection. You can connect over the Internet or over a dedicated link. Here, we'll look at Azure VPN Gateway, which provides an endpoint for incoming connections from on-premises environments.

You have set up an Azure virtual network and need to ensure that any data transfers from Azure to your site and between Azure virtual networks are encrypted. You also need to know how to connect virtual networks between regions and subscriptions.

**What is a VPN gateway?**

An Azure virtual network gateway provides an endpoint for incoming connections from on-premises locations to Azure over the Internet. A VPN gateway is a specific type of virtual network gateway that can be an endpoint for encrypted connections. It can also send encrypted traffic between Azure virtual networks over Microsoft's dedicated network that links Azure datacenters in different regions. This configuration allows you to link virtual machines and services in different regions securely.

Each virtual network can have only one VPN gateway. All connections to that VPN gateway share the available network bandwidth.

Within each virtual network gateway there are two or more virtual machines (VMs). These VMs have been deployed to a special subnet that you specify, called the gateway subnet. They contain routing tables for connections to other networks, along with specific gateway services. These VMs and the gateway subnet are similar to a hardened network device. You don't need to configure these VMs directly and should not deploy any additional resources into the gateway subnet.

Creating a virtual network gateway can take some time to complete, so it's vital that you plan appropriately. When you create a virtual network gateway, the provisioning process generates the gateway VMs and deploys them to the gateway subnet. These VMs will have the settings that you configure on the gateway.

A key setting is the gateway type. The gateway type determines the way the gateway functions. For a VPN gateway, the gateway type is "vpn". Options for VPN gateways include:

    Network-to-network connections over IPsec/IKE VPN tunneling, linking VPN gateways to other VPN gateways.

    Cross-premises IPsec/IKE VPN tunneling, for connecting on-premises networks to Azure through dedicated VPN devices to create site-to-site connections.

    Point-to-site connections over IKEv2 or SSTP, to link client computers to resources in Azure.

Now, let's look at the factors you need to consider for planning your VPN gateway.

**Plan a VPN gateway**

When you're planning a VPN gateway, there are three architectures to consider:

    Point to site over the Internet
    Site to site over the Internet
    Site to site over a dedicated network, such as Azure ExpressRoute

**Planning factors**

Factors that you need to cover during your planning process include:

    Throughput - Mbps or Gbps
    Backbone - Internet or private?
    Availability of a public (static) IP address
    VPN device compatibility
    Multiple client connections or a site-to-site link?
    VPN gateway type
    Azure VPN Gateway SKU

The following table summarizes some of these planning issues. The remainder are discussed later.

![Capture](https://user-images.githubusercontent.com/46513413/86923917-bb024080-c0fc-11ea-9e11-4a36168a1eb1.PNG)

**Gateway SKUs**

It's important that you choose the right SKU. If you have set up your VPN gateway with the wrong one, you'll have to take it down and rebuild the gateway, which can be time consuming. For the latest information about gateway SKUs, including throughput, see What is VPN Gateway? - Gateway SKUs.
Workflow

When designing a cloud connectivity strategy using virtual private networking on Azure, you should apply the following workflow:

    Design your connectivity topology, listing the address spaces for all connecting networks.

    Create an Azure virtual network.

    Create a VPN gateway for the virtual network.

    Create and configure connections to on-premises networks or other virtual networks, as required.

    If required, create and configure a point-to-site connection for your Azure VPN gateway.

**Design considerations**

When you design your VPN gateways to connect virtual networks, you must consider the following factors:

    Subnets cannot overlap

    It is vital that a subnet in one location does not contain the same address space as in another location.

    IP addresses must be unique

    You cannot have two hosts with the same IP address in different locations, as it will be impossible to route traffic between those two hosts and the network-to-network connection will fail.

    VPN gateways need a gateway subnet called GatewaySubnet

    It must have this name for the gateway to work, and it should not contain any other resources.

Create an Azure virtual network

Before you create a VPN gateway, you need to create the Azure virtual network.
Create a VPN gateway

The type of VPN gateway you create will depend on your architecture. Options are:

    RouteBased

    Route-based VPN devices use any-to-any (wildcard) traffic selectors, and let routing/forwarding tables direct traffic to different IPsec tunnels. Route-based connections are typically built on router platforms where each IPsec tunnel is modeled as a network interface or VTI (virtual tunnel interface).

    PolicyBased

    Policy-based VPN devices use the combinations of prefixes from both networks to define how traffic is encrypted/decrypted through IPsec tunnels. A policy-based connection is typically built on firewall devices that perform packet filtering. IPsec tunnel encryption and decryption are added to the packet filtering and processing engine.

**Set up a VPN gateway**

The steps you need to take will depend on the type of VPN gateway that you are installing. For example, to create a point-to-site VPN gateway by using the Azure portal, you would carry out the following steps:

    Create a virtual network

    Add a gateway subnet

    Specify a DNS server (optional)

    Create a virtual network gateway

    Generate certificates

    Add the client address pool

    Configure the tunnel type

    Configure the authentication type

    Upload the root certificate public certificate data

    Install an exported client certificate

    Generate and install the VPN client configuration package

    Connect to Azure

As there are several configuration paths with Azure VPN gateways, each with multiple options, it is not possible to cover every setup in this course. For more information, see the Additional Resources section.
Configure the gateway

Once your gateway is created, you'll need to configure it. There are several configuration settings you will need to provide, such as the name, location, DNS server, etc. We will go into these in more detail in the exercise.

Azure VPN gateways are a component in Azure virtual networks that enable point-to-site, site-to-site, or network-to-network connections. Azure VPN gateways enable individual client computers to connect to resources in Azure, extend on-premises networks into Azure, or facilitate connections between virtual networks in different regions and subscriptions.


## Create an Azure VPN gateway

You want to ensure that you can connect clients or sites within your environment into Azure using encrypted tunnels across the public Internet. In this unit, you'll create a point-to-site VPN gateway, and then connect to that gateway from your client computer. You'll use native Azure certificate authentication connections for security.

You will carry out the following process:

 Create a RouteBased VPN gateway.

 Upload the public key for a root certificate for authentication purposes.

 Generate a client certificate from the root certificate, and then install the client certificate on each client computer that will connect to the virtual network for authentication purposes.

 Create VPN client configuration files, which contain the necessary information for the client to connect to the virtual network.

**Setup**

To complete this module, use Azure PowerShell from your local Windows 10 computer.

Open a new PowerShell session on your local Windows 10 computer where you have the Azure PowerShell module installed.
Sign in to Azure by using the PowerShell cmdlet Connect-AzAccount.
Set up variables you'll use to create a virtual network. Copy and paste in the following variables into PowerShell.

    PowerShell

    $VNetName  = "VNetData"
    $FESubName = "FrontEnd"
    $BESubName = "Backend"
    $GWSubName = "GatewaySubnet"
    $VNetPrefix1 = "192.168.0.0/16"
    $VNetPrefix2 = "10.254.0.0/16"
    $FESubPrefix = "192.168.1.0/24"
    $BESubPrefix = "10.254.1.0/24"
    $GWSubPrefix = "192.168.200.0/26"
    $VPNClientAddressPool = "172.16.201.0/24"
    $ResourceGroup = "VpnGatewayDemo"
    $Location = "East US"
    $GWName = "VNetDataGW"
    $GWIPName = "VNetDataGWPIP"
    $GWIPconfName = "gwipconf"

Configure a virtual network

Run the following command to create a resource group.
   
    PowerShell

    New-AzResourceGroup -Name $ResourceGroup -Location $Location

Run the following command to create subnet configurations for the virtual network. These have the name FrontEnd, BackEnd, and GatewaySubnet. All of these subnets exist within the virtual network prefix.

    PowerShell

    $fesub = New-AzVirtualNetworkSubnetConfig -Name $FESubName -AddressPrefix $FESubPrefix
    $besub = New-AzVirtualNetworkSubnetConfig -Name $BESubName -AddressPrefix $BESubPrefix
    $gwsub = New-AzVirtualNetworkSubnetConfig -Name $GWSubName -AddressPrefix $GWSubPrefix

Next, run the following command to create the virtual network using the subnet values and a static DNS server.

    PowerShell

    New-AzVirtualNetwork -Name $VNetName -ResourceGroupName $ResourceGroup -Location $Location -AddressPrefix $VNetPrefix1,$VNetPrefix2 -Subnet $fesub, $besub, $gwsub -DnsServer 10.2.1.3

Now specify the variables for this network that you have just created.

    PowerShell

    $vnet = Get-AzVirtualNetwork -Name $VNetName -ResourceGroupName $ResourceGroup
    $subnet = Get-AzVirtualNetworkSubnetConfig -Name "GatewaySubnet" -VirtualNetwork $vnet

Run the following command to request a dynamically assigned public IP address.

    PowerShell

    $pip = New-AzPublicIpAddress -Name $GWIPName -ResourceGroupName $ResourceGroup -Location $Location -AllocationMethod Dynamic
    $ipconf = New-AzVirtualNetworkGatewayIpConfig -Name $GWIPconfName -Subnet $subnet -PublicIpAddress $pip

**Create the VPN gateway

When creating this VPN gateway:

    GatewayType must be Vpn
    VpnType must be RouteBased

Note that this part of the exercise can take up to 45 minutes to complete.

    To create the VPN gateway, run the following command and press Enter.
    PowerShell

    New-AzVirtualNetworkGateway -Name $GWName -ResourceGroupName $ResourceGroup `
    -Location $Location -IpConfigurations $ipconf -GatewayType Vpn `
    -VpnType RouteBased -EnableBgp $false -GatewaySku VpnGw1 -VpnClientProtocol "IKEv2"

    Wait for the command output to appear.

Add the VPN client address pool

    Run the following command to add the VPN client address pool.
    PowerShell

    $Gateway = Get-AzVirtualNetworkGateway -ResourceGroupName $ResourceGroup -Name $GWName
    Set-AzVirtualNetworkGateway -VirtualNetworkGateway $Gateway -VpnClientAddressPool $VPNClientAddressPool

    Wait for the command output to appear.

**Generate a client certificate**

With the network infrastructure created on Azure, we need to create a self-signed client certificate on our local machine. This can be done similarly on most operating systems, but we will cover how to generate your client certificate on Windows 10 using PowerShell with the Azure PowerShell module and the Windows Certificate Manager utility.

Our first step is to create the self-signed root certificate. Run the following command.

    PowerShell

    $cert = New-SelfSignedCertificate -Type Custom -KeySpec Signature `
    -Subject "CN=P2SRootCert" -KeyExportPolicy Exportable `
    -HashAlgorithm sha256 -KeyLength 2048 `
    -CertStoreLocation "Cert:\CurrentUser\My" -KeyUsageProperty Sign -KeyUsage CertSign

Next, generate a client certificate signed by your new root certificate.

      PowerShell

        New-SelfSignedCertificate -Type Custom -DnsName P2SChildCert -KeySpec Signature `
        -Subject "CN=P2SChildCert" -KeyExportPolicy Exportable `
        -HashAlgorithm sha256 -KeyLength 2048 `
        -CertStoreLocation "Cert:\CurrentUser\My" `
        -Signer $cert -TextExtension @("2.5.29.37={text}1.3.6.1.5.5.7.3.2")

Export certificate public key

With our certificates generated, we need to export our root certificate's public key.

    Run certmgr from PowerShell to open the Certificate Manager.

    Go to Personal > Certificates.

    Right-click the P2SRootCert certificate in the list and select All tasks > Export....

    In the Certificate Export Wizard, click Next.

    Ensure that No, do not export the private key is selected, and then click Next.

    On the Export File Format page, ensure that Base-64 encoded X.509 (.CER) is selected, and then click Next.

    In the File to Export page, under File name, navigate to a location you'll remember and save the file as P2SRootCert.cer, and then click Next.

    On the Completing the Certificate Export Wizard page, click Finish.

    On the Certificate Export Wizard message box, click OK.

Upload the root certificate public key information

In the PowerShell window, run the following command to declare a variable for the certificate name:
    
    PowerShell

    $P2SRootCertName = "P2SRootCert.cer"

Replace the <cert-path> placeholder with the export location of your root certificate and run the following command:

    PowerShell

    $filePathForCert = "<cert-path>\P2SRootCert.cer"
    $cert = new-object System.Security.Cryptography.X509Certificates.X509Certificate2($filePathForCert)
    $CertBase64 = [system.convert]::ToBase64String($cert.RawData)
    $p2srootcert = New-AzVpnClientRootCertificate -Name $P2SRootCertName -PublicCertData $CertBase64

With the group name set, upload the certificate to Azure with the following command.

    PowerShell

    Add-AzVpnClientRootCertificate -VpnClientRootCertificateName $P2SRootCertName -VirtualNetworkGatewayname $GWName -ResourceGroupName $ResourceGroup -PublicCertData $CertBase64

Azure will now recognize this certificate as a trusted root certificate for our virtual network.

Configure the native VPN client

    Run the following command to create VPN client configuration files in .ZIP format.
    PowerShell

    $profile = New-AzVpnClientConfiguration -ResourceGroupName $ResourceGroup -Name $GWName -AuthenticationMethod "EapTls"
    $profile.VPNProfileSASUrl

    Copy the URL returned in the output from this command and paste it into your browser. Your browser should start downloading a .ZIP file. Extract the archive contents and put them in a suitable location.

    Some browsers will initially attempt to block downloading this ZIP file as a dangerous download. You will need to override this in your browser to be able to extract the archive contents.

    In the extracted folder, navigate to either the WindowsAmd64 folder (for 64-bit Windows computers) or the WindowsX86 folder (for 32-bit computers).

    If you want to configure a VPN on a non-Windows machine, you can use the certificate and settings files from the Generic folder.

    Double-click on the VpnClientSetup{architecture}.exe file, with {architecture} reflecting your architecture.

    In the Windows protected your PC screen, click More info, and then click Run anyway.

    In the User Account Control dialog box, click Yes.

    In the VNetData dialog box, click Yes.

Connect to Azure

    Press the Windows key, type Settings and press Enter.

    In the Settings window, click Network and Internet.

    In the left-hand pane, click VPN.

    In the right-hand pane, click VNetData, and then click Connect.

    In the VNetData window, click Connect.

    In the next VNetData window, click Continue.

    In the User Account Control message box, click Yes.

If these steps do not work, you may need to restart your computer.
Verify your connection

    In a new Windows command prompt, run IPCONFIG /ALL.

    Copy the IP address under PPP adapter VNetData, or write it down.

    Confirm that IP address is in the VPNClientAddressPool range of 172.16.201.0/24.

    You have successfully made a connection to the Azure VPN gateway.

You just set up a VPN gateway, allowing you to make an encrypted client connection to a virtual network in Azure. This approach is great with client computers and smaller site-to-site connections.


## Explore Azure ExpressRoute

As your company deals with highly sensitive data and has large amounts of information it will store in Azure, there are some concerns about the security and reliability of connections over the public Internet. The company isn't willing to migrate wholesale to Azure unless it can demonstrate higher levels of connectivity, security, and reliability.

Here, we'll go beyond connections that run over the Internet to dedicated lines direct into the Azure datacenters.
Azure ExpressRoute

Microsoft Azure ExpressRoute enables organizations to extend their on-premises networks into the Microsoft Cloud over a private connection implemented by a connectivity provider. This arrangement means that the connectivity to the Azure datacenters doesn't go over the Internet but across a dedicated link. ExpressRoute also facilitates efficient connections with other Microsoft cloud-based services, such as Office 365 and Dynamics 365.

Advantages that ExpressRoute provides include:

    Faster speeds, from 50 Mbps to 10 Gbps, with dynamic bandwidth scaling

    Lower latency

    Greater reliability through built-in peering

    Highly secure

ExpressRoute brings a number of further benefits, such as:

    Connectivity to all supported Azure services

    Global connectivity to all regions (requires premium add-on)

    Dynamic routing over Border Gateway Protocol

    Service-level agreements (SLAs) for connection uptime

    Quality of Service (QoS) for Skype for Business

Additionally, there's the ExpressRoute premium add-on, which offers benefits such as increased route limits, global service connectivity, and increased virtual network links per circuit.
ExpressRoute connectivity models

Connections into ExpressRoute can be through the following mechanisms:

    IP VPN network (any-to-any)

    Virtual cross-connection through an Ethernet exchange

    Point-to-point Ethernet connection

ExpressRoute capabilities and features are all identical across all of the above connectivity models.

What is layer 3 connectivity?

Microsoft uses an industry-standard dynamic routing protocol (BGP) to exchange routes between your on-premises network, your instances in Azure, and Microsoft public addresses. We establish multiple BGP sessions with your network for different traffic profiles.

Any-to-any (IPVPN) networks

IPVPN providers typically provide connectivity between branch offices and your corporate datacenter over managed layer 3 connections. With ExpressRoute, the Azure datacenters appear as if they were another branch office.

Virtual cross-connection through an Ethernet Exchange

If your organization is co-located with a cloud exchange facility, you request cross-connections to the Microsoft Cloud through your provider's Ethernet exchange. These cross-connections to the Microsoft Cloud can operate at either layer 2 or layer 3 managed connections, as in the networking OSI model.

Point-to-point Ethernet connection

Point-to-point Ethernet links can provide layer 2 or managed layer 3 connections between your on-premises datacenters or offices to the Microsoft Cloud.

How ExpressRoute works

Azure ExpressRoute uses a combination of ExpressRoute circuits and routing domains to provide high-bandwidth connectivity to the Microsoft Cloud.

What are ExpressRoute circuits

An ExpressRoute circuit is the logical connection between your on-premises infrastructure and the Microsoft Cloud. A connectivity provider implements that connection, although some organizations use multiple connectivity providers for redundancy reasons. Each circuit has a fixed bandwidth of either 50, 100, 200 Mbps or 500 Mbps, or 1 Gbps or 10 Gbps, and each of those circuits map to a connectivity provider and a peering location. In addition, each ExpressRoute circuit has default quotas and limits.

An ExpressRoute circuit isn't equivalent to a network connection or a network device. Each circuit is defined by a GUID, called a service or s-key. This s-key provides the connectivity link between Microsoft, your connectivity provider, and your organization - it isn't a cryptographic secret. Each s-key has a one-to-one mapping to an Azure ExpressRoute circuit.

Each circuit can have up to three peerings, which are a pair of BGP sessions that are configured for redundancy. They are:

    Azure private
    Azure public
    Microsoft

Routing domains

ExpressRoute circuits then map to routing domains, with each ExpressRoute circuit having multiple routing domains. These domains are the same as the three peerings listed above. In an active-active configuration, each pair of routers would have each routing domain configured identically, thus providing high availability. The Azure public and Azure private peering names represent the IP addressing schemes.

Azure private peering

Azure private peering connects to Azure compute services such as virtual machines and cloud services that are deployed with a virtual network. As far as security goes, the private peering domain is simply an extension of your on-premises network into Azure. You then enable bidirectional connectivity between that network and any Azure virtual networks, making the Azure VM IP addresses visible within your internal network.

Note

You can connect only one virtual network to the private peering domain.

Azure public peering

Azure public peering enables private connections to services that are available on public IP addresses, such as Azure Storage, Azure SQL databases, and Azure web services. With public peering, you can connect to those service public IP addresses without your traffic being routed over the Internet. Connectivity is always from your WAN to Azure, not the other way around. This is also an all-or-nothing approach, as you can't select the services for which you want public peering enabled.

Note

For Azure PaaS services, it's recommended to use Microsoft peering rather than public peering.

Microsoft peering

Microsoft peering supports connections to cloud-based SaaS offerings, such as Office 365 and Dynamics 365. This peering option provides bi-directional connectivity between your company's WAN and Microsoft cloud services.

ExpressRoute health

As with most features in Microsoft Azure, you can monitor ExpressRoute connections to ensure that they are performing satisfactorily. Monitoring includes coverage of the following areas:

    Availability
    Connectivity to virtual networks
    Bandwidth utilization

The key tool for this monitoring activity is Network Performance Monitor, particularly NPM for ExpressRoute.

Azure ExpressRoute is used to create private connections between Azure datacenters and infrastructure on your premises or in a colocation environment. ExpressRoute connections don't go over the public Internet, and they offer more reliability, faster speeds, and lower latencies than typical Internet connections.

Azure offers three primary ways to set up virtual networking:

    Azure virtual networks
    Azure VPN gateways
    Azure ExpressRoute

Azure virtual networks can connect resources such as virtual machines and virtual machine scale sets within the same region, enabling them to communicate. 
Azure virtual networks can also connect to specified Azure service endpoints, such as Azure Storage, databases, and web apps.

Azure VPN gateways can enable communication with on-premises clients or networks over the public Internet, or connect virtual networks in different Azure regions. When you need a highly secure, dedicated route, you can use Azure ExpressRoute. It creates private, high-bandwidth connections to Azure datacenters that achieve the highest levels of reliability and security.


















