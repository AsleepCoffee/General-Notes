# Explore the different alert types that Azure Monitor supports

Azure Monitor is a powerful reporting and analytics tool. Use it for insights into the behavior and running of your environment and applications. You can then respond proactively to faults in your system.

After the downtime that your customers faced, you set up monitoring on your key resources in Azure. With the monitoring in place, you want to make sure the right people are being alerted, at the right level.

In this unit, you'll see how Azure Monitor receives resource data, what makes up an alert, and how and when to use an alert. Finally, you'll learn how to create and manage your own alerts.

# Data types in Azure Monitor

Azure Monitor receives data from target resources like applications, operating systems, Azure resources, Azure subscriptions, and Azure tenants. The nature of the resource defines which data types are available. A data type will be a metric, a log, or both a metric and a log.

    The focus for metric-based data types is the numerical time-sensitive values that represent some aspect of the target resource.
    The focus for log-based data types is the querying of content data held in structured, record-based log files that are relevant to the target resource.


https://docs.microsoft.com/en-us/learn/modules/incident-response-with-alerting-on-azure/media/2-azure-resource-signal-types.svg

You'll learn about the three signal types that you can use to monitor your environment:

    Metric alerts provide an alert trigger when a specified threshold is exceeded. For example, a metric alert can notify you when CPU usage is greater than 95 percent.
    Activity log alerts notify you when Azure resources change state. For example, an activity log alert can notify you when a resource is deleted.
    Log alerts are based on things written to log files. For example, a log alert can notify you when a web server has returned a number of 404 or 500 responses.

Composition of an alert rule

https://docs.microsoft.com/en-us/learn/modules/incident-response-with-alerting-on-azure/media/2-creating-an-alert.png


Every alert or notification available in Azure Monitor is the product of a rule. Some of these rules are built into the Azure platform. You use alert rules to create custom alerts and notifications. No matter which target resource or data source you use, the composition of an alert rule remains the same.

    RESOURCE
        The target resource to be used for the alert rule. It's possible to assign multiple target resources to a single alert rule. The type of resource will define the available signal types.
    CONDITION
        The signal type to be used to assess the rule. The signal type can be a metric, an activity log, or logs. There are others, but this module doesn't cover them.
        The alert logic applied to the data that's supplied via the signal type. The structure of the alert logic will change depending on the signal type.
    ACTIONS
        The action, like sending an email, sending an SMS message, or using a webhook.
        An action group, which typically contains a unique set of recipients for the action.
    ALERT DETAILS
        An alert name and an alert description that should specify the alert's purpose.
        The severity of the alert if the criteria or logic test evaluates true. The five severity levels are:
            0: Critical
            1: Error
            2: Warning
            3: Informational
            4: Verbose

Scope of alert rules

You can get monitoring data from across most of the Azure services, and report on it by using the Azure Monitor pipeline. In the Azure Monitor pipeline, you can create alert rules for these items and more:

    Metric values
    Log search queries
    Activity log events
    Health of the underlying Azure platform
    Tests for website availability

The following alert capabilities aren't yet available for the generation of monitoring data:

    Service health alerts based on activity logs
    Web availability tests through Application Insights

Managing alert rules

Not every alert rule that you create needs to run forever. With Azure Monitor, you can specify one or more alert rules and enable or disable them as needed.

As an Azure solution architect, you would use Azure Monitor to enable tightly focused and specific alerts before any application change. You would then disable the alerts after a successful deployment.
Alert summary view

By default, the alert page shows a summary of all alerts. Note that the view doesn't show classic alerts. You can apply filters to the view by using one or more of the following three categories: subscriptions, resource groups, or time ranges. The view will include only alerts that match these criteria. The following constraints apply:

    Subscriptions: You're limited to reporting on a maximum of five subscriptions.
    Resource groups: You can have only one resource group.
    Time ranges: These ranges support the past hour, the past 24 hours, the past 7 days, and the past 30 days.

Understanding the alert state in the resolution process

You control the alert state to manage and specify where you are in the alert resolution process. Currently, there are three states:

    Every new alert has an alert state of New. This state means that the issue has been detected but not yet reviewed.
    After an administrator has reviewed the alert and is working on it, the alert state changes to Acknowledged.
    When the issue is resolved, the alert state is set to Closed.

Filtering alerts

From the alert summary window, you'll see a satellite view of the alerts being reported in Azure Monitor. You filter this view to reduce the volume of alerts being reported to a specific subset that you're interested in.

You can select the following items to filter the view:

    Smart groups: You can select this filter if it's enabled.
    Resource type: This filter is applicable only when it's used with a resource group.
    Resource: This filter is applicable only when a resource type has been specified.
    Severity: This filter identifies the severity assigned by the alert rule.
    Monitor condition: This filter is set by the system and indicates if the alert is fired or resolved.
    Alert state: You'd typically use this filter to find the New and Acknowledged alerts.

# Use metric alerts to alert on performance issues in your Azure environment

Azure Monitor can use thresholds to monitor specific resources. In an organization, it's far more useful to be notified when the free disk space on a server is less than 5 percent, instead of being alerted every time a file is saved.

As a solution architect, you want to implement regular threshold monitoring for a number of your target resources and instances. Monitoring will help to head off potential issues before they can affect your customers.

## When would you use metric alerts?

In Azure Monitor, you can use metric alerts to achieve regular threshold monitoring of Azure resources. Azure Monitor runs metric alert trigger conditions at regular intervals. When the evaluation is true, Azure Monitor sends a notification. Metric alerts are stateful, and Azure Monitor will send a notification only when the prerequisite conditions are met.

Metric alerts can be useful if, for instance, you need to know when your server CPU utilization is reaching a critical threshold of 90 percent. You can be alerted when your database storage is getting too low, or when network latency is about to reach unacceptable levels.

## Composition of a metric alert

As you learned in the previous unit, all alerts are governed by their rules. For metric alerts, there's an additional factor to define: the condition type. It can be static or dynamic.

You must define the type of statistical analysis to be used with either static or dynamic metric alerts. Example types are minimum, maximum, average, and total. In this example, you define the period of data to be assessed: the last 10 minutes. Finally, you set the frequency by which the alert conditions are checked: every 2 minutes.

## Using static threshold metric alerts

Static metric alerts are based on simple static conditions and thresholds that you define. With static metrics, you specify the threshold that will be used to trigger the alert or notification.

In the previously defined scenario, a static alert with a threshold of 85 percent CPU utilization checks the rule every 2 minutes. It evaluates the last 10 minutes of CPU utilization data to assess if it rises above the threshold. If the evaluation is true, the alert triggers the actions associated with the action group.

## Using dynamic threshold metric alerts

Dynamic metric alerts use machine learning tools that Azure provides to automatically improve the accuracy of the thresholds defined by the initial rule.

There's no hard threshold in dynamic metrics. However, you'll need to define two more parameters:

    The look-back period defines how many previous periods need to be evaluated. For example, if you set the look-back period to 3, then in the example used here, the assessed data range would be 30 minutes (three sets of 10 minutes).

    The number of violations expresses how many times the logic condition has to deviate from the expected behavior before the alert rule fires a notification. In this example, if you set the number of violations to two, the alert would be triggered after two deviations from the calculated threshold.

Understanding dimensions

Until now, the assessed metric alerts have focused on a single target instance. Azure Monitor supports dimensions, which enable monitoring data to be supplied from multiple target instances.

You use dimensions to define one metric alert rule and have it applied to multiple related instances. For example, you can monitor CPU utilization across all the servers running your application. You can then receive an individual notification for each server instance when the rule conditions are triggered.

You can define the dimensions by naming each target instance specifically. Or you can define the dimensions by using the asterisk (*) wildcard, which will use all available instances.
Scaling metric alerts

Azure Monitor supports the creation of metric alerts that, like dimensions, monitor multiple resources. Scaling is currently limited to Azure virtual machines. However, a single metric alert can monitor resources in one Azure region.

The creation of scaling metric alert rules to monitor multiple resources is no different from creating any other metric alert rule. You just select all the resources that you want to monitor.

Like dimensions, a scaling metric alert is individual to the resource that triggered it.


# Exercise - Use metric alerts to alert on performance issues in your Azure environment

https://docs.microsoft.com/en-us/learn/modules/incident-response-with-alerting-on-azure/4-exercise-metric-alerts

# Use log alerts to alert on events in your application

You can use Azure Monitor to capture important information from log files. These log files can be created by applications, operating systems, other hardware, or Azure services.

As a solution architect, you want to explore ways that monitoring log data can detect issues before they become problems for your customers. You know that Azure Monitor supports the use of log data.

In this unit, you want to understand how the use of log data can improve resilience in your system.
When to use log alerts

Log alerts use log data to assess the rule logic and, if necessary, trigger an alert. This data can come from any Azure resource: server logs, application server logs, or application logs.

By its nature, log data is historical. So usage is focused on analytics and trends.

You use these types of logs to assess if any of your servers have exceeded their CPU utilization by a given threshold during the last 30 minutes. Or you can evaluate response codes issued on your web application server in the last hour.
How log alerts work

Log alerts behave in a slightly different way from other alert mechanisms. The first part of a log alert is used to define the log search rule. The rule defines how often it should run, the time period under evaluation, and the query to be run.

When a log search evaluates as positive, an alert record is created and any associated actions are triggered.
Composition of log search rules

Every log alert has an associated search rule. The composition of these rules is:

    Log query: The query that runs every time the alert rule fires.
    Time period: The time range for the query.
    Frequency: How often the query should run.
    Threshold: The trigger point for an alert to be created.

Log search results are one of two types, number of records or metric measurement.
Number of records

Consider using the number-of-records type of log search when you're working with an event or event-driven data. Examples are syslog and web app responses.

This type of log search returns a single alert when the number of records in a search result reaches or exceeds the value for the number of records (threshold). For example, when the threshold for the search rule is greater or equal to five, the query results have to return five or more rows of data before the alert is triggered.
Metric measurement

Metric measurement logs offer the same basic functionality as metric alert logs.

Unlike number-of-records search logs, metric measurement logs require additional criteria to be set:

    Aggregate function: The calculation that will be made against the result data. An example is count or average. The result of the function is called AggregatedValue.
    Group field: A field by which the result will be grouped. This criterion is used in conjunction with the aggregated value. For example, you might specify that you want the average grouped by computer.
    Interval: The time interval by which data is aggregated. For example, if you specify 10 minutes, an alert record is created for each aggregated block of 10 minutes.
    Threshold: A point defined by an aggregated value and the total number of breaches.

Consider using this type of alert when you need to add a level of tolerance to the results found. One use for this type of alert is to respond if a particular trend or pattern is found. For example, if the number of breaches is five, and any server in your group exceeds 85 percent CPU utilization more than five times within the given time period, an alert is fired.

As you can see, metric measurements greatly reduce the volume of alerts that are produced. But give careful consideration when you're setting the threshold parameters, to avoid missing critical alerts.

Stateless nature of log alerts

One of the primary considerations when you're evaluating the use of log alerts is that they are stateless. This means that a log alert will generate new alerts every time the rule criteria are triggered, regardless of whether the alert was previously recorded.


# Use activity log alerts to alert on events within your Azure infrastructure

Activity log alerts allow you to be notified when a specific event happens on some Azure resource. For example, you can be notified when someone creates a new VM in a subscription.

An activity log can also include alerts for Azure service health. A company can be notified when service issues or planned maintenance happens on the Azure platform.

As an Azure solution architect, you want to explore the capability to monitor selected Azure resources within your subscription. You'll understand how the resources can be used to improve your team's responsiveness and the stability of your systems.

In this unit, you'll explore the two different kinds of active log alerts. Now that you've seen all the different kinds of alerts you can use in Azure Monitor, you'll see how you can trigger actions for your alerts. Actions might include sending an email or creating an IT Service Management (ITSM) support ticket.
When to use activity log alerts

So far, you've seen two different types of alerts supported in Azure Monitor. Metric alerts are ideally suited to monitoring for threshold breaches or spotting trends. Log alerts allow for greater analytical monitoring of historical data.

Activity log alerts are designed to work with Azure resources. Typically, you create this type of log to receive notifications when specific changes occur on a resource within your Azure subscription.

There are two types of activity log alerts:

    Specific operations: Apply to resources within your Azure subscription and often have a scope with specific resources or a resource group. You use this type when you need to receive an alert that reports a change to an aspect of your subscription. For example, you can receive an alert if a virtual machine is deleted or new roles are assigned to a user.
    Service health events: Include notice of incidents and maintenance of target resources.

Composition of an activity log alert

It's important to note that activity log alerts will monitor events only in the subscription where the log alert was created.

Activity log alerts are based on events. So the best approach for defining them is to use Azure Monitor to filter all the events in your subscription - until you find the one that you want. You then select Add activity log alert to begin the creation process.

Like the previous alerts, activity log alerts have their own attributes:

    Category: Administrative, service health, autoscale, policy, or recommendation.
    Scope: Resource level, resource group level, or subscription level.
    Resource group: Where the alert rule is saved.
    Resource type: Namespace for the target of the alert.
    Operation name: Operation name.
    Level: Verbose, informational, warning, error, or critical.
    Status: Started, failed, or succeeded.
    Event initiated by: The email address or Azure Active Directory identifier (known as the "caller") for the user.

Creating a resource-specific log alert

When you create your activity log alert, you choose Activity Log for the signal type. Then you'll see all the available alerts for the resource you choose. The following screenshot shows all the administrative alerts for Azure VMs. For example, trigger an alert when a VM is powered off.

Changing the monitor service will enable you to reduce the list of options. So choosing Administrative filters all the signals to show only admin-related signals.

![6-example-activity-log-alert](https://user-images.githubusercontent.com/46513413/97606844-a1a43d80-19e6-11eb-9bd3-bac25ab12306.png)

Creating a service health alert

Service health alerts are not like all the other alert types you've seen so far in this module. To create a new alert, on the Azure portal, search for and select Service Health. Then select Health alerts. After you select + Create service health alert, the steps to create the alert are similar to the steps you've seen to create other alerts.

![6-service-health-alerts](https://user-images.githubusercontent.com/46513413/97606990-c7c9dd80-19e6-11eb-8d1d-8c9965017185.png)

The only difference is that you no longer need to select a resource, because the alert is for a whole region in Azure. What you can select is the kind of health event that you want to be alerted on. It's possible to select service issues, planned maintenance, or health advisories, or to choose all of the events. The remaining steps of performing actions and naming the alerts are the same.

Performing actions when an alert happens

When any event is triggered, you can create an associated action in an action group. Action groups allow you to define actions that will be run. You can run one or more actions for each triggered alert.

The available actions are:

    Send an email
    Send an SMS message
    Create an Azure app push notification
    Make a voice call to a number
    Call an Azure function
    Trigger a logic app
    Send a notification to a webhook
    Create an ITSM ticket
    Use a runbook (to restart a VM, or scale a VM up or down)

You can also reuse action groups on multiple alerts, after you've created them. For example, after you've created an action to email your company's operations team, you can add that action group to all the service health events.

You can add or create action groups at the same time that you create your alert. You can also edit an existing alert to add an action group after you've created it.

# Exercise - Use activity log alerts to alert on events within your Azure infrastructure

Microsoft Learn needs your permission to create Azure resources.

For more information, please check the troubleshooting guidance page.

The shipping company that you work for wants to avoid any future issues with updates to its applications on the Azure platform. To improve the alerting capabilities within Azure, you'll use activity log alerts.

Your goal is to set up the Linux VM and create an activity log monitoring rule to detect when a VM is deleted. You'll then delete the VM to trigger this alert.
Create the Azure activity log monitor

    Sign in to the Azure portal by using the same account that you activated the sandbox with.

    On the Azure portal menu, select Monitor. Next, select Alerts in the left panel.

    Select + New alert rule.

    Under the Scope section, select Select resource. The Select a resource panel appears.

    The Filter by subscription dropdown should already be populated with Concierge Subscription. In the Filter by resource type dropdown, select Virtual machines.

    You want alerts when any virtual machine in your resource group is deleted. Select the [sandbox resource group name] resource group, and then select Done.

    In the Condition section, select Select condition. The Configure signal logic panel appears.

    In the Configure signal logic panel, in the Search by signal name box, enter Delete. Select Delete Virtual Machine (Microsoft.Compute/virtualMachines).

    You want to receive alerts of all types. Leave Alert logic settings at their default of All, and then select Done.

Add an email alert action

For the previous Azure Monitor alert, you didn't add any actions. You just viewed triggered alerts in the Azure portal. Actions enable you to send emails for notifications, trigger an Azure function, or call a webhook. You'll now add an email alert when VMs are deleted.

    Under Actions, select Select action group. The Select an action group to attach to this alert rule panel appears.

    Select + Create action group. The Create action group page appears.

    Under the Basics tab, enter the following details:
    Table 1
    Setting 	Value
    Subscription 	Concierge Subscription
    Resource group 	From the dropdown, name of your sandbox resource group
    Action group name 	Alert the operations team
    Display name 	AlertOpsTeam

    Under the Notifications tab, enter the following details:
    Table 2
    Setting 	Value
    Notification type 	Email/SMS/Push/Voice
    Name 	VM was deleted

    Select the Edit pencil icon. The Email/SMS message/Push/Voice panel appears.

    Select Email, and in the Email box, enter your email address, and then select OK.

    On the Create action group page, select Review + create.

    Now that you've defined the rule, select Create.

    The Create alert rule page reappears. In the Actions section, under Alert rule details, provide the following information:
    Table 3
    Setting 	Value
    Alert rule name 	VM was deleted
    Description 	A VM in your resource group was deleted
    Save alert rule to resource group 	default resource group
    Enable alert rule upon creation 	Check - Yes

    Now that you've defined the rule, select Create alert rule.

Recipients added to the action group will receive a notification when they're added to the action group, when the alert is activated, and when the alert is triggered.

It can take up to five minutes for an activity log alert rule to become active. In this exercise, if you delete the virtual machine before this time, the alert rule might not be triggered. Because of this delay, you might not see the same results in the following steps after you delete the VM.
Delete your virtual machine

To trigger the alert, you need to delete the virtual machine that you created earlier.

    On the Azure portal menu or from the Home page, select Virtual machines. This action shows a list of the virtual machines.

    Select the vm1 virtual machine.

    From the menu bar, select Delete. The Delete Resources panel appears.

    To confirm the deletion, enter yes.

    Select Delete.

View your activity log alerts in Azure Monitor

In the example, you set up an Ubuntu VM, and you created an activity log rule to detect when the VM was deleted. You then deleted a VM from your resource group. You now need to check if an alert was triggered.

    Open your email program. You should have received an email from azure-noreply@microsoft.com.

    Screenshot of alert email

    On the Azure portal menu, select Monitor, and then select Alerts.

    You should see the Sev4 alerts generated from the deletion of the VM.

    Screenshot that shows a completed alert details section

The alert list now shows an alert for the VM that you deleted. The affected resource column tells you which VM was removed.


# Use smart groups to reduce alert noise in Azure Monitor
https://docs.microsoft.com/en-us/learn/modules/incident-response-with-alerting-on-azure/8-smart-groups

In a large environment, Azure Monitor can generate a large number of alerts. It can be hard to see the difference between your critical and nonessential issues.

You want to explore the options available in Azure Monitor. Is there a mechanism that might reduce the alert noise and make the task of managing alerts easier?

In this unit, you'll investigate how to use smart groups, and see how they can help you manage alerts in Azure Monitor.
What are smart groups?

Smart groups are an automatic feature of Azure Monitor. By using machine learning algorithms, Azure Monitor joins alerts based on repeat occurrence or similarity. Smart groups enable you to address a group of alerts instead of each alert individually.

The name of the smart group (its taxonomy), is assigned automatically, and is the name of the first alert in the group. It's important to assign meaningful names to each alert that you create, because the name of the smart group can't be changed or amended.
When to use smart groups

Think of smart groups as a dynamic filter applied to all the alerts in Azure Monitor. The machine learning algorithm in Azure Monitor joins alerts based on information, such as historical patterns, similar properties, or structure. Using smart groups can reduce alert noise by more than 90 percent.

The power of smart groups is that they show you all related alerts and give improved analytics. They can often identify a previously unseen root cause.
Managing smart groups

There are two ways to get to your smart groups: from the Alert Summary page or from the All Alerts page. Next, select Alerts by Smart Group.


Either method results in a new page that shows all the smart groups. Selecting a smart group opens its details page, which splits into two sections:

    Summary: Lists all the alerts included in the smart group.
    History: Provides a history of all the changes made to the smart group.

Screenshot that shows the details page for a smart group
Smart group states

Smart groups, like regular alerts, have their own state. The state shows the progress of the smart group in the resolution process. Changing the state of a smart group doesn't alter the state of the individual alerts.

To change the state, select Change smart group state.

The states are:

    New: The smart group has been created with a collection of alerts, but it hasn't yet been addressed.
    Acknowledged: When an admin starts the resolution process, they change the state to this.
    Closed: When the source of the alert is fixed, the admin changes the state to this.







