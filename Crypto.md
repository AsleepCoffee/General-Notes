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
   
   - Block cipher modes
      - ECB (Electronic Codebook)
        Each block is independently encrypted, meaning each same two blocks will have the same cipher text.
      - CBC (Cipher Block Chaining)
         Most common. Each plaintext block is XORed with the ciphertext of the previous block before encryption. Reverse is preformed for decryption.
