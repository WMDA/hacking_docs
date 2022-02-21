# Network Services

## SMB

Server Message Block protocol: 

- A client-side protocol used for sharing files, accessing printers, serial ports and other network resources.
- Server makes file systems and other resources available to client. 
- Once connected client can open/read/write 
- A response-request protocol (transmits multiple messages between client and server).
- The directories on the remote hosts made available via SMB are called “shares.”
- Communicates over TCP/IP (Run over NetBIOS), NetBEUI or IPX/SPX.
- Port 139 (older versions running over NetBIOS) /port 445 (dedicated port for newer versions).
- SMB is windows.
- Samba is unix.


### Enumerating SMB

~~~
enum4linux [-OPTIONS] IP
~~~
- Enumerates SMB on both windows and linux

- Flags  
-U (get userlist)  
-M (machine list)  
-N (namelist dump)  
-P (get password policy information)  
-G (get group and member list)  
-d (be detailed, applies to -U and -S)  
-u (specify username to use (default ""))    
-p (specify password to use (default ""))   
-r (enumerate users via RID cycling)   
-o (Get OS information)  
-i (Get printer information)  
-n (Do an nmblookup (similar to nbtstat))  

-a Does everything (-U -S -G -P -r -o -n -i)  

### Exploiting SMB

~~~
smbclient \\\\IP\\share [-options]
~~~

or 


~~~
smbclient //<ip>/<share>
~~~

Connects to SMB servers

- Flags  

-U (To specify the user, needs to be in)  
-p (To specify the port)  
-N (No password)

To see if "Anonymous" login use -U "Anonymous" and skip password

## Telnet

Telnet:

- An application that can connect and excute remote commands on a remote machine running telenet.
- Telenet establishes connection and becomes a virtual terminal.
- Mainly replaced by ssh.
- No security everything is plain text.
- port 23 over TCP/UDP.

Connecting to telenet

~~~
telnet [ip] [port]
~~~

Once inside telenet all commands need to start with .RUN

## FTP 
	
File transport protocol:
- A file transfer protocol over networks
- Uses a client server model and relay commands 
- Uses a command (control) channel and a data channel.
- Command channel transmits commands while data channel transmits data.
- Client initiates the session and the server validates the credientials then opens the session.
- Has two types of connections: active connection (the client opens a port and listens. The server is required to actively connect to it) and
passive (the server opens a port and listens (passively) and the client connects to it.)
- Seperation of channels means commands can be sent and data transfered at the same so is efficient. 
- Uses port 21
- Similar to telnet data is plain text.
  
### Connecting to FTP 

~~~
ftp [options] [ip] [optional port]
~~~








