# SAML - Security Assertion Markup Language

 XML-based markup language for security assertions.

A protocol for authenticating web apps. 

SAML allows federated apps and org to trust and communicates with each others users.

The glue that holds web based SSO together.

**SAML Assertion** - A message asserting a user’s identity and often other attributes, 
  sent over HTTP via browser redirects. This was the wristband itself.


1.Want to login to Lego.ca (SP)
     
    -> Click "sign in".
    -> I am now redirected to bricks.ca (Lego.ca trusted IDP) and presented with a login form.
    -> Enter creds and click login 
        a. Login info is checked against the IDP. The issues a SAML assertion that is sent back to lego.ca 
           to prove this message came from the IDP that lego.ca trusts.
    -> I am redirected back to Lego.ca. Logged in.
    -> If multiple SPs are configured to this IDP, then I could go to megablocks.ca and be logged in.
    
