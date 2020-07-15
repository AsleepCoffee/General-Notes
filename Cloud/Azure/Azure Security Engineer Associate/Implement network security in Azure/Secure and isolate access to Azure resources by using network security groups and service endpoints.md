## Use network security groups to control network access

As part of the project to move your ERP system to Azure, you need to ensure that servers have proper isolation, so that only allowed systems can make network connections. For example, you have DB that store data for your ERP application. You want to block prohibited systems from communicating with the servers over the network, while allowing application servers to communicate with the database servers.

**Network security groups**

Network security groups filter network traffic to and from Azure resources. Network security groups contain security rules that you configure to allow or deny inbound and outbound traffic. You can use network security groups to filter traffic between virtual machines or subnets, both within a virtual network and from the internet.

**Network security group assignment and evaluation**

Network security groups are assigned to a network interface or a subnet. When you assign a network security group to a subnet, the rules apply to all network interfaces in that subnet. You can restrict traffic further by associating a network security group to the network interface of a virtual machine.

When you apply network security groups to both a subnet and a network interface, each network security group is evaluated independently. Inbound traffic is first evaluated by the network security group applied to the subnet, and then by the network security group applied to the network interface. Conversely, outbound traffic from a virtual machine is first evaluated by the network security group applied to the network interface, and then by the network security group applied to the subnet.

Applying a network security group to a subnet instead of individual network interfaces can reduce administration and management efforts. This approach also ensures that all virtual machines within the specified subnet are secured with the same set of rules.

Each subnet and network interface can have one network security group applied to it. Network security groups support TCP, UDP, and ICMP, and operate at Layer 4 of the OSI model.

In our manufacturing company scenario, network security groups can help you secure the network. You can control which computers can connect to your application servers. You configure the network security group so that only a specific range of IP addresses can connect to the servers. You can lock this down even more by only allowing access to or from specific ports, or from individual IP addresses. These rules can be applied to devices that are connecting remotely from on-premises networks, or between resources within Azure.

**Security rules**

A network security group contains one or more security rules. Configure security rules to either allow or deny traffic.

Rules have several properties:

![Capture](https://user-images.githubusercontent.com/46513413/87440785-5a717880-c5c0-11ea-98ea-f0c15c60ffc6.PNG)

Network security group security rules are evaluated by priority, using the 5-tuple information (source, source port, destination, destination port, and protocol) to allow or deny the traffic. When the conditions for a rule match the device configuration, rule processing stops.

For example, suppose your company has created a security rule to allow inbound traffic on port 3389 (RDP) to your web servers, with a priority of 200. Then suppose that another administrator has created a rule to deny inbound traffic on port 3389, with a priority of 150. The deny rule takes precedence, because it's processed first. The rule with priority 150 is processed before the rule with priority 200.

With network security groups, the connections are stateful. Return traffic is automatically allowed for the same TCP/UDP session. For example, an inbound rule allowing traffic on port 80 also allows the virtual machine to respond to the request (typically on an ephemeral port). You don't need a corresponding outbound rule.

With regard to the ERP system, the web servers for the ERP application connect to database servers that are in their own subnets. You can apply security rules to state that the only allowed communication from the web servers to the database servers is port 1433 for SQL Server database communications. All other traffic to the database servers will be denied.

The default rules for inbound traffic are:

**Default security rules**

When you create a network security group, Azure creates several default rules. These default rules can't be changed, but can be overridden with your own rules. These default rules allow connectivity within a virtual network and from Azure load balancers. They also allow outbound communication to the internet, and deny inbound traffic from the internet.

![Capture](https://user-images.githubusercontent.com/46513413/87441462-1d59b600-c5c1-11ea-952f-c572d08a50fb.PNG)

**Augmented security rules**

You use augmented security rules for network security groups to simplify the management of large numbers of rules. Augmented security rules also help when you need to implement more complex network sets of rules. Augmented rules let you add the following options into a single security rule:

    multiple IP addresses
    multiple ports
    service tags
    application security groups

Suppose your company wants to restrict access to resources in your datacenter, spread across several network address ranges. With augmented rules, you can add all these ranges into a single rule, reducing the administrative overhead and complexity in your network security groups.
Service tags

You use service tags to simplify network security group security even further. You can allow or deny traffic to a specific Azure service, either globally or per region.

Service tags simplify security for virtual machines and Azure virtual networks, by allowing you to restrict access by resources or services. Service tags represent a group of IP addresses, and help simplify the configuration of your security rules. For resources that you can specify by using a tag, you don't need to know the IP address or port details.

You can restrict access to many services. Microsoft manages the service tags (you can't create your own). Some examples of the tags are:

    VirtualNetwork - This tag represents all virtual network addresses anywhere in Azure, and in your on-premises network if you're using hybrid connectivity.
    
    AzureLoadBalancer - This tag denotes Azure's infrastructure load balancer. The tag translates to the virtual IP address of the host (168.63.129.16) where Azure health probes originate.
    
    Internet - This tag represents anything outside the virtual network address that is publicly reachable, including resources that have public IP addresses. One such resource is the Web Apps feature of Azure App Service.
   
    AzureTrafficManager - This tag represents the IP address for Azure Traffic Manager.
   
    Storage - This tag represents the IP address space for Azure Storage. You can specify whether traffic is allowed or denied. You can also specify if access is allowed only to a specific region, but you can't select individual storage accounts.
    
    SQL - This tag represents the address for Azure SQL Database, Azure Database for MySQL, Azure Database for PostgreSQL, and Azure SQL Data Warehouse services. You can specify whether traffic is allowed or denied, and you can limit to a specific region.
   
    AppService - This tag represents address prefixes for Azure App Service.

**Application security groups**

Application security groups let you configure network security for resources used by specific applications. You can group virtual machines logically, no matter what their IP address or subnet assignment.

Use application security groups within a network security group to apply a security rule to a group of resources. It's easier to deploy and scale up specific application workloads. You just add a new virtual machine deployment to one or more application security groups, and that virtual machine automatically picks up your security rules for that workload.

An application security group allows you to group network interfaces together. You can then use that application security group as a source or destination rule within a network security group.

For example, your company has a number of front-end servers in a virtual network. The web servers must be accessible over ports 80 and 8080. Database servers must be accessible over port 1433. You assign the network interfaces for the web servers to one application security group, and the network interfaces for the database servers to another application security group. You then create two inbound rules in your network security group. One rule allows HTTP traffic to all servers in the web server application security group. The other rule allows SQL traffic to all servers in the database server application security group.

Without application security groups, you'd need to create a separate rule for each virtual machine.

The key benefit of application security groups is that it makes administration easier. You can easily add and remove network interfaces to an application security group as you deploy or redeploy application servers. You can also dynamically apply new rules to an application security group, which are then automatically applied to all the virtual machines in that application security group.

**When to use network security groups**

As a best practice, you should always use network security groups to help protect your networked assets against unwanted traffic. Network security groups give you granular control access over the network layer, without the potential complexity of setting security rules for every virtual machine or virtual network.

## Create a virtual network and network security group

First, you'll create a resource group, the virtual network, and subnets for your server resources. You'll then create a network security group.

    Open the Azure Cloud Shell in your browser, and log in to the directory with access to the subscription you want to create resources in. Use the Bash version of Cloud Shell.

   Run the following command in the Cloud Shell to create a variable to store your resource group name, and a resource group for your resources. Replace <resource group name> with a name for your resource group, and <location> with the Azure region you'd like to deploy your resources in.
    Azure CLI

    rg=<resource group name>

    az group create --name $rg --location <location>

Run the following command in Azure Cloud Shell to create the ERP-servers virtual network and the Applications subnet.
Azure CLI

    az network vnet create \
        --resource-group $rg \
        --name ERP-servers \
        --address-prefix 10.0.0.0/16 \
        --subnet-name Applications \
        --subnet-prefix 10.0.0.0/24

Run the following command in Cloud Shell to create the Databases subnet.
Azure CLI

    az network vnet subnet create \
        --resource-group $rg \
        --vnet-name ERP-servers \
        --address-prefix 10.0.1.0/24 \
        --name Databases

Run the following command in Cloud Shell to create the ERP-SERVERS-NSG network security group.
Azure CLI

    az network nsg create \
        --resource-group $rg \
        --name ERP-SERVERS-NSG

**Create virtual machines running Ubuntu**

Next, you create two virtual machines called AppServer and DataServer. You deploy AppServer to the Applications subnet, and DataServer to the Databases subnet. Add the virtual machine network interfaces to the ERP-SERVERS-NSG network security group. Then use these virtual machines to test your network security group.

    Run the following command in Cloud Shell to build the AppServer virtual machine. Define a <password> for the admin account.
    Azure CLI

    wget -N https://raw.githubusercontent.com/MicrosoftDocs/mslearn-secure-and-isolate-with-nsg-and-service-endpoints/master/cloud-init.yml && \
    az vm create \
        --resource-group $rg \
        --name AppServer \
        --vnet-name ERP-servers \
        --subnet Applications \
        --nsg ERP-SERVERS-NSG \
        --image UbuntuLTS \
        --size Standard_DS1_v2 \
        --admin-username azureuser \
        --custom-data cloud-init.yml \
        --no-wait \
        --admin-password <password>

Run the following command in Cloud Shell to build the DataServer virtual machine. Define a <password> for the admin account.
Azure CLI

    az vm create \
        --resource-group $rg \
        --name DataServer \
        --vnet-name ERP-servers \
        --subnet Databases \
        --nsg ERP-SERVERS-NSG \
        --size Standard_DS1_v2 \
        --image UbuntuLTS \
        --admin-username azureuser \
        --custom-data cloud-init.yml \
        --admin-password <password>

It can take several minutes for the virtual machines to be in a running state. To confirm that the virtual machines are running, run the following command in Cloud Shell.
Azure CLI

    az vm list \
        --resource-group $rg \
        --show-details \
        --query "[*].{Name:name, Provisioned:provisioningState, Power:powerState}" \
        --output table

When virtual machine creation is complete, you should see the following output.
Output

    Name        Provisioned    Power
    ----------  -------------  ----------
    AppServer   Succeeded      VM running
    DataServer  Succeeded      VM running

**Check default connectivity**

Now, you'll try to open a Secure Shell (SSH) session to each of your virtual machines. Remember, so far you've deployed a network security group with default rules.

To connect to your virtual machines, use SSH directly from Cloud Shell. To do this, you need the public IP addresses that have been assigned to your virtual machines. Run the following command in Cloud Shell to list the IP addresses that you'll use to connect to the virtual machines.
    Azure CLI

    az vm list \
        --resource-group $rg \
        --show-details \
        --query "[*].{Name:name, PrivateIP:privateIps, PublicIP:publicIps}" \
        --output table

To make it easier to connect to your virtual machines during the rest of this exercise, assign the public IP addresses to variables. Run the following command in Cloud Shell to save the public IP address of AppServer and DataServer to a variable.
Bash

    APPSERVERIP="$(az vm list-ip-addresses \
                     --resource-group $rg \
                     --name AppServer \
                     --query "[].virtualMachine.network.publicIpAddresses[*].ipAddress" \
                     --output tsv)"

    DATASERVERIP="$(az vm list-ip-addresses \
                     --resource-group $rg \
                     --name DataServer \
                     --query "[].virtualMachine.network.publicIpAddresses[*].ipAddress" \
                     --output tsv)"

Run the following command in Cloud Shell to check whether you can connect to your AppServer virtual machine.
Bash

        ssh azureuser@$APPSERVERIP -o ConnectTimeout=5

You'll get a Connection timed out message.

Run the following command in Cloud Shell to check whether you can connect to your DataServer virtual machine.
Bash

    ssh azureuser@$DATASERVERIP -o ConnectTimeout=5

    You'll get the same connection failure message.

Remember that the default rules deny all inbound traffic into a virtual network, unless this traffic is coming from another virtual network. The Deny All Inbound rule blocked the inbound SSH connections you just attempted.

**Inbound**

Check default connectivity
Name 	Priority 	Source IP 	Destination IP 	Access
Allow VNet Inbound 	65000 	VIRTUAL_NETWORK 	VIRTUAL_NETWORK 	Allow
Deny All Inbound 	65500 	* 	* 	Deny
Create a security rule for SSH

As you've now experienced, the default rules in your ERP-SERVERS-NSG network security group include a Deny All Inbound rule. You'll now add a rule so that you can use SSH to connect to AppServer and DataServer.

Run the following command in Cloud Shell to create a new inbound security rule to enable SSH access.
    Azure CLI

    az network nsg rule create \
        --resource-group $rg \
        --nsg-name ERP-SERVERS-NSG \
        --name AllowSSHRule \
        --direction Inbound \
        --priority 100 \
        --source-address-prefixes '*' \
        --source-port-ranges '*' \
        --destination-address-prefixes '*' \
        --destination-port-ranges 22 \
        --access Allow \
        --protocol Tcp \
        --description "Allow inbound SSH"

Run the following command in Cloud Shell to check whether you can now connect to your AppServer virtual machine.
Bash

    ssh azureuser@$APPSERVERIP -o ConnectTimeout=5

The network security group rule might take a minute or two to take effect. If you receive a connection failure message, try again.

You should now be able to connect. After the Are you sure you want to continue connecting (yes/no)? message, type yes.

Enter the password you used when you created the virtual machine.

Type exit to close the AppServer session.

Run the following command in Cloud Shell to check whether you can now connect to your DataServer virtual machine.
Bash

    ssh azureuser@$DATASERVERIP -o ConnectTimeout=5

You should now be able to connect. After the Are you sure you want to continue connecting (yes/no)? message, type yes.

Enter the password you used when you created the virtual machine.

Type exit to close the DataServer session.

**Create a security rule to prevent web access**

Now add a rule so that AppServer can communicate with DataServer over HTTP, but DataServer can't communicate with AppServer over HTTP. These are the internal IP addresses for these servers:
Create a security rule to prevent web access
Server name 	IP address
AppServer 	10.0.0.4
DataServer 	10.0.1.4

 Run the following command in Cloud Shell to create a new inbound security rule to deny HTTP access over port 80.
    Azure CLI

    az network nsg rule create \
        --resource-group $rg \
        --nsg-name ERP-SERVERS-NSG \
        --name httpRule \
        --direction Inbound \
        --priority 150 \
        --source-address-prefixes 10.0.1.4 \
        --source-port-ranges '*' \
        --destination-address-prefixes 10.0.0.4 \
        --destination-port-ranges 80 \
        --access Deny \
        --protocol Tcp \
        --description "Deny from DataServer to AppServer on port 80"

**Test HTTP connectivity between virtual machines**

Here, you check if your new rule works. AppServer should be able to communicate with DataServer over HTTP. DataServer shouldn't be able to communicate with AppServer over HTTP.

Run the following command in Cloud Shell to connect to your AppServer virtual machine, and check if AppServer can communicate with DataServer over HTTP.
    Bash

    ssh -t azureuser@$APPSERVERIP 'wget http://10.0.1.4; exit; bash'

Enter the password you used when you created the virtual machine.

The response should include a 200 OK message.

Run the following command in Cloud Shell to connect to your DataServer virtual machine, and check if DataServer can communicate with AppServer over HTTP.
Bash

    ssh -t azureuser@$DATASERVERIP 'wget http://10.0.0.4; exit; bash'

Enter the password you used when you created the virtual machine.

This shouldn't succeed, because you've blocked access over port 80. After several minutes, you should get a Connection timed out message. Press Ctrl+C to stop the command prior to the timeo

**Deploy an application security group**

Next, create an application security group for database servers, so that all servers in this group can be assigned the same settings. You're planning to deploy more database servers, and want to prevent these servers from accessing application servers over HTTP. By assigning sources in the application security group, you don't need to manually maintain a list of IP addresses in the network security group. Instead, you assign the network interfaces of the virtual machines you want to manage to the application security group.


Run the following command in Cloud Shell to create a new application security group called ERP-DB-SERVERS-ASG.
Azure CLI

    az network asg create \
        --resource-group $rg \
        --name ERP-DB-SERVERS-ASG

Run the following command in Cloud Shell to associate DataServer with the application security group.
Azure CLI

    az network nic ip-config update \
        --resource-group $rg \
        --application-security-groups ERP-DB-SERVERS-ASG \
        --name ipconfigDataServer \
        --nic-name DataServerVMNic \
        --vnet-name ERP-servers \
        --subnet Databases

Run the following command in Cloud Shell to update the HTTP rule in the ERP-SERVERS-NSG network security group. It should reference the ERP-DB-Servers application security group.
Azure CLI

    az network nsg rule update \
        --resource-group $rg \
        --nsg-name ERP-SERVERS-NSG \
        --name httpRule \
        --direction Inbound \
        --priority 150 \
        --source-address-prefixes "" \
        --source-port-ranges '*' \
        --source-asgs ERP-DB-SERVERS-ASG \
        --destination-address-prefixes 10.0.0.4 \
        --destination-port-ranges 80 \
        --access Deny \
        --protocol Tcp \
        --description "Deny from DataServer to AppServer on port 80 using application security group"

**Test the updated HTTP security rule**

Run the following command in Cloud Shell to connect to your AppServer virtual machine, and check if AppServer can communicate with DataServer over HTTP.
    Bash

    ssh -t azureuser@$APPSERVERIP 'wget http://10.0.1.4; exit; bash'

Enter the password you used when you created the virtual machine.

As before, the response should include a 200 OK message. The application security group settings can take a minute or two to take effect. If you don't initially receive the 200 OK message, wait a minute and try again.

Run the following command in Cloud Shell to connect to your DataServer virtual machine, and check if DataServer can communicate with AppServer over HTTP.
Bash

    ssh -t azureuser@$DATASERVERIP 'wget http://10.0.0.4; exit; bash'

    Enter the password you used when you created the virtual machine.

 As before, this shouldn't succeed, because you've blocked access over port 80. After several minutes, you should get a Connection timed out message. Press Ctrl+C to stop the command prior to the timeout.

You've now confirmed that your network security group rule works using an application security group, in the same way as when you used a source IP address. If we were to add additional data servers, we can easily ensure they have the proper network security by adding the new servers to the ERP-DB-SERVERS-ASG.


## Secure network access to PaaS services with virtual network service endpoints

You've migrated your existing application and database servers for your ERP system to Azure as virtual machines. Now you're considering using some Azure platform as a service (PaaS) services to reduce your costs and administrative requirements. 
In this unit, you'll look at how to use virtual network service endpoints for securing supported Azure services.

**Virtual network service endpoints**

Use virtual network service endpoints to extend your private address space in Azure by providing a direct connection to your Azure services. Service endpoints let you secure your Azure resources to only your virtual network. Service traffic will remain on the Azure backbone, and doesn't go out to the internet.

By default, Azure services are all designed for direct internet access. All Azure resources have public IP addresses, including PaaS services such as Azure SQL Database and Azure Storage. Because these services are exposed to the internet, anyone can potentially access your Azure services.

Service endpoints can connect certain PaaS Services directly to your private address space in Azure, so they act like they’re on the same virtual network. You use your private address space to access the PaaS services directly. Adding service endpoints doesn't remove the public endpoint. It simply provides a redirection of traffic.

Azure service endpoints are available for many services, such as:

    Azure Storage
    Azure SQL Database
    Azure Cosmos DB
    Azure Key Vault
    Azure Service Bus
    Azure Data Lake

For a service like SQL Database, which can't be accessed until you add IP addresses to its firewall, service endpoints should still be considered. Using a service endpoint for SQL Database restricts access to specific virtual networks, providing greater isolation and reducing the attack surface.
How service endpoints work

To enable a service endpoint, you must do two things:

    Turn off public access to the service.
    Add the service endpoint to a virtual network.

When you enable a service endpoint, you restrict the flow of traffic, and allow your Azure virtual machines to access the service directly from your private address space. Devices cannot access the service from a public network. On a deployed virtual machine vNIC, if you look at Effective routes, you'll notice the service endpoint as the Next Hop Type.

This is an example route table, before enabling a service endpoint:

![Capture](https://user-images.githubusercontent.com/46513413/87553052-85230600-c680-11ea-8d01-285622723fc9.PNG)

All traffic for the service now is routed to the VirtualNetworkServiceEndpoint, and remains internal to Azure.

**Service endpoints and hybrid networks**

Service resources that you've secured by using virtual network service endpoints are not, by default, accessible from on-premises networks. To access resources from an on-premises network, use NAT IPs. If you use ExpressRoute for connectivity from on-premises to Azure, you have to identify the NAT IP addresses that are used by ExpressRoute. By default, each circuit uses two NAT IP addresses to connect to the Azure backbone network. You then need to add these IP addresses into the IP firewall configuration of the Azure service resource (for example, Azure Storage).

## Restrict access to Azure Storage by using service endpoints


As the solution architect, you're planning to move sensitive engineering diagram files into Azure Storage. The files must only be accessible from computers inside the corporate network. You want to create a virtual network service endpoint for Azure Storage to secure the connectivity to your storage accounts.

In this unit, you'll create a service endpoint, and use network rules to restrict access to Azure Storage. You'll create a virtual network service endpoint for Azure Storage on the Databases subnet. You'll then verify that your DataServer virtual machine can access Azure Storage. Finally, you'll check that the AppServer virtual machine, which is on a different subnet, can't access storage.

**Add rules to the network security group**

Ensure that communications with Azure Storage pass through the service endpoint. Add outbound rules to allow access to the Storage service, but deny all other internet traffic.

Run the following command in Azure Cloud Shell to create an outbound rule to allow access to Storage.
    Azure CLI

    az network nsg rule create \
        --resource-group $rg \
        --nsg-name ERP-SERVERS-NSG \
        --name Allow_Storage \
        --priority 190 \
        --direction Outbound \
        --source-address-prefixes "VirtualNetwork" \
        --source-port-ranges '*' \
        --destination-address-prefixes "Storage" \
        --destination-port-ranges '*' \
        --access Allow \
        --protocol '*' \
        --description "Allow access to Azure Storage"

Run the following command in Cloud Shell to create an outbound rule to deny all internet access.
Azure CLI

    az network nsg rule create \
        --resource-group $rg \
        --nsg-name ERP-SERVERS-NSG \
        --name Deny_Internet \
        --priority 200 \
        --direction Outbound \
        --source-address-prefixes "VirtualNetwork" \
        --source-port-ranges '*' \
        --destination-address-prefixes "Internet" \
        --destination-port-ranges '*' \
        --access Deny \
        --protocol '*' \
        --description "Deny access to Internet."

You should now have the following rules in ERP-SERVERS-NSG:

Rule name 	Direction 	Priority 	Purpose
AllowSSHRule 	Inbound 	100 	Allow inbound SSH
httpRule 	Inbound 	150 	Deny from DataServer to AppServer on 80
Allow_Storage 	Outbound 	190 	Allow access to Azure Storage
Deny_Internet 	Outbound 	200 	Deny access to Internet from VNet

At this point, both AppServer and DataServer have access to the Azure Storage service.
Configure storage account and file share

In this step, you'll create a new storage account, and then add an Azure file share to this account. This share is where you'll store your engineering diagrams.

 Run the following command in Cloud Shell to create a storage account for engineering documents.
  
  Bash

    STORAGEACCT=$(az storage account create \
                    --resource-group $rg \
                    --name engineeringdocs$RANDOM \
                    --sku Standard_LRS \
                    --query "name" | tr -d '"')

Run the following command in Cloud Shell to store the primary key for your storage in a variable.
Bash

    STORAGEKEY=$(az storage account keys list \
                    --resource-group $rg \
                    --account-name $STORAGEACCT \
                    --query "[0].value" | tr -d '"')

Run the following command in Cloud Shell to create an Azure file share called erp-data-share.
Azure CLI

    az storage share create \
        --account-name $STORAGEACCT \
        --account-key $STORAGEKEY \
        --name "erp-data-share"

**Enable the service endpoint**

You now need to configure the storage account to be accessible only from database servers, by assigning the storage endpoint to the Databases subnet. You then add a security rule to the storage account.

 Run the following command in Cloud Shell to assign the Microsoft.Storage endpoint to the subnet.
    Azure CLI

    az network vnet subnet update \
        --vnet-name ERP-servers \
        --resource-group $rg \
        --name Databases \
        --service-endpoints Microsoft.Storage

Run the following command to deny all access to change the default action to Deny. After network access is denied, the storage account is not accessible from any network.
Azure CLI

    az storage account update \
        --resource-group $rg \
        --name $STORAGEACCT \
        --default-action Deny

Run the following command in Cloud Shell to restrict access to the storage account. By default, storage accounts are open to accept all traffic. You want only traffic from the Databases subnet to be able to access the storage.
Azure CLI

    az storage account network-rule add \
        --resource-group $rg \
        --account-name $STORAGEACCT \
        --vnet ERP-servers \
        --subnet Databases

**Test access to storage resources**

In this step, you'll connect to both of your servers, and verify that only DataServer has access to the Azure file share on the storage account.

Run the following command in Cloud Shell to save the public IP addresses of AppServer and DataServer to variables.
    Bash

    APPSERVERIP="$(az vm list-ip-addresses \
                        --resource-group $rg \
                        --name AppServer \
                        --query "[].virtualMachine.network.publicIpAddresses[*].ipAddress" \
                        --output tsv)"

    DATASERVERIP="$(az vm list-ip-addresses \
                        --resource-group $rg \
                        --name DataServer \
                        --query "[].virtualMachine.network.publicIpAddresses[*].ipAddress" \
                        --output tsv)"

Run the following command in Cloud Shell to connect to your AppServer virtual machine, and attempt to mount the Azure file share.
Bash

    ssh -t azureuser@$APPSERVERIP \
        "mkdir azureshare; \
        sudo mount -t cifs //$STORAGEACCT.file.core.windows.net/erp-data-share azureshare \
        -o vers=3.0,username=$STORAGEACCT,password=$STORAGEKEY,dir_mode=0777,file_mode=0777,sec=ntlmssp; findmnt \
        -t cifs; exit; bash"

Enter the password you used when you created the virtual machine.

The response should include a mount error message. This connection isn't allowed, because there is no service endpoint for the storage account on the Applications subnet.

Run the following command in Cloud Shell to connect to your DataServer virtual machine, and attempt to mount the Azure file share.
Bash

    ssh -t azureuser@$DATASERVERIP \
        "mkdir azureshare; \
        sudo mount -t cifs //$STORAGEACCT.file.core.windows.net/erp-data-share azureshare \
        -o vers=3.0,username=$STORAGEACCT,password=$STORAGEKEY,dir_mode=0777,file_mode=0777,sec=ntlmssp;findmnt \
        -t cifs; exit; bash"

    Enter the password you used when you created the virtual machine.

 The mount should be successful, and the response should include details of the mount point. This is allowed because you created the service endpoint for the storage account on the Databases subnet.

You've now verified that DataServer can access storage, by using the storage service endpoint on the Databases subnet. You've also verified that AppServer can't access storage. This is because this server is on a different subnet, and doesn't have access to the virtual network service endpoint.


## Application Gateway and encryption

Transport encryption helps protect application data while it's in transit from users to your servers. This encryption prevents unauthorized users from seeing the transmitted data.

Consider the example of a retail organization that has a new shipping portal. The organization is publishing this portal and making it available over the internet to allow vendors to ship customer items and track status. This portal exposes business and customer data. The data needs to be encrypted between users and the backend application to ensure that it isn't captured by an unauthorized user while it's transmitted over the network. The organization has implemented Azure Application Gateway to load balance traffic. The organization now needs to enable SSL encryption between users and its servers.

Encrypting your data while it's in transit is an important step toward securing your applications. You can purchase certificates from a certificate authority and use them to encrypt the messages that pass in and out of your servers. This prevents unauthorized users from intercepting and examining the information in these messages while they're being transmitted.

In the shipping portal, encryption is important because we're dealing with shipping customer orders. If someone can access the transmitted data, they can view sensitive information, such as customer details or financial account data.

To help secure this data, you can use Azure Application Gateway. It encrypts data that's traversing the network from users to application servers.

Application Gateway and its benefits

Azure Application Gateway is an application delivery controller. It provides features such as load balancing HTTP traffic, web application firewall, and support for SSL encryption of your data. Application Gateway supports encrypting traffic between users and an application gateway, and between application servers and an application gateway.

When you terminate the SSL connection at the application gateway, it offloads the CPU-intensive SSL termination workload from your servers. Also, you don’t need to install certificates and configure SSL on your servers.

If you need end-to-end encryption, Application Gateway can decrypt the traffic on the gateway by using your private key and then re-encrypt again with the public key of the service running in the backend pool.

Exposing your website or web application through the application gateway also means that you don't directly connect your servers to the web. You're exposing only port 80 or port 443 on the application gateway. Your web servers aren't directly accessible from the internet, reducing the attack surface of your infrastructure.
Application Gateway components

Application Gateway has several components. The main parts for encryption are the frontend port, the listener, and the backend pool.

The following image shows how incoming traffic from a client to Application Gateway over SSL is decrypted and then re-encrypted when it's sent to a server in the backend pool.

Frontend port and listener

Traffic enters the gateway through a frontend port. You can open many ports, and Application Gateway can receive messages on any of these ports. A listener is the first thing that your traffic meets when entering the gateway through a port. It's set up to listen for a specific host name, and a specific port on a specific IP address. The listener can use an SSL certificate to decrypt the traffic that enters the gateway. The listener then uses a rule that you define to direct the incoming requests to a backend pool.

Backend pool

The backend pool contains your application servers. These servers might be virtual machines, a virtual machine scale set, or applications running on Azure App Service. Incoming requests can be load balanced across the servers in this pool. The backend pool has an HTTP setting that references a certificate used to authenticate the backend servers. The gateway re-encrypts the traffic by using this certificate before sending it to one of your servers in the backend pool.

If you're using Azure App Service to host the backend application, you don't need to install any certificates in Application Gateway to connect to the backend pool. All communications are automatically encrypted. Application Gateway trusts the servers because Azure manages them.

## Configure backend pools for encryption

The backend pool contains the servers that implement the application. Azure Application Gateway routes requests to these servers, and can load balance the traffic across these servers.

In the shipping portal, the application servers in the backend pool must use SSL to encrypt the data that passes between Application Gateway and the servers in the backend pool. Application Gateway uses an SSL certificate with a public key to encrypt the data. The servers use the corresponding private key to decrypt the data as it's received. In this unit, you'll see how to create the backend pool and install the necessary certificates in Application Gateway to help protect the messages that are transmitted to and from the backend pool.

Encryption from Application Gateway to the backend pool

A backend pool can reference individual virtual machines, a virtual machine scale set, the IP addresses of real computers (either on-premises or running remotely), or services hosted through Azure App Service. All the servers in the backend pool should be configured in the same way, including their security settings.

If the traffic directed to the backend pool is protected through SSL, each server in the backend pool must provide a suitable certificate. For testing purposes, you can create a self-signed certificate. In a production environment, you should always generate or purchase a certificate that a certificate authority (CA) can authenticate.

There are currently two versions of Application Gateway: v1 and v2. They have similar capabilities but have slightly different implementation details. The v2 version provides additional features and performance improvements.
Certificate configuration in Application Gateway v1

Application Gateway v1 requires that you install the authentication certificate for the servers in the gateway configuration. This certificate contains the public key that Application Gateway can use to encrypt messages and authenticate your servers. You can create this certificate by exporting it from the server. The application server uses the corresponding private key for decrypting these messages. This private key should be stored only on your application servers.

You can add an authentication certificate to Application Gateway by using the az network application-gateway auth-cert create command from the Azure CLI. The following example illustrates the syntax of this command. The certificate should be in CER (Claim, Evidence, and Reasoning) format.
Azure CLI

    az network application-gateway auth-cert create \
        --resource-group <resource group name> \
        --gateway-name <application gateway name> \
        --name <certificate name> \
        --cert-file <path to authentication certificate>

Application Gateway provides other commands that you can use to list and manage authentication certificates. For example:

    The az network application-gateway auth-cert list command shows the certificates that have been installed.
    The az network application-gateway auth-cert update command can be used to change the certificate.
    The az network application-gateway auth-cert delete command removes a certificate.

Certificate configuration in Application Gateway v2

Application Gateway v2 has slightly different authentication requirements. You provide the certificate for the certificate authority that has authenticated the SSL certificate for the servers in the backend pool. You add this certificate as a trusted root certificate to Application Gateway. Use the az network application-gateway root-cert create command from the Azure CLI.
Azure CLI

    az network application-gateway root-cert create \
          --resource-group <resource group name> \
          --gateway-name <application gateway name> \
          --name <certificate name> \
          --cert-file <path to trusted CA certificate>

If your servers are using a self-signed certificate, add this certificate as the trusted root certificate in Application Gateway.
HTTP settings

Application Gateway uses a rule to specify how to direct the messages that it receives on its incoming port to the servers in the backend pool. If the servers are using SSL, you must configure the rule to indicate:

That the servers expect traffic through the HTTPS protocol.
Which certificate to use to encrypt traffic and authenticate the connection to a server.

You define this configuration information by using an HTTP setting.

Define an HTTP setting by using the az network application-gateway http-settings create command in the Azure CLI. The following example shows the syntax for creating a setting that routes traffic by using the HTTPS protocol to port 443 on the servers in the backend pool. If you're using Application Gateway v1, the --auth-certs parameter is the name of the authentication certificate that you added to Application Gateway previously.
Azure CLI

    az network application-gateway http-settings create \
        --resource-group <resource group name> \
        --gateway-name <application gateway name> \
        --name <HTTPS settings name> \
        --port 443 \
        --protocol Https \
        --auth-certs <certificate name>

If you're using Application Gateway v2, omit the --auth-certs parameter. Application Gateway contacts the backend server. It verifies the authenticity of the certificate presented by the server against the CAs specified by a list of trusted root certificates. If there's no match, Application Gateway won't connect to the backend server and will fail with an HTTP 502 (Bad Gateway) error.

















