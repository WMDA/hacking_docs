# Proxy

In proxychains file set up the bottom the port. ```socks5          127.0.0.1 1234``` worked for me!!

Then set up a proxy ```ssh -D 1234 -i id_rsa root@10.200.73.200``` easiest way.

Run commands by proxy using 

```proxychains nmap 10.200.73.150 -Pn -sT -p 80```
```proxychains curl http://10.200.73.150```


dirb syntax ```proxychains dirb http://10.200.73.150:80 -w /usr/share/wordlists/dirb/common.txt``` 

Remember only TCP not UDP through proxies!!

With metasploit 

```
use server/socks_proxy (set SRVPORT etc) 
run autoroute -s 
```