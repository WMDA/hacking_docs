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


Simple Mail Transfer Protocol:
- Involved in sending emails.
- SMTP verfies who is sending the email (through the SMTP server), sends outgoing mail and if it fails let the user know.
- Part of a protocol pair with Post Office Protocol (POP)/Internet Message Access Protocol (IMAP).
- Works on port 25 usually.
- Runs on linux/windows.

### POP v IMAP

- POP downloads the servers inbox directly.
- IMAP synchorises with the servers inbox and only downloads new emails.
- IMAP allows for changes on a machine to persist unlike POP.


### How SMTP works

1. The sender connects to the SMTP server of your domain, e.g. smtp.google.com. 
2. This initiates the SMTP handshake and the SMTP session starts.
3. The sender then submits the email to the SMTP server.
4. The SMTP server then checks whether the domain name of the recipient and the sender is the same.
5. The SMTP server of the sender will make a connection to the recipient's SMTP server before relaying the email. 
6. If the recipient's server can't be accessed, or is not available- the Email gets put into an SMTP queue.
7. The recipient's SMTP server verifies the incoming email, by checking if the domain and user name have been recognised. 
8. The recipient's server will then forward the email to the POP or IMAP server.
9. The E-Mail will then show up in the recipient's inbox.

### Enumeration SMTP

SMTP service has two internal commands that allow the enumeration:
- VRFY (confirming the names of users). 
- EXPN (reveals address of user’s aliases and lists of e-mail).

Use metasploit module smtp_version to finger print the server:
- Return server with response code 


Use metasploit smtp_enum with USER_FILE /usr/share/wordlists/SecLists/Usernames/top-usernames-shortlist.txt to return users.


## mySQL

### enumerating mySQL

can use metasploit mysql_sql module

or

https://nmap.org/nsedoc/scripts/mysql-enum.html

or 

https://www.exploit-db.com/exploits/23081


### exploiting mySQL

mysql_schemadump module in metasploit. Dumps mySQL databases.

mysql_hashdump module in metasploit. MYSQL Password Hashdump


