## Cryptography

### XOR (^)

The ability for XOR to reverse itself makes it massively important part of crypto.

0 ^ 0 == 0
0 ^ 1 == 1
1 ^ 0 == 1
1 ^ 1 == 0


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

### Hashes

 - takes input and outputs a fixed size output.
 - Due to any size input and fixed out, collisions are a going to happen
 - Strength of a hash algorithm is in how hard it is to produce a collision.
 - Hash functions 
    - MD5
    - SHA1
    - SHA2
    
### MACs (Message Authentication Codes)
  
  - based on hashes that allow for message authentication. Ensures message and MAC was not tampered with.
  - Shared key is used for the construction and validation of the MAC.
  
  - Most well known MAC is the HMAC and is based around the hash of your choosing.
  - HMAC(key, message) = hash(key + hash(key + message))
  - Keys are padded seperately in each run of the hash algorithm.
  
### Padding
