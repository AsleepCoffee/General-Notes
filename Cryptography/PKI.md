Public key infrastructure

A set of hardware, software, people, policies, and procedures needed to create, manage, store, distribute, and revoke digital certificates.

In crypto, PKI relies on a number of elements to make sure the ID of someone or an ORG is effectively certified and verified by means of a CA. 

User ID must be unique for each CA.

PKI is not the same as public key algorithms.

X.509: stabndard for public key certificates. 

   used by protocols such as SSL/TLS, SET, S/MIME, IPsec, and more.

**Public key certificate**

Public key certificate binds a public key with an identity by means of digital signature. Certificate can be used to verify that a public key belongs to someone. 

In PKI the signature assuring the ID will be of a CA. The CA acts as a trusted third party. Those who wants to verify the ID has to trust the CA. The signature on a cert are attestations by the certificate signer that the identitiy information and the public key are bound together.

**Example with SSL:**

SSL cert has 2 purposes: 

1. Provide proof of identity. 

2. Provide a secure channel for transmitting data.


A chain exists: Root CA's sign certs of intermediate CA's that sign SSL certs of websites.

Someone visits a website using SSL and is presented with a sert signed by a CA. They can validate the validity of the SSL cert by validating its signature.

To validate a signature, the public key of the signer is required: This is located in the web browser. Web browsers store the public keys of the root CA's.

Authenticity and confidentiality of SSL:

Authenticity is verified by verifying the validity of the cert (validate the digital signature) 

Confidentiality is achived by handshaking initial channel parameters encrypted with the SSL certified public key of the website. 


**Contents of a typical digital cert:**

![Capture](https://user-images.githubusercontent.com/46513413/89237086-42d65000-d5c0-11ea-8b12-fb667affda23.PNG)


**Common filename extensions for x.509-certs are:**

.DER - (Distinquished Encoding Rules) encoded cert

.PEM - Privacy Enhanced mail base64 encoded DER cert, enclosed between "---begin certificate---" and "---end certificate---"

.P7C - PKCS#7 SignedData structure without data,just certificates(s) or CRL(s) (cert revocation list).

.PFX or .p12 - PKCS#12, may contain certificates(s) (public) and private keys (password protected).





