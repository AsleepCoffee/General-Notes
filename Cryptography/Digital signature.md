Mechanism that allows to auth a message. It proves that the message is effectively coming from a given sender. Provides the means to verify that the sender of a message really is who he's claiming to be. The signature on a document cannot be reproduced for other documents; it is bound to the signed doc or a representation of it.

An example of Alice wanting to send Bob a message: 

![Capture](https://user-images.githubusercontent.com/46513413/89238734-140ea880-d5c5-11ea-9019-271806556200.PNG)


Reasons for reproducing the message digests are:

- Verify integrity

- Digital sig is applied to the digest because it is smaller than the message.

- Hash algorithms are much faster than any encryption. 
























