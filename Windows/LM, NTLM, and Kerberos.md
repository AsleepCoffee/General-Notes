
[netsec](https://netsec.ws/?p=314)

All are windows mechanisms for authenticating network services in a windows environment.

Release order: LM -> NTLM -> NTLMv2 -> Kerberos


**LM (Lan Manager) hashes:**

Hash is DES.
Windows procedure to compute Hash: 
1. password is transformed to upper case 
2. Add null characters until it is 14 bytes long
3. Split the password into 2 blocks (7 byte chunks plus a byte of parity)
4. Each of the 2 keys is used to encrypt the fixed string "KGS!@#$%" (8 byte ciphertext)
5. The 2 ciphertext are concatenated to form a 16-byte value. 

Originally windows passwords shorter than 15 characters were stored in the Lan Manager (LM) hash format. Some OSes such as Windows 2000, XP and Server 2003 continue to use these hashes unless disabled. Occasionally an OS like Vista may store the LM hash for backwards compatibility with other systems. This hash is simply terrible. It includes several poor design decisions from Microsoft such as splitting the password into two blocks and allowing each to be cracked independently. Through the use of rainbow tables which will be explained later it’s trivial to crack a password stored in a LM hash regardless of complexity. This hash is then stored with the same password calculated in the NT hash format in the following format: ::::::

**NT hashes (A.K.A NTLM):**

Windows procedure to compute Hash: 
1. the password is converted to UNICODE
2. MD4 is then used to get a 16-byte long hash

It addresses some LM flaws, but is still considered to be weak. 

However, the NTLM response is sent together with the LM response, most of the time.

Newer Windows operating systems use the NT hash. There is no significant weakness in this hash that sets it apart from any other cryptographic hash function. Cracking methods such as brute force, rainbow tables or word lists are required to recover the password if it’s only stored in the NT format.



            SAM (Security Accounts Manager) file will contain system hashes. 

            Administrator:500:611D6F6E763B902934544489FCC9192B:B71ED1E7F2B60ED5A2EDD28379D45C91:::
                              ^              LM              ^ ^             NT               ^
                              |                              | |                              |



Note that users who log into a computer in a domain have their hashes stored in memory until the computer is shutoff or rebooted. This means any user that has logged on prior to a reboot can have its credentials/hashes stolen from memory via [Mimikats](https://github.com/Kahvi-0/Tools-and-Concepts/blob/master/Windows/Mimikatz.md)

## NTLM vs. NTLMv1/v2 vs. Net-NTLMv1/v2

https://medium.com/@petergombos/lm-ntlm-net-ntlmv2-oh-my-a9b235c58ed4#:~:text=LM%2D%20and%20NT%2Dhashes%20are,confusingly%20also%20known%20as%20NTLM.&text=NTLMv1%2Fv2%20are%20challenge%20response,through%20Brute%20Force%2FDictionary%20attacks.

NTLMv1/v2 is a shorthand for Net-NTLMv1/v2 and hence are the same thing.

NTLM hashes are stored in the Security Account Manager (SAM) database and in Domain Controller's NTDS.dit database. Can be also obtained using Mimikatz (Windows >= 8.1 you can get NTLM hashes from memory). Some tools just give you the NT hash (e.g. Mimikatz) and that's fine: you can still Pass-The-Hash with just the NT hash.

Net-NTLM hashes are used for network authentication (they are derived from a challenge/response algorithm and are based on the user's NT hash).

From a pentesting perspective:

    You CAN perform Pass-The-Hash attacks with NTLM hashes.

    You CANNOT perform Pass-The-Hash attacks with Net-NTLM hashes.

**You get Net-NTLMv1/v2 (a.k.a NTLMv1/v2) hashes when using tools like Responder or Inveigh.**

## How the LM/NTLMv1 authentication protocol works

Used to auth client to a server, where the server has some way to verify the creds sent by the client. 

Same for both:

1. Client sends a request for authentication.

2. Server sends a 8 byte (random value) 

3. Client encrypts the challenge using the password hash and sends it back as a response.

Step 3 is the most important part for attacks, this what is attempted to be captured. 

How the client message is built: 

 1. The 16-byte hash is padded with 5 null bytes to make it 21 bytes string
 2. The 21 bytes string is split in 3 blocks, 7 bytes each +1 parity byte. (now 24 bytes total)
 3. Each block will be the key to encrypt the server challenge senf during step 2 of the authentication protocol.
    - In an attack scenario, we impersonate the server and choose the challenge.
    - Each block encrypts the server challenge with DES
 4. Each block now together make up the step 3 client challenge response.

More information: http://davenport.sourceforge.net/ntlm.html#theType3Message



















