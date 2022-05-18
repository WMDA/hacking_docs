# Wireshark

A tool for creating and analysing PCAPs (network packet capture files).

## Overview

First page is to select interface. Clicking on the green ribbion filters what is captured. 

Next page is the main window, we can capture packets or load a pcap file.

The information displayed is 

```
Packet number
Time
Source (source IP)
Destination (Destination IP)
Protcol
Length
Packet info (dsource port to destination port)
```

Protocols I have seen on my wireshark

```
TLSv1 (Transport Layer Security) = SSL  
TCP (Transport control protocol)
DNS = DNS quiery
OCSP = Online certification process, maintains security of the servers.
QUIC =  a low-latency transportation protocol often used for apps and services that require speedy online service.
PPP LCP - operates in the data link layer. It is responsible for establishing, configuring, testing, maintaining and terminating links for transmission
SSDP = discovers Plug & Play devices used by small networks
```

Color
``` 
Black = Bad TCP and errors
Red = RST flags and aborted scans
light blue = TCP, UDP
light yellow = ARP
light green = HTTP
light pink = ICMP
Grey = TCP syn
```

## Collection Methods

How to collect packets:

- Taps. Physical implant on or between cables  
- MAC flooding. Stress the switch to fill the CAM table. Once filled the switch will no longer accept new MAC addresses so to keep the network alive it will send put packets to all ports of the switch.
- ARP poisoning. Redirect traffic from the hosts to the attacker machine. 

## Filtering packets

Can be done by filtering packets at the start or displaying filters to begin with. Displaying filters is easy and will be covered.

Wireshark supports basic logical operators for filtering (|| && etc) for display filters.

Basic syntax for display filters is filter by service or protcol (ip, tcp etc) then a . then a whatever is being filtered i.e address, MAC address etc.

To filter by IP addresses
```ip.addr==<ip address>```

Can also filter by ip source and ip destination

```ip.src==<source Ip``` and ```ip.dst==<dst ip>```

Filtering by protocol:

```tcp.port==<port number>``` (useful when tracking tracking trying to keep track of unusual ports)
```udp..port==<port number>```

## Inspecting packets
[OSI MODEL ](https://assets.tryhackme.com/additional/wireshark101/12.png "Text to show on mouseover")

Double click on a packet to inspect it. It will list the details in the TCP/IP model (physical, data link, network, transport, application).

First layer is the frame layer and is the physical layer. Gives information on the physical layer such as time frame arrived and interface etc.

Second layer is the data link layer and gives information on MAC addresses. 

Third layer is the network layer and gives information on the IP(v4) addresses.

Fourth layer is the network layer and gives information on protcol (UDP/TCP), with destination and source ports. Also shows any protocol errors.

Fifth layer is the application layer and shows details of specific protocols such as http etc as well any data (maybe encripyted done by the presentation layer in the OSI model.)

## ARP packets

Address resolution protocol is a layer 2 protocol that links IP addresses to MAC addresses. 
There are two types of ARP packets, requests (Broadcast) and response.

Wireshark will identify the device, so can check for unfamilar devices on the network. 

Most important part of the ARP packet located in the address resolution protocol: 

- The opcode. This tells whether the request is request (1) or reply (2)
- Target mac address (brodcast will all be Fs)
- Sender mac address 
- Sender ip address 

## ICMP 

ICMP or Internet Control Message Protocol is used to analyze various nodes on a network. Used by ping and traceroute.

Like ARP has request and reply.

Most important parts of the package:

- Type. 8 is request and 0 is reply.
- Timestamp 

## TCP

TCP packets need to be looked together rather than individually.

Common thing to see on TCP is the threeway hand shake. If this is out of order of rst flags thrown in then something suspiciou is happening, like an nmap scan.

Import parts of TCP packets.

- In the syn packet, the sequence and acknowledgment number. If the acknowledgment number is 0 then the port is closed. 

## DNS

Keep in mind query-response, dns-servers only and UDP. 

Import parts of packages

- For DNS query. Look at where the protocol orginates from, i.e UDP port 53. If it was from TCP then this is suspicious. Also look at what is being queried. 
- DNS response. Look at the answers part to see what the answer is.

## HTTP

Analysing HTTP packets is useful to spot SQLi, web shells etc.

Easiest to analyse.

Statistics > Protocol Hierarchy (see percentage of requests), file > Export Objects > HTTP and Statistics > Endpoints can help to organise packets to identify discrepancies in packet captures.

## HTTPS

Before sending encrypted information the client and server need to agree upon various steps to secure the tunnel.

1) Client and server agree on protocol version. 
2) Client and server select a cryptographic algorithm
3) The client and server can authenticate to each other (optional)
4) Create a secure tunnel with a public key


More on the packet process.

1. The client sends a client hello packet showing the SSLv2 Record Layer, Handshake Type, and SSL Version.
2. The server responds with a server hello packet with similar information as the Client Hello packet as well as session details and SSL certificate information.
3. The client then sends a client key exchange packet which determines the public key to use to encrypt messages between client and server.
4. The server sends a confirmation packet and creates a secure tunnel. Everything is now encrpyted.	

To see the un-encrypted data the rsa key has to be loaded into wireshark. Load the RSA key by going to Edit > Preferences > Protocols > TLS > RSA keys list edit >[+] 


Enter:

```
IP Address: 127.0.0.1

Port: start_tls

Protocol: http

Keyfile: RSA key location
```
## Zerologin example

In the example pcap there are lots of unusual protocols such as DCE/RPC(allows programmers to write distributed software as if it were all working on the same computer) and EPM (end point mapper for the DCE/RPC protocol).

All the requests are coming from the IP address 192.168.100.128 so most likely the attacker. So filter the requests to this IP address. 

When analyzing PCAPS be aware of IOCs or Indicators of Compromise that particular exploits may have with them. The Zerologon exploit uses multiple RPC connections, and DCERPC requests to change the machine account password which is what the pcap shows. There is also a lot of SMB2/3 traffic and DRSUAPI traffic, which represents secretsdump to dump hashes. Secretsdump abuses SMB2/3 and DRSUAPI to do dump hashes.

So the order is the zerologon is used to change the machine account password to logon and then a secretdump to dump hashes.

## INE questions.

Follow TCP stream to look for traffic between Web-Browser and Server. Http stream 