# tcpdump

tcpdump (https://danielmiessler.com/study/tcpdump/)
- Analyses network traffic
- Packet analyser
- Prints  out a description of the contents of packets on a network interface   

Example of usage
```
tcpdump ip proto \\icmp -i [interface]
```

This searches for icmp (pings) to a interface