Provides crypto prvacy and auth.

PGP is a windows tool commonly used to encrypt files, apply digital signatures and enforce integrity. 

PGP and similar products follw the OpenPGP standard for encrypting and decrypting files.

Public key crypto

includes system which binds the public key to an email address.

A web of trust model is used over PKI model with CA's signing public keys.

Web of trust has made PGP widespread bc ez, fast and inexpensive to use. 

auth and integrity checks.

Works as long as the public key used to send a message belongs to the intended addressee.


-

PGPkey parts:

- name of the owner
- # values comprising of the key
- what the key is used for
- the algorth, the key is used with E.G RSA, DSA
- maybe an expiration date

Similar to X.509 cert, but a pgp key is not a cert (no one has signed it yet).


To use: 

You need to store: 

Your secret key (encrytped witha passphrase)

your public key and the public key of your friends and and associates (stored in clear)

PGP puts them in a keyring


PGP can sign a document or a hash version of the document. NMore efficient that signing everything plaintext.

Encrypt message: PGP will gen a Symmetic key, encrypt that with the public key. The message is encrypted with the symmetric key. Allows to have many addresses for the same message, just use the correct public key. 


PGP used algorithms:

RSA, DSS, Diffie-Hellman for public key encryption

3DES, IDEA, CAST-128 for symmetic key encryption 

SHA-1 for hashing

ZIP for compression









