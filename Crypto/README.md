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
   <summary>Ciphers</summary>
   <br>
   
  ### Ciphers

- Symmetric -- Both sides share the same key
   - Stream -- Encrypts data byte-by-byte
   - Block -- Encrypts data block-by-block
   
- Asymmertric  -- Each side has their own private key and private key
   - Recipients public key is used to encrypt, and their private key is used to decrypt.
   - Typically used to transfer symmetric keys rather than data due to proformance.
   
   - Block cipher modes
      - ECB (Electronic Codebook)
        Each block is independently encrypted, meaning each same two blocks will have the same cipher text.
      - CBC (Cipher Block Chaining)
         Most common. Each plaintext block is XORed with the ciphertext of the previous block before encryption. Reverse is preformed for decryption. The first block is XORed with the IV (Initilization Vector)
</details>

---------------------------------------------------------------------------------------------

</details>
<details>
   <summary>Hashes</summary>
   <br>
  
  ### Hashes

 - takes input and outputs a fixed size output.
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
   <summary>SSL/TLS</summary>
   <br>
   <p>https://tls.ulfheim.net/</p>


</details>
