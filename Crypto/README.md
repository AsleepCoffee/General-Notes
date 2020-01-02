## Cryptography

<details>
   <summary>XOR</summary>
   <br>
   
   ### XOR (^)

The ability for XOR to reverse itself makes it massively important part of crypto.

0 ^ 0 == 0

0 ^ 1 == 1

1 ^ 0 == 1

1 ^ 1 == 0

</details>

---------------------------------------------------------------------------------------------

<details>
   <summary>Key Ciphers</summary>
   <br>
   
  ### Ciphers

- Symmetric -- Both sides share the same key

  Can use either stream or block ciphers.

   - Stream -- Encrypts data byte-by-byte
   - Block -- Encrypts data block-by-block 
   
- Asymmertric  -- (aka public key) Each side has their own private key and private key
   - Recipients public key is used to encrypt, and their private key is used to decrypt.
   - Typically used to transfer symmetric keys rather than data due to proformance.
   
   ## Two main uses of Asymmertric
  
  Two of the best-known uses of public key cryptography are:

   - Public key encryption: in which a message is encrypted with a recipient's public key. The message cannot be decrypted by anyone who does not possess the matching private key, who is thus presumed to be the owner of that key and the person associated with the public key. This is used in an attempt to ensure confidentiality.
    
   - Digital signatures: in which a message is signed with the sender's private key and can be verified by anyone who has access to the sender's public key. This verification proves that the sender had access to the private key, and therefore is likely to be the person associated with the public key. This also ensures that the message has not been tampered with, as a signature is mathematically bound to the message it originally was made with, and verification will fail for practically any other message, no matter how similar to the original message.
  
</details>

---------------------------------------------------------------------------------------------

</details>
<details>
   <summary>Hashes</summary>
   <br>
  
  ### Hashes

 - takes input and outputs a fixed size output called a digest.
 - Due to any size input and fixed out, collisions are a going to happen
 - Strength of a hash algorithm is in how hard it is to produce a collision.
 - Hash functions 
    - MD5
    - SHA1
    - SHA2
</details>

---------------------------------------------------------------------------------------------

<details>
   <summary> MACs</summary>
   <br>
  
  ### MACs (Message Authentication Codes)
  
  - based on hashes that allow for message authentication. Ensures message and MAC was not tampered with.
  - Shared key is used for the construction and validation of the MAC.
  
  - Most well known MAC is the HMAC and is based around the hash of your choosing.
  - HMAC(key, message) = hash(key + hash(key + message))
  - Keys are padded seperately in each run of the hash algorithm.
</details>

---------------------------------------------------------------------------------------------

<details>
   <summary> Encryption Algorithms </summary>
   <br>
    
  ## Keys
  
   Key length is equal to the number of bits in an encryption algorithm’s key. Longer the better. But does not mean better security. The key length determines the maximum number of combinations required to break an encryption algorithm. If the key length is 40 bits long, then there are 240 possible keys.
  
 ## Algorithms
 
 - AES (Advances Encryption Standard)
   Symmetric
   Key Length: 128, 192, 256
 
 - CAST5: 
   Symmetric
   Key Length: 128
   
</details>
    
---------------------------------------------------------------------------------------------

<details>
   <summary>Modes of operation</summary>
   <br>
   
A block cipher mode of operation is an algorithm that uses a block cipher to provide information security such as confidentiality or authenticity.

   - Block cipher mode of operation
      - ECB (Electronic Codebook)
        Each block is independently encrypted, meaning each same two blocks will have the same cipher text.
        
      - CBC (Cipher Block Chaining)
         Most common. Each plaintext block is XORed with the ciphertext of the previous block before encryption. Reverse is preformed for decryption. The first block is XORed with the IV (Initilization Vector)
</details>

---------------------------------------------------------------------------------------------

<details>
   <summary>Signature Algorithms
 </summary>
   <br>

 Used to for secure data transmission.
 
 RSA: 
 
 DSA(Digital Signatrure Algorithm):
 
 ECDSA(Elliptic Curve Digital Signature Alogrithm):

</details>
    
---------------------------------------------------------------------------------------------

<details>
   <summary>Key Establishment</summary>
   <br>


</details>

---------------------------------------------------------------------------------------------

<details>
   <summary>Key Derivation</summary>
   <br>
</details>

---------------------------------------------------------------------------------------------

<details>
   <summary>Key Wrap Modes of Operation</summary>
   <br>
</details>

---------------------------------------------------------------------------------------------

<details>
   <summary>Cipher suite</summary>
   <br>
  A cipher suite is a set of algorithms that help secure a network connection that uses TLS/SSL.
   
   An example of a cipher suite name: TLS_RSA_WITH_AES_128_GCM_SHA

  - TLS defines the protocol that this cipher suite is for.
  
  - RSA indicates the key exchange algorithm being used.
  
  - AES_128 indicates the block/stream cipher being used to encrypt the message stream...
  
  - GCM The block cipher mode of operation.
  
  - SHA indicates the hash algorithm which is used to authenticate a message.

</details>

