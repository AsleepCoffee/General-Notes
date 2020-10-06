# Features of Azure Monitor logs

Azure Monitor is a service for collecting and analyzing telemetry. It helps you get maximum performance and availability for your cloud applications, and for your on-premises resources and applications. It shows how your applications are performing and identifies any issues with them.

# Data collection in Azure Monitor

Azure Monitor collects two fundamental types of data: metrics and logs. Metrics tell you how the resource is performing, and the other resources that it's consuming. Logs contain records that show when resources are created or modified.

The following diagram gives a high-level view of Azure Monitor. On the left are the sources of monitoring data: Azure, operating systems, and custom sources. At the center of the diagram are the data stores for metrics and logs. On the right are the functions that Azure Monitor performs with this collected data, such as analysis, alerting, and streaming to external systems.

![Azure data collector](https://user-images.githubusercontent.com/46513413/95248414-431fe100-07e5-11eb-922a-2a636c7e8cef.PNG)

Azure Monitor collects data automatically from a range of components. For example:

    Application data: Data that relates to your custom application code.
    Operating system data: Data from the Windows or Linux virtual machines that host your application.
    Azure resource data: Data that relates to the operations of an Azure resource, such as a web app or a load balancer.
    Azure subscription data: Data that relates to your subscription. It includes data about Azure health and availability.
    Azure tenant data: Data about your Azure organization-level services, such as Azure Active Directory.

Because Azure Monitor is an automatic system, it begins to collect data from these sources as soon as you create Azure resources such as virtual machines and web apps. You can extend the data that Azure Monitor collects by:

    Enabling diagnostics: For some resources, such as Azure SQL Database, you receive full information about a resource only after you have enabled diagnostic logging for it. You can use the Azure portal, the Azure CLI, or PowerShell to enable diagnostics.
    Adding an agent: For virtual machines, you can install the Log Analytics agent and configure it to send data to a Log Analytics workspace. This agent increases the amount of information that's sent to Azure Monitor.

Your developers might also want to send data to Azure Monitor from custom code, such as a web app, an Azure function, or a mobile app. They send data by calling the Data Collector API. You communicate with this REST interface through HTTP. This interface is compatible with a variety of development frameworks, such as .NET Framework, Node.js, and Python. Developers can choose their favorite language and framework to log data in Azure Monitor.
Logs

Logs contain time-stamped information about changes made to resources. The type of information recorded varies by log source. The log data is organized into records, with different sets of properties for each type of record. The logs can include numeric values such as Azure Monitor metrics, but most include text data rather than numeric values.

The most common type of log entry records an event. Events can occur sporadically rather than at fixed intervals or according to a schedule. Events are created by applications and services, which provide the context for the events. You can store metric data in logs to combine them with other monitoring data for analysis.

You log data from Azure Monitor in a Log Analytics workspace. Azure provides an analysis engine and a rich query language. The logs show the context of any problems and are useful for identifying root causes.

# Metrics

Metrics are numerical values that describe some aspect of a system at a point in time. Azure Monitor can capture metrics in near real time. The metrics are collected at regular intervals and are useful for alerting because of their frequent sampling. You can use a variety of algorithms to compare a metric to other metrics and observe trends over time.

Metrics are stored in a time-series database. This data store is most effective for analyzing time-stamped data. Metrics are suited for alerting and fast detection of issues. They can tell you about system performance. If needed, you can combine them with logs to identify the root cause of issues.

# Analyzing logs by using Kusto

To retrieve, consolidate, and analyze data, you specify a query to run in Azure Monitor logs. You write a log query with the Kusto query language, which is also used by Azure Data Explorer.

Log queries can be tested in the Azure portal so you can work with them interactively. You typically start with basic queries and then progress to more advanced functions as your requirements become more complex.

In the Azure portal, you can create custom dashboards, which are targeted displays of resources and data. Each dashboard is built from a set of tiles. Each tile might show a set of resources, a chart, a table of data, or some custom text. Azure Monitor provides tiles that you can add to dashboards. For example, you might use a tile to display the results of a Kusto query in a dashboard.

In the example scenario, the operations team can consolidate its data by visualizing monitoring data such as charts and tables. These tools are effective for summarizing data and presenting it to different audiences.

By using Azure dashboards, you can combine various kinds of data, including both logs and metrics, into a single pane in the Azure portal. For example, you might want to create a dashboard that combines tiles that show a graph of metrics, a table of activity logs, charts from Azure Monitor, and the output of a log query.


# Create basic Azure Monitor log queries to extract information from log data

You use Azure Monitor log queries to extract information from log data. Querying is an important part of examining the log data that Azure Monitor captures.

In the example scenario, the operations team will use Azure Monitor log queries to examine the health of its system.
Write Azure Monitor log queries by using Log Analytics

You can find the Log Analytics tool in the Azure portal and use it to run sample queries or to create your own queries:

    1. In the Azure portal, select Monitor in the left pane.

    You see the Azure Monitor page and more options, including Activity Log, Alerts, Metrics, and Logs.

    2. Select Query & Analyze Logs.

    Here you can enter your query and see the output.

https://docs.microsoft.com/en-us/learn/modules/analyze-infrastructure-with-azure-monitor-logs/media/3-azure-monitor-portal-query-pane.png

# Write queries by using the Kusto language

You use the Kusto Query Language to query log information for your services running in Azure. A Kusto query is a read-only request to process data and return results. You state the query in plain text, by using a data-flow model that's designed to make the syntax easy to read, write, and automate. The query uses schema entities that are organized in a hierarchy similar to that of Azure SQL Database: databases, tables, and columns.

A Kusto query consists of a sequence of query statements, delimited by a semicolon (;). At least one statement is a tabular expression statement. A tabular expression statement formats the data arranged as a table of columns and rows.

The syntax of a tabular expression statement has a tabular data flow from one tabular query operator to another, starting with a data source. A data source might be a table in a database, or an operator that produces data. The data then flows through a set of data transformation operators that are bound together with the pipe (|) delimiter.

For example, the following Kusto query has a single tabular expression statement. The statement starts with a reference to a table called Events. The database that hosts this table is implicit here, and is part of the connection information. The data for that table, stored in rows, is filtered by the value of the StartTime column. The data is filtered further by the value of the State column. The query then returns the count of the resulting rows.

        Events
        | where StartTime >= datetime(2018-11-01) and StartTime < datetime(2018-12-01)
        | where State == "FLORIDA"  
        | count


NOTE: The Kusto query language that Azure Monitor uses is case-sensitive. Language keywords are typically written in lowercase. When you're using names of tables or columns in a query, make sure to use the correct case.

Events, captured from the event logs of monitored computers, are just one type of data source. Azure Monitor provides many other types of data sources. For example, the Heartbeat data source reports the health of all computers that report to your Log Analytics workspace. You can also capture data from performance counters, and update management records.

The following example retrieves the most recent heartbeat record for each computer. The computer is identified by its IP address. In this example, the summarize aggregation with the arg_max function returns the record with the most recent value for each IP address.


# Exercise - Create basic Azure monitor log queries to extract information from log data 

https://docs.microsoft.com/en-us/learn/modules/analyze-infrastructure-with-azure-monitor-logs/4-exercise-create-log-queries






























