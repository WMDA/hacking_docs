# SNMP

Simple Network Management Protocol (SNMP):
- UDP
- Is a way for different devices on a network to share information with one another. 
- It allows devices to communicate even if the devices are different hardware and run different software.
- A protocol used to monitor different devices in the network (like routers, switches, printers, IoTs...).
- Comes in SNMPv1 and SNMPv2 both send cleartext messages (SNMPv3 doesn't)
- Stores information in a structure called a Management Information Base (MIB)
- To retrieve information from machines running SNMP, a requester will send a GET request to the machine, along with a string to authenticate itself. 
- SNMPv1 uses two different strings, called community strings, for authentication with machines. 
- A read only string is for read-only information, and the read-write string is for modifying information.
- Community string is easy to crack

enumerating snmp (version number etc)
```
nmap -p 161 -sU -sV <IP>
```

brute forcing community string
```
nmap -sU -p 161 --script snmp-brute --script-args snmp-brute.communitiesdb=/usr/share/wordlists/seclists/Discovery/SNMP/common-snmp-community-strings.txt <ip>
```

getting information once have community string
```snmpwalk -v <snmp version number> -c <public string>```