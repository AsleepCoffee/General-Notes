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
































