# SAML - Security Assertion Markup Language

 XML-based markup language for security assertions.

A protocol for authenticating web apps. 

SAML allows federated apps and org to trust and communicates with each others users.

The glue that holds web based SSO together.

RP/IDP initiated. Where the login starts. Start RP/SP that then sends SAML request to IDP, auth, that then returns SAML assertation back to RP/SP VS Starting at IDP, auth, that then returns SAML assertation back to RP/SP.

**SAML Assertion** - A message asserting a user’s identity and often other attributes, 
  sent over HTTP via browser redirects. This was the wristband itself.
  
**SAML Request** - This request says "User X is trying to login, but they don’t have a SAML assertion yet. Please help them get a SAML assertion, then send them back here.” Only used in SP initiated.

### Example

1.Want to login to Lego.ca (SP)
     
    -> Click "sign in".
       a. SP sends SAML request to bricks.ca
    -> I am now redirected to bricks.ca (Lego.ca trusted IDP) and presented with a login form.
    -> Enter creds and click login 
        a. Login info is checked against the IDP. The issues a SAML assertion that is sent back to lego.ca 
           to prove this message came from the IDP that lego.ca trusts.
    -> I am redirected back to Lego.ca. Logged in.
    -> If multiple SPs are configured to this IDP, then I could go to megablocks.ca and be logged in.
    

# IDP configuration

 The IdP needs to be configured so it knows where and how to send users when they want to log in to a specific SP. 

 **EntityID** - A globally unique name for the SP. Formats vary, but it’s increasingly common to see this value formatted as a URL.

    Example: <EntityDescriptor entityID="https://lego.ca/home">

**Assertion Consumer Service (ACS)** - The URL location where the SAML assertion is sent.

    Example: https://lego.ca/saml/auth/

**ACS Validator** - A security measure in the form of a regular expression (regex) that ensures the SAML assertion is sent to the correct ACS. This only comes into play during SP-initiated logins where the SAML request contains an ACS location, so this ACS validator would ensure that the SAML request-provided ACS location is legitimate.

    Example: ^https:\/\/lego\.cca\/saml\/auth\/$

**Attributes** - The number of and format of attributes can vary greatly. There’s usually at least one attribute, the nameID, which is typically the username of the user trying to log in.

    Real Examples:
    NameID Format
    NameID Attribute

**RelayState** - Not required. Deep linking for SAML. This tells the SP where to take the user once they’ve successfully logged in.

    Real Example: https://lego.ca/account
    Beer Example: “After the Beer Tent approves of your wristband, ask for a lager.”

**SAML Signature Algorithm** - SHA-1 or SHA-256. Less commonly SHA-384 or SHA-512. This algorithm is used in conjunction with the X.509 certificate mentioned below.


# SP Configuration

 So the SP/RP can proces information provided by the IDP and set at the SP.
 
 **X.509 Certificate** - A certificate provided by the IdP, used to verify the public key as passed by the IdP in the metadata of the SAML assertion. It allows the SP to verify the SAML assertion is actually coming from the IdP it trusts. SAML assertions are usually signed, however SAML requests can also be signed. Typically, it’s downloaded or copied from the IdP and configured by uploading or pasting it to into the SP.

**Issuer URL** - Unique identifier of the IdP. Formatted as a URL containing information about the IdP so the SP can validate that the SAML assertions it receives are issued from the correct IdP.

    Example: <saml:Issuer>https://bricks.ca/saml2/idp/metadata.php</saml:Issuer>

**SAML SSO Endpoint / Service Provider Login URL** - An IdP endpoint that initiates authentication when redirected here by the SP with a SAML request.

**SAML SLO (Single Log-out) Endpoint** - An IdP endpoint that will close the user’s IdP session when redirected here by the SP, typically after the user clicks “Log out.”

    Real Example: https://bicks.ca/logout
 
 
 
 
 
 
 
 
 
 
 
 
 
