# Searchsploit 

## Search for exploits

Searches the ExploitDB website (https://www.exploit-db.com/) for exploit from CLI.

Other websites:
- https://nvd.nist.gov/vuln/search
- https://cve.mitre.org/  

CVEs (Common Vulnerabilities and Exposures) are structured:
CVE-YEAR-NUMBER

## Searchsploit

```
searchsploit [options] term1 [term2] ... [termN]

Useful flags:

-v verbose output.
-w shows urls to ExploitDB rather than local path.
```

# Other useful tools

- whois (query who a domain name is registered to)
- traceroute (traces packet route)
- dig (manually query recursive DNS servers for information) 

## tcpdump

tcpdump (https://danielmiessler.com/study/tcpdump/)
- Analyses network traffic
- Packet analyser
- Prints  out a description of the contents of packets on a network interface   

Example of usage
```
tcpdump ip proto \\icmp -i [interface]
```

This searches for icmp (pings) to a interface
