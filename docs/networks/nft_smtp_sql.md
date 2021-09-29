# Networks

## NFT

Network file system:
- Shares files and directories on a remote system as if they were on a local system.
- Part of the file system is mounted and can be accessed by clients.
- Files have privileges like local systems.
- By default root-squashing is enabled.
- Remote root users are assigned user “nfsnobody” when connected, which has the least local privileges. 

How NFT works:
- First client requests to mount a directory from a remote machine.
- Mount service connects to the NFSD (NFS daemon) using RPC. 
- Server checks if user has permission to mount the directory.
- Returns file handler which uniquely identifies each file/directory. 
- Server needs: file handler, name of file, user ID, group ID.
- When a file is transfered into the mount it is automatically placed in the client.

NFTs work on all operating systems.

### NSF common

- consists of numerous modules (mount and showmount are two) for nfs.

Mounting nfs-shares

~~~
mount -t nfs IP:share [directory] -nolock

-t nfs type of device to mount, specifies nft.
IP:share IP Address NFS server, and name of share to mount
directory to share to.
-nolock Specifies not to use NLM locking
~~~

showmount - show mount information for an NFS server

~~~
/usr/sbin/showmount [options] [IP]

options
-a List both the client hostname or IP address and mounted directory in host:dir format.
-d List only the directories mounted by some client.
-e Show the NFS server's export list.
~~~

### NSF root access

NFS Access ->

Gain Low Privilege Shell ->

Upload Bash Executable to the NFS share ->

Set SUID Permissions Through NFS Due To Misconfigured Root Squash ->

Execute SUID Bit Bash Executable ->

ROOT ACCESS


## SMTP