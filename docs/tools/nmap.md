# nmap 

## Commands

~~~
-O 
Enable os detection.

-sV 
Probes open ports and determines service/version. 

-sC 
performs a script scan with default scripts.

--traceroute 
Determines the port and protocol most likely to reach target.

-A 
Enables -O -sV -sC and --traceroute (aggressive, can be detected easier)

-sN
Ping sweep. Switchs off port scans and uses ICMP pinging (or ARP if on same network). 

-v 
verbose

-vv 
verbose level 2

-q 
Decreased verbose level.

-oA 
Outputs normal, XML and grepable format.

-oG 
Grepable output.

-oN 
Normal output.

-T<0-5> 
Higher is faster but more noisey.

-p 
Port range to be scanned (-p 80 scans port 80. -p[-1024] scans all ports <= 1024, -p- scans all ports.).

--script 
Selects nmap script to use (--script=vuln uses vuln scripts)

-f 
Fragments a package to make it smaller and avoid firewalls

-mtu <number>
Fragments a package to make smaller but more control (needs to be multiples of 8)

--badsum 
Generate an invalid checksum. A firewall will respond but a proper TCP/IP stack will drop. 

-Pn
Turns off ping scan (firewalls block pings making nmap think the target is down when it isn't.) Slow.
~~~


## Scan types

SYN scans

- Stealthy scan.
- Quick.
- Half scan (doesn't open full connection). 
- Can bypass older intrusion detection system and is fast.  
- Needs root/sudo permission.
- Unstable services can be brought down by this scan.
- Raw packets.

~~~
-sS 
~~~

UDP scan

- Doesn't rely on hand shake, 
- Cannot tell if port is open or filtered as a open and filtered UDP ports don't send a response back (gets ping back if port is closed).
- UDP ports are often ignored.
- Very slow (20mins for top 1000 ports).
- Sends raw packets.

~~~
-sU
~~~ 

TCP scan

~~~
-sT
~~~ 

NULL/FIN/Xmas scans

- Desgined to bypass firewalls
- Stealthy
- Send out malfomed packages
- Similar to UDP cannot tell if port opened or filtered as both don't respond to malformed packages (a RST will be sent back if port is closed).
- NULL scan: Sends a TCP request with no flags 
~~~
-sN
~~~

- FIN scan sends out with a FIN flag.

~~~
-sF
~~~

- Xmas scan (looks like a xmas tree on wireshark) sends out FIN,PSH and URG flags

~~~
-sX
~~~

## Scipts

- Safe: Won't affect the target
- Intrusive: Not safe, likely to affect the target
- vuln: Scan for vulnerabilities
- exploit: Attempt to exploit a vulnerability
- auth: Attempt to bypass authentication for running services (e.g. Log into an FTP server anonymously)
- brute: Attempt to bruteforce credentials for running services
- discovery: Attempt to query running services for further information about the network (e.g. query an SNMP server).
- Some take arguments 
~~~
--script-args
~~~
- /usr/share/nmap/scripts/script.db contains all scripts info (also https://nmap.org/nsedoc/)