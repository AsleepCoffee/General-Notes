# Enable and Configure App Service Application Logging

In this unit, you'll look at how app logging can help with your Web apps, and how to enable these logs.

### What are app logs?

App logs are the output of runtime trace statements in app code. For example, you might want to check some logic in your code by adding a trace to show when a particular function is being processed, or you might only want to see a logged message when a particular level of error has occurred. App logging is primarily for apps in pre-production and for troublesome issues, because excessive logs can carry a performance hit and quickly consume storage; for this reason, logging to the file system is automatically disabled after 12 hours.

App logging has scale limitations, primarily because files are being used to save the logged output. If you have multiple instances of an app, and the same storage used is shared across all instances, messages from different instances may be interleaved, making troubleshooting difficult. If each instance has its own log file, there will be multiple logs, again making it difficult to troubleshoot instance-specific issues.

The types of logging available through the Azure App Service depends on the code framework of the app, and on whether the app is running on a Windows or Linux app host.
ASP.NET

ASP.NET apps only run on Windows app services. To log information to the app diagnostics log, use the System.Diagnostics.Trace class. There are four trace levels you can use, and these correlate with error, warning, information, and verbose logging levels shown in the Azure portal.

    Trace.TraceError("Message"); // Writes an error message
    Trace.TraceWarning("Message"); // Writes a warning message
    Trace.TraceInformation("Message"); // Writes an information message
    Trace.WriteLine("Message"); // Writes a verbose message

ASP.NET Core apps

ASP.NET Core apps can run on either Windows or Linux. To log information to Azure app logs, use the logger factory class, and then use one of six-log levels:

    logger.LogCritical("Message"); // Writes a critical message at log level 5
    logger.LogError("Message"); // Writes an error message at log level 4
    logger.LogWarning("Message"); // Writes a warning message at log level 3
    logger.LogInformation("Message"); // Writes an information message at log level 2
    logger.LogDebug("Message"); // Writes a debug message at log level 1
    logger.LogTrace("Message"); // Writes a detailed trace message at log level 0

For ASP.NET Core apps on Windows, these messages relate to the filters in the Azure portal in this way:

    Levels 4 and 5 are "error" messages.
    Level 3 is a "warning" message.
    Level 2 is an "information" message.
    Levels 0 and 1 are "verbose" messages.

For ASP.NET Core apps on Linux, only "error" messages (levels 4 and 5) are logged.
Node.js apps

For script-based Web apps, such as Node.js apps on Windows or Linux, app logging is enabled using the console() method:

    console.error("Message") - writes a message to STDERR
    console.log("Message") - writes a message to STDOUT

Both types of message are written to the Azure app service error-level logs.
Logging differences for Windows and Linux hosts

To route messages to log files, Azure Web apps use the Web server (IIS process). Because Windows-based Web apps are a well-established Azure service, and messaging for ASP.NET apps is tightly integrated with the underlying IIS service, Windows apps benefit from a rich logging infrastructure. For other apps, logging options may be limited by the development platform, even when running on a Windows app service.

The logging functionality available to Linux-based scripted apps, such as Node, is determined by the Docker image used for the app's container. Basic logging, using redirections to STDERR or STDOUT, uses the Docker logs. Richer logging functionality is dependent on the underlying image, such as whether this is running PHP, Perl, Ruby, and so on. To download equivalent Web application logging as provided by IIS for Windows apps, may require connecting to your container using SSH.

This table summarizes the logging support for common app environments and hosts.
Logging differences for Windows and Linux hosts
App environment 	Host 	Log levels 	Save location
ASP.NET 	Windows 	Error, Warning, Information, Verbose 	File system, Blob storage
ASP.NET Core 	Windows 	Error, Warning, Information, Verbose 	File system, Blob storage
ASP.NET Core 	Linux 	Error 	File system
Node.js 	Windows 	Error (STDERR), Information (STDOUT), Warning, Verbose 	File system, Blob storage
Node.js 	Linux 	Error 	File system
Java 	Linux 	Error 	File system
Alternatives to app diagnostics

Azure Application Insights is a site extension that provides additional performance monitoring features, such as detailed usage and performance data, and is designed for production app deployments as well as being a potentially useful development tool. Application Insights works with a range of app development environments, providing the same set of rich telemetry and performance data whether the app is ASP.NET or Node. However, to make use of Application Insights, you have to include specific code within your app, using the App Insights SDK. Application Insights is also a billable service, so depending on the scale of your app deployments and data collected, you may need to plan for regular costs.

You can also view Metrics for your app, which can help you profile how your app is operating, and these counters are useful in production, as well as, development. You can view CPU, memory, network, and file system usage, and set up alerts when a counter hits a particular threshold. Billing for metrics is covered by the app service plan tier.
Enable logging using the Azure portal

In the portal, app logging is managed from the Diagnostics logs pane of the web app.


https://docs.microsoft.com/en-us/learn/modules/capture-application-logs-app-service/media/2-portal-diagnostics-logs-pane.png

To enable app logging to the Web app's file system, set Application logging (Filesystem) to On, and then set the Level to Error, Warning, Information, or Verbose. Logging to the file system will be automatically reset to Off after 12 hours.

To enable app logging to a blob storage container, set Application logging (Blob) to On, and then select a storage account and container; the storage account and Web app must be created in the same Azure region. You then set the Level to Error, Warning, Information, or Verbose.

Note

Saving to blob storage is not available for Linux app logs.

When logging to blob storage, you must also set a Retention Period. Unlike the file system logs, blob logs are never deleted by default; the retention period option means that any logs older than the specified number of days will be deleted.

Screenshot of configuring application logs in the Azure portal with callout highlighting the save button.

After configuring the logs, select Save.
Enable logging using the Azure CLI

The current version of Azure CLI does not enable you to manage app logging to blob storage. To enable app logging to the file system, use this command.

az webapp log config --application-logging true --level verbose --name <app-name> --resource-group <resource-group-name>

For example, to enable logging to the file system for an app called contosofashions123, capturing all messages, use this command.
Azure CLI

az webapp log config --application-logging true --level verbose --name contosofashions123 --resource-group contosofashionsRG

There is currently no way to disable application logging by using Azure CLI commands; however, the following command resets file system logging to error-level only.
Azure CLI

az webapp log config --application-logging false --name <app-name> --resource-group <resource-group-name>

To view the current logging status for an app, use this command.
Azure CLI

az webapp log show --name <app-name> --resource-group <resource-group-name>

# Exercise - Enable and Configure App Service Application Logging using the Azure Portal

https://docs.microsoft.com/en-us/learn/modules/capture-application-logs-app-service/3-enable-and-configure-app-service-application-logging-using-the-azure-portal

In this unit, you'll enable app logging for the new fashions Azure Web App.

You're going to deploy a sample ASP.NET Core Web app from GitHub; this app includes code to generate various trace output messages. You'll then use the Azure portal to enable app logging for this app.
Use Azure CLI to deploy a web app

In this step, to create an ASP.NET Web app using code from a GitHub repository, you're going to use Azure CLI commands. You will also create a new storage account, in the same region as the Web app, for log storage.

    To set some variables, replacing <your-local-Azure-region>, with the closest region to you from the following list, in the Cloud Shell, run the following commands.

    The free sandbox allows you to create resources in a subset of the Azure global regions. Select a region from this list when you create resources:
        westus2
        southcentralus
        centralus
        eastus
        westeurope
        southeastasia
        japaneast
        brazilsouth
        australiasoutheast
        centralindia
    Bash

gitRepo=https://github.com/MicrosoftDocs/mslearn-capture-application-logs-app-service
appName="contosofashions$RANDOM"
appPlan="contosofashionsAppPlan"
appLocation=<your-local-Azure-region>
resourceGroup=[sandbox resource group name]
storageAccount=sa$appName

To deploy the web app, in the Cloud Shell, run the following commands.
Azure CLI

az appservice plan create --name $appPlan --resource-group $resourceGroup --location $appLocation --sku FREE
az webapp create --name $appName --resource-group $resourceGroup --plan $appPlan --deployment-source-url $gitRepo

Make a note of the random number suffix in your app name; this was generated to uniquely identify your app. The app may take several minutes to deploy.

To create a storage account, in the Cloud Shell, run the following command.
Azure CLI

    az storage account create -n $storageAccount -g $resourceGroup -l $appLocation --sku Standard_LRS 

    Before continuing with the exercise, wait until the commands have been completed.

Enable logging using the Azure portal

In this step, you're going to use the Azure portal to enable app logging to the file system, and to Azure Blob storage. You'll start by checking that your Web app is running.

    Sign in to the Azure portal using the same account you activated the sandbox with.
    On the Portal toolbar, select Subscriptions, and in the directories list, select Microsoft Learn Sandbox (this is the directory associated with the Concierge Subscription).
    On the Azure portal menu, or from the Home page, select Resource groups, and check that your sandbox resource group ([sandbox resource group name]) is listed.
    On the Azure portal menu, select App Services.
    In the App Services list, select contosofashions<your-number>. Next, in the Overview section, to open the home page for the Contoso Fashions website in a new browser tab, select the URL string (https://contosofashions<_your-number\ >.azurewebsites.net).

You'll now set up the app logging.

    Switch to the tab showing the Azure portal.
    On the left-hand side, scroll down to the Monitoring section, and then select App Service Logs.
    Under Application logging (Filesystem), select On, and in the Level box, select Error.
    Under Application logging (Blob), select On, and in the Level box, select Verbose.
    Select Storage Settings, and on the Storage Accounts pane, select sacontosofashions<your-number>, where <your-number> is the number suffix you noted when you created your app. If it says Storage not configured, select that text, and follow the previous directions.
    On the Containers pane, select + Container, and in the Name box, enter asplogs, and then select Create.
    Select asplogs, and then select Select.
    In the Retention Period (Days) box, enter 5.
    To close the logs pane, and update the log settings, select Save.

#View Live Application Logging with the Log Streaming Service

In this unit, you'll look at how to view a live app log stream, and how live log streams can help during Web app development.
What is live log streaming

Live log streaming is an easy and efficient way to view live logs for troubleshooting purposes. Live log streaming is designed to provide a quick view of all messages that are being sent to the app logs in the file system, without having to go through the process of locating and opening these logs. To use live logging, you connect to the live log service from the command line, and can then see text being written to the app's logs in real time.
What logs can be streamed

The log streaming service adds a redirect from the file system logs, so you'll see the same information as is saved to those log files. So, if you enable verbose logging for ASP.NET Windows apps, for example, the live log stream will show all your logged messages.

Typical scenarios for using live logging

Live logging is a good tool for initial debugging; log messages show in real time to give you quick feedback on code or server issues. You can then make a change, redeploy your app, and instantly see the results.

The live log stream connects to only one app instance, so is not useful if you have a multi-instance app. Live logging is also of limited use as you scale up your apps; in these scenarios, it is better to ensure that messages are saved to log files that can be opened and studied offline.
How to use live log streaming

To enable live log streaming from the command line, run Azure CLI or curl commands.
Azure CLI

To open the log stream, run the following command.

az webapp log tail --name <app name> --resource-group <resource group name>

To stop viewing live logs, press Ctrl +C.
Curl

To use Curl, you need deployment credentials. There are two types of deployment credentials:

    App level. Azure automatically creates a username/password pair when you deploy a Web app, and each of your apps has their own separate set of credentials.

    User level. You can create your own credentials for use with any Web app; you can manage these credentials in the Azure portal, as long as you already have at least one Web app, or by using Azure CLI commands.

You can view and copy these details from the Deployment Credentials page in the Azure portal

To create a new set of user-level credentials, run the following command.

az webapp deployment user set --user-name <name-of-user-to create> --password <new-password>

Note

Usernames must be globally unique across all of Azure, not just within your own subscription or directory.

After you have created a set of credentials, to open the log stream, run the following command. You'll be prompted for the password.
azcli

curl -u {username} https://{sitename}.scm.azurewebsites.net/api/logstream

To close the log stream session, press Ctrl +C.

# Exercise - View Live Application Logging with the Log Streaming Service using Azure CLI

As the lead Web developer for Contoso Fashions, you now want a quick view of your new Web app's operation. You know there will be issues, so rather than having to find and open log files, you want to use log streaming as a quick way to view logged messages as you troubleshoot your app.

In this unit, you're going to use Azure CLI and Curl commands to view the live log stream generated by your Web app.
Use Azure CLI to view the live log stream

The ASP.NET app that you've deployed includes the following code for the home page:
C#

logger.LogInformation("Information message from OnGet method on Index.cshtml page");
logger.LogDebug("Debug message from OnGet method on Index.cshtml page");
logger.LogError("Error message from OnGet method on Index.cshtml page");
logger.LogWarning("Warning message from OnGet method on Index.cshtml page");
logger.LogTrace("Trace message from OnGet method on Index.cshtml page");
logger.LogCritical("Critical message from OnGet method on Index.cshtml page");

Similar code is included on the other pages. Each time a page is loaded, a log entry will be generated for every log level that has been enabled in the app service. So, because you enabled Error-level logging for the file system, you will only see LogError and LogCritical messages.

In this step, you'll open the log stream generated by your ASP.NET Web app by using Azure CLI commands from the Azure Cloud Shell.

    In the Azure Cloud Shell, to open the log stream, replacing <your-number> with the random number that was generated to uniquely identify your app, run the following command.
    Azure CLI

az webapp log tail  --resource-group [sandbox resource group name] --name contosofashions<your-number>

Wait until you see the Welcome, you are now connected to log-streaming service message.

Switch to the browser tab showing the Contoso Fashions website (https://contosofashions<_your-number\ >.azurewebsites.net).

On the website Home page, select About. On the About page, select Contact, and then on the Contact page, select Home.

In the Azure Cloud Shell, you should now see log entries generated by each page in the ASP.NET app; if you do not see any log data, repeat the previous step, and wait a few minutes.

The log stream should display entries for each page, such as:
Azure CLI

Error message, in the Page_Load method for Contact.aspx

Click in the Azure Cloud Shell, and to stop the log stream session, press Ctrl + C.

# Retrieve Application Log Files

Log files are a great resource for a Web developer, but only if you know how to find and use the logged information. Here, you'll look at the methods you can use to retrieve logged information, ready for offline analysis.
Log file storage locations

The Azure infrastructure used to run Windows Web apps is not the same as that for Linux apps, and log files are not stored in the same locations.
Windows app log files

For Windows apps, file system log files are stored in a virtual drive that is associated with your Web app. This drive is addressable as D:\Home, and includes a LogFiles folder; within this folder are one or more subfolders:

    Application - contains application-generated messages, if File System application logging has been enabled.
    DetailedErrors - contains detailed Web server error logs, if **Detailed error messages have been enabled.
    http - contains IIS-level logs, if Web server logging has been enabled.
    W3SVC<number> - contains details of all failed http requests, if Failed request tracing has been enabled.

Where storage to a Blob container has been enabled, logs are stored in year, month, date, and hour folders; for example:

    2019
     01
      10
       08 - log entries for the period 08:00:00 to 08:59:59 on January 10th 2019
       09 - log entries for the period 09:00:00 to 09:59:59 on January 10th 2019

Within the hour folder, there will be one or more CSV files containing messages saved within that 60-minute period.
Linux app log files

For Linux Web apps, the Azure tools currently support fewer logging options than for Windows apps. Redirections to STDERR and STDOUT are managed through the underlying Docker container that runs the app, and these messages are stored in Docker log files. To see messages logged by underlying processes, such as Apache, you will need to open an SSH connection to the Docker container.
Methods for retrieving log files

How you retrieve log files depends on the type of log file, as well as your preferred environment. For file system logs, you can use the Azure CLI or the Kudu console.
Azure CLI

To download file system log files using the Azure CLI, first copy the log files from the app's file system to your Azure Cloud Shell storage, and then run the following command.
Azure CLI

az webapp log download --log-file \<_filename_\>.zip  --resource-group \<_resource group name_\> --name \<_app name_\>

To download the zipped log files to your local computer, ready for opening in Microsoft Excel, or other apps, use the file download and upload tool on the Azure Cloud Shell toolbar.

Note

The Azure CLI download includes all app logs, except for failed request traces.
Kudu

All Azure Web apps have an associated Source Control Management (SCM) service site. This site runs the Kudu service, and other Site Extensions; it is Kudu that manages deployment and troubleshooting for Azure Web Apps, including options for viewing and downloading log files. The specific functionality available in KUDU, and how you download logs, depends on the type of Web app. For Windows apps you can browse to the log file location, and then download the logs; for Linux apps, there may be a download link.

One way to access the KUDU console is navigate to https://<app name>.scm.azurewebsites.net, and then sign in using deployment credentials.

You can also access KUDU from the Azure portal. On the app pane, in the Development Tools section, select Advanced Tools, and then on the Advanced Tools pane, to open a new Kudu Services tab, select Go.

To download the log files from Windows apps:

    Select Debug Console, and then select CMD.

https://docs.microsoft.com/en-us/learn/modules/capture-application-logs-app-service/media/6-kudu-windows-logs-cmd.png

    Then, in the file explorer section, select LogFiles, and for the Application folder, select Download; the logs will be downloaded to your computer as Application.zip.

    For Linux apps, click the download link on the Environment page.

 https://docs.microsoft.com/en-us/learn/modules/capture-application-logs-app-service/media/6-kudu-linux-logs.png

Azure Storage Explorer

To access Windows logs saved to an Azure Blob Storage container, you can use the Azure portal; to view and download the contents of the log file container, select Storage Explorer. Open the relevant year, month, date, and hour folder, then double-click a CSV file to download it to your computer.

https://docs.microsoft.com/en-us/learn/modules/capture-application-logs-app-service/media/6-blob-logs.png

If you have Microsoft Excel on your computer, the log file will automatically open as a worksheet; otherwise, you can open the file using a text editor such as Notepad.
















