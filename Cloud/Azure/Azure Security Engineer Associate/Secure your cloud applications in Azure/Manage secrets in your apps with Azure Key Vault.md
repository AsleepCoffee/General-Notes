Introduction

Leaking a database connection string, API key, or service password can be catastrophic. Stolen or deleted data, financial harm, application downtime, and irreparable damage to business assets and reputation are all potential results. Unfortunately, secret values often need to be deployed in multiple places simultaneously and changed at inopportune times. And you have to store them somewhere! Let's see how Steve can reduce risk and improve the security and maintainability of his app with Azure Key Vault.

## What is Azure Key Vault?

Azure Key Vault is a secret store: a centralized cloud service for storing application secrets - configuration values like passwords and connection strings that must remain secure at all times. Helps you control your applications' secrets by keeping them in a single central location and providing secure access, permissions control, and access logging.

The main benefits of using Key Vault are:

    Separation of sensitive application information from other configuration and code, reducing risk of accidental leaks
    Restricted secret access with access policies tailored to the applications and individuals that need them
    Centralized secret storage, allowing required changes to happen in only one place
    Access logging and monitoring to help you understand how and when secrets are accessed

Secrets are stored in individual vaults, which are Azure resources used to group secrets together. Secret access and vault management is accomplished via a REST API, which is also supported by all of the Azure management tools as well as client libraries available for many popular languages. Every vault has a unique URL where its API is hosted.

**Important**

Key Vault is designed to store configuration secrets for server applications. It's not intended for storing data belonging to your app's users, and it shouldn't be used in the client-side part of an app. This is reflected in its performance characteristics, API, and cost model.

User data should be stored elsewhere, such as in an Azure SQL database with Transparent Data Encryption, or a storage account with Storage Service Encryption. Secrets used by your application to access those data stores can be kept in Key Vault.

## What is a secret in Key Vault?

In Key Vault, a secret is a name-value pair of strings. Secret names must be 1-127 characters long, contain only alphanumeric characters and dashes, and must be unique within a vault. A secret value can be any UTF-8 string up to 25 KB in size.

Authentication to Key Vault uses Azure Active Directory identities. Access policies are used to provide authorization for actions that apply to every secret in the vault.

Once secrets have been loaded by an app, they are unprotected. Make sure to not log them, store them, or return them in client responses.

**Tip** Secret names don't need to be considered especially secret themselves. You can store them in your app's configuration if your implementation calls for it. The same is true of vault names and URLs.

**Note** Key Vault supports two additional kinds of secrets beyond strings — keys and certificates — and provides useful functionality specific to their use cases. This module does not cover these features and concentrates on secret strings like passwords and connection strings.

## Vault authentication and permissions

Azure Key Vault's API uses Azure AD to authenticate users and applications. Vault access policies are based on actions, and are applied across an entire vault. For example, an application with Get (read secret values), List (list names of all secrets), and Set (create or update secret values) permissions to a vault is able to create secrets, list all secret names, and get and set all secret values in that vault.

All actions performed on a vault require authentication and authorization. no way to grant anonymous access.

**Tip** When granting vault access to developers and apps, follow principle of least privilege.

Developers will usually only need Get and List permissions to a development-environment vault. Some engineers will need full permissions to change and add secrets when necessary.

For apps, often only Get permissions are required. Some apps may require List depending on the way the app is implemented. The app we'll implement in this module's exercise requires the List permission because of the technique it uses to read secrets from the vault.


## Creating Key Vaults for your applications

Good practice is to create a separate vault for each deployment environment of each of your applications, such as development, test, and production. You can use a single vault to store secrets for multiple apps and environments, but the impact of an attacker gaining read access to a vault increases with the number of secrets in the vault.

**Tip** If you use the same names for secrets across different environments for an application, the only environment-specific configuration that has to change in your app is the vault URL.

Creating a vault requires no initial configuration. Your user identity is automatically granted the full set of secret management permissions and you can start adding secrets immediately. Once you have a vault, adding and managing secrets can be done from any Azure administrative interface, including the Azure portal, the Azure CLI, and Azure PowerShell. When you set up your application to use the vault, you'll need to assign the correct permissions to it; we'll see that in the next unit.

## Create the vault and store the secret in it

Given all the trouble the company's been having with application secrets, management has asked you to create a small starter app to set the other developers on the right path. The app needs to demonstrate best practices for managing secrets as simply and securely as possible.

To start, you'll create a vault and store one secret in it.
Create the vault

Key Vault names must be globally unique, so you'll need to pick a unique name. Vault names must be 3-24 characters long and contain only alphanumeric characters and dashes. Make a note of the vault name you choose, as you'll need it throughout this exercise.

Run the following command in the Cloud Shell to create your vault.

    az keyvault create \
        --resource-group learn-38cddd9e-efd0-49ff-a670-9a09801a8e01 \
        --location centralus \
        --name <your-unique-vault-name>

**TIP** The command used the pre-created resource group named learn-38cddd9e-efd0-49ff-a670-9a09801a8e01. When working with your own subscription, you would want to either create a new resource group, or use an existing one you have previously created.

Add the secret

Now add the secret: our secret will be named SecretPassword with a value of reindeer_flotilla.

        az keyvault secret set \
            --name SecretPassword \
            --value reindeer_flotilla \
            --vault-name <your-unique-vault-name>


## Vault authentication with managed identities for Azure resources

Azure Key Vault uses Azure Active Directory to authenticate users and applications that try to access a vault. To grant our web application access to the vault, we first need to register our app with Azure Active Directory. Registering creates an identity for the app. Once the app has an identity, we can assign vault permissions to it.

Apps and users authenticate to Key Vault using an Azure Active Directory authentication token. Getting a token from Azure Active Directory requires a secret or certificate, because anyone with a token could use the application identity to access all of the secrets in the vault.

Our application secrets are secure in the vault, but we still need to keep a secret or certificate outside of the vault in order to access them! This problem is called the bootstrapping problem, and Azure has a solution for it.

## Managed identities for Azure resources

Managed identities for Azure resources is an Azure feature that your app can use to access Key Vault and other Azure services without having to manage even a single secret outside of the vault. Using a managed identity is a simple and secure way to take advantage of Key Vault from your web app.

When you enable managed identity on your web app, Azure activates a separate token-granting REST service specifically for use by your app. Your app will request tokens from this service instead of directly from Azure Active Directory. Your app needs to use a secret to access this service, but that secret is injected into your app's environment variables by App Service when it starts up. You don't need to manage or store this secret value anywhere, and nothing outside of your app can access this secret or the managed identity token service endpoint.

Managed identities for Azure resources also registers your app in Azure Active Directory for you, and will delete the registration if you delete the web app or disable its managed identity.

Managed identities are available in all editions of Azure Active Directory, including the Free edition included with an Azure subscription. Using it in App Service has no extra cost and requires no configuration, and it can be enabled or disabled on an app at any time.

Enabling a managed identity for a web app requires only a single Azure CLI command with no configuration. We'll do it later on when we set up an App Service app and deploy to Azure. 

## Exercise - Access secrets stored in Azure Key Vault


**Reading secrets in an ASP.NET Core app**

The Azure Key Vault API is a REST API that handles all management and usage of keys and vaults. Each secret in a vault has a unique URL, and secret values are retrieved with HTTP GET requests.

The official Key Vault client for .NET Core is the *KeyVaultClient* class in the Microsoft.Azure.KeyVault NuGet package. You don't need to use it directly, though — with ASP.NET Core's *AddAzureKeyVault* method, you can load all the secrets from a vault into the Configuration API at startup. This technique enables you to access all of your secrets by name using the same *IConfiguration interface* you use for the rest of your configuration. Apps that use *AddAzureKeyVault* require both Get and List permissions to the vault.

**Tip** Regardless of the framework or language you use to build your app, you should design it to cache secret values locally or load them into memory at startup unless you have a specific reason not to. Reading them directly from the vault every time you need them is unnecessarily slow and expensive.

*AddAzureKeyVault* only requires the vault name as an input, which we'll get from our local app configuration. It also automatically handles managed identity authentication — when used in an app deployed to Azure App Service with managed identities for Azure resources enabled, it will detect the managed identities token service and use it to authenticate. It's a good fit for most scenarios and implements all best practices, and we'll use it in this unit's exercise.


**Handling secrets in an app**

Once a secret is loaded into your app, it's up to your app to handle it securely. In the app we build in this module, we write our secret value out to the client response and view it in a web browser to demonstrate that it has been loaded successfully. Returning a secret value to the client is not something you'd normally do! Usually, you'll use secrets to do things like initialize client libraries for databases or remote APIs.

**Important** Always carefully review your code to ensure that your app never writes secrets to any kind of output, including logs, storage, and responses.


**Create the app**

In the Azure Cloud Shell terminal, run the following to create a new ASP.NET Core web API application and open it in the editor.

    dotnet new webapi -o KeyVaultDemoApp
    cd KeyVaultDemoApp
    code .
    
After the editor loads, run the following commands in the shell to add the NuGet package containing **AddAzureKeyVault** and restore all of the app's dependencies.

    dotnet add package Microsoft.Extensions.Configuration.AzureKeyVault -v 2.1.1
    dotnet restore

Add code to load and use secrets

To demonstrate good usage of Key Vault, we will modify our app to load secrets from the vault at startup. We'll also add a new controller with an endpoint that gets our SecretPassword secret from the vault.

First, the app startup: Open Program.cs, delete the contents and replace them with the following code:

    using Microsoft.AspNetCore;
    using Microsoft.AspNetCore.Hosting;
    using Microsoft.Extensions.Configuration;

    namespace KeyVaultDemoApp
    {
        public class Program
        {
            public static void Main(string[] args)
            {
                CreateWebHostBuilder(args).Build().Run();
            }

            public static IWebHostBuilder CreateWebHostBuilder(string[] args) =>
                WebHost.CreateDefaultBuilder(args)
                    .ConfigureAppConfiguration((context, config) =>
                    {
                        // Build the current set of configuration to load values from
                        // JSON files and environment variables, including VaultName.
                        var builtConfig = config.Build();

                        // Use VaultName from the configuration to create the full vault URL.
                        var vaultUrl = $"https://{builtConfig["VaultName"]}.vault.azure.net/";

                        // Load all secrets from the vault into configuration. This will automatically
                        // authenticate to the vault using a managed identity. If a managed identity
                        // is not available, it will check if Visual Studio and/or the Azure CLI are
                        // installed locally and see if they are configured with credentials that can
                        // access the vault.
                        config.AddAzureKeyVault(vaultUrl);
                    })
                    .UseStartup<Startup>();
        }
    }

The only change from the starter code is the addition of ConfigureAppConfiguration. This is where we load the vault name from configuration and call AddAzureKeyVault with it.

Next, the controller: Create a new file in the Controllers folder called SecretTestController.cs and paste the following code into it.

    using System;
    using Microsoft.AspNetCore.Http;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.Extensions.Configuration;

    namespace KeyVaultDemoApp.Controllers
    {
        [Route("api/[controller]")]
        public class SecretTestController : ControllerBase
        {
            private readonly IConfiguration _configuration;

            public SecretTestController(IConfiguration configuration)
            {
                _configuration = configuration;
            }

            [HttpGet]
            public IActionResult Get()
            {
                // Get the secret value from configuration. This can be done anywhere
                // we have access to IConfiguration. This does not call the Key Vault
                // API, because the secrets were loaded at startup.
                var secretName = "SecretPassword";
                var secretValue = _configuration[secretName];

                if (secretValue == null)
                {
                    return StatusCode(
                        StatusCodes.Status500InternalServerError,
                        $"Error: No secret named {secretName} was found...");
                }
                else {
                    return Content($"Secret value: {secretValue}" +
                        Environment.NewLine + Environment.NewLine +
                        "This is for testing only! Never output a secret " +
                        "to a response or anywhere else in a real app!");
                }
            }
        }
    }

Run dotnet build in the shell to make sure everything compiles. The app is ready to run. Not to get into Azure. 


## Exercise - Configure, deploy, and run in Azure

We need to create an Azure App Service app, set it up with a managed identity and our vault configuration, and deploy our code.

**Create the App Service plan and app**

Creating an App Service app is a two-step process: First create the plan, then the app.

The plan name only needs to be unique within your subscription, so you can use the same name we've used: keyvault-exercise-plan. The app name needs to be globally unique, though, so you'll need to pick your own.

In Azure Cloud Shell, run the following to create an App Service plan:

    az appservice plan create \
        --name keyvault-exercise-plan \
        --sku FREE \
        --location centralus \
        --resource-group learn-561b1876-d72b-4630-b4e9-a95fdee45869

Next, run the following command to create the Web App that uses the App Service plan you just created:

    az webapp create \
        --plan keyvault-exercise-plan \
        --resource-group learn-561b1876-d72b-4630-b4e9-a95fdee45869 \
        --name <your-unique-app-name>

**Add configuration to the app**

For deploying to Azure, we'll follow the App Service best practice of putting the VaultName configuration in an application setting instead of a configuration file. Run this command to create the application setting:

    az webapp config appsettings set \
        --resource-group learn-561b1876-d72b-4630-b4e9-a95fdee45869 \
        --name <your-unique-app-name> \
        --settings 'VaultName=<your-unique-vault-name>'

**Enable managed identity**

Enabling managed identity on an app is a one-liner — run this to enable it on your app:

    az webapp identity assign \
        --resource-group learn-561b1876-d72b-4630-b4e9-a95fdee45869 \
        --name <your-unique-app-name>

From the JSON output that results, copy the principalId value. PrincipalId is the unique ID of the app's new identity in Azure Active Directory, and we're going to use it in the next step.

**Grant access to the vault**

The last step before deploying is to assign Key Vault permissions to your app's managed identity. Use the principalId value you copied from the previous step as the value for object-id in the command below. Running this command will grant Get and List access:

    az keyvault set-policy \
        --secret-permissions get list \
        --name <your-unique-vault-name> \
        --object-id <your-managed-identity-principleid>


**Deploy the app and try it out**

All your configuration is set and you're ready to deploy! The below commands will publish the site to the pub folder, zip it up into site.zip, and deploy the zip to App Service.
You'll need to *cd* back to the KeyVaultDemoApp directory if you're not still there.

    dotnet publish -o pub
    zip -j site.zip pub/*

    az webapp deployment source config-zip \
        --src site.zip \
        --resource-group learn-561b1876-d72b-4630-b4e9-a95fdee45869 \
        --name <your-unique-app-name>
        
The deployment may take a minute or two to complete. Once you get a result that indicates the site has deployed, open https://<your-unique-app-name>.azurewebsites.net/api/SecretTest in a browser. The app will take a moment to start up for the first time on the server, but once it does, you should see the secret value, reindeer_flotilla.
    
When you're working in your own subscription, it's a good idea at the end of a project to identify whether you still need the resources you created. Resources left running can cost you money. You can delete resources individually or delete the resource group to delete the entire set of resources.

To cleanup your Cloud Shell storage, delete the KeyVaultDemoApp directory.

Next steps

If this was a real app, what would come next?

   - Put all your app secrets in your vaults! There's no longer any reason to have them in configuration files.
   - Continue to develop the application. Your production environment is all set up, so for future deployments to it you don't need to repeat all the setup.
   - To support development, create a development-environment vault that contains secrets with the same names but different values. Grant permissions to the development team and configure the vault name in the app's development-environment configuration file. Configuration depends on your implementation: for ASP.NET Core, AddAzureKeyVault will automatically detect local installations of Visual Studio and the Azure CLI and use Azure credentials configured in those applications to sign in and access the vault. For Node.js, you can create a development-environment service principal with permissions to the vault and have the app authenticate using loginWithServicePrincipalSecret.
   - Create additional environments for purposes like user acceptance testing.
   - Separate vaults across different subscriptions and/or resource groups to isolate them.
   - Grant access to other environment vaults to the appropriate people.



