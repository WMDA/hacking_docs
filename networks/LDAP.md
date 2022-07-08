# LDAP 

Lightweight Directory Access Protocol (LDAP) is an open, vendor-neutral, industry standard application protocol for accessing and maintaining distributed directory information services over an Internet Protocol (IP) network.

Application layer protocol

PORT 389

## enumerating LDAP

```nmap -n -sV --script "ldap* and not brute" IP```