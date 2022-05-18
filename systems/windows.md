# Windows 

cmd commands
~~~
type (reads file out to terminal)
~~~

- Windows passwords are stored at
~~~
C:\Windows\System32\config
~~~

- Windows uses NTLM (Windows New Technology LAN Manager) hashing for local passwords.
- NTLM is cracked in john the ripper with

~~~
john -w=/usr/share/wordlists/rockyou.txt --format=NT <file with hashes> 
~~~

- Kerberos (computer-network authentication protocol) is used for network authentication.
use Mimikatz in metasploit for this

~~~
load kiwi
~~~

- LSASS (Local Security Authority Subsystem Service) is a process in windows that is
resonsible for enforcing security (authentication etc)