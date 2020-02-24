# Windows shares

It can be used on clients and servers to provide authentication, file sharing, printer management and other features.

A Windows machine can share a file or a directory on the network; this lets local and remote users access the resource and, possibly, modify it.

Starting from Windows Vista, users can choose to share a single file or use the Publicdirectory. When sharing a single file, they can choose local or remote users to share the file with.When using the Public directory, they can choose which local users can access the files on the share, but they can only allow everyone or no one in the network to access the share.

An authorized user can access shares by using Universal Naming Convention paths (UNC paths).

    \\ServerName\ShareName\file.nat
    
There are also some special default administrative shareswhich are used by system administrators and Windows itself:

  •\\ComputerName\C$  lets an administrator access a volume on the local machine. Every volume has a share (C$, D$, E$,etc.)
  •\\ComputerName\admin$  points to the windows installation directory
  •\\ComputerName\ipc$ is used for inter-process communication. You cannot browse it via Windows Explorer
  
  Accessing a share means having access to the resources of the computer hosting it. So, badly configured shares exploitation can lead to:•Information disclosure•Unauthorized file access•Information leakage used to mount a targeted attack
