# nmap 

## Flags

~~~
-sS 
Stealthy scan, quick,half scan (doesn't open full 
connection). SYN scans.

-sU 
Scans for UDP ports as UDP ports are often ignored.

-O 
Enable os detection.

-sV 
Probes open ports and determines service/version. 

-sC 
performs a script scan with default scripts.

--traceroute 
Determines the port and protocol most likely 
to reach target.

-A 
Enables -O -sV -sC and --traceroute (aggressive, 
can be detected easier)

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
Normal output

-T<0-5> 
Higher is faster but more noisey.

-p 
Port range to be scanned. 
(-p 80 scans port 80. 
-p[-1024] scans all ports <= 1024)

-p- 
Scans all ports.

--script 
Selects nmap script to use
(--script=vuln uses vuln scripts)
~~~

## nmap scan types

Three basic types, TCP connect scans (-sT), SYN "Half-open Scans" (-sS) and UDP scans (-sU).

Less common port scans, TCP Null Scans (-sN), TCP FIN Scans (-sF) and TCP Xmas Scans (-sX)


