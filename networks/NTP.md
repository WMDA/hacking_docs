# NTP
The Network Time Protocol (NTP) is a networking protocol for clock synchronization between computer systems over packet-switched, variable-latency data networks. 

- UDP protocol.
- port 123
- ntp.conf is the config file generally located in the /etc/ directory

```nmap -sU -sV --script "ntp* and (discovery or vuln) and not (dos or brute)" -p 123 {IP}```