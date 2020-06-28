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
















