# Passwords

## Wordlist creators

This is a very brief overview of tools available to create wordlists

### Usernames

```python username_generator.py -w wordlist_of_potential_users```
This will create different combintations of usernames to use in brute force attacks.

### Passwords

```crunch <min_length_of_word> <max_length_of_word> <string_to_use_to_create_wordlists> -o <save_to_file```

```crunch 6 6 -t pass%% -o wordlist``` this will create a wordlist file with all the words begining with pass and going from 00 to 99 as a suffix.

In the example replace % with any of the following for different results
```
@ - lower case alpha characters
, - upper case alpha characters
% - numeric characters
^ - special characters including space
```

```python cupp.py``` interactively builds wordlist based on information regarding the target.

```
cewl -w <name of wordlist> -m -d <url>

-w writes the contents to a file. 
-m gathers strings (words) that are certain character length or more
-d  depth level of web crawling/spidering (default 2)
```

## Password cracking

### identifying hashes

```hash-identifer```

### Hashcat

```
hashcat -a -m <hash> <wordlist> 

-a attack mode. 0 is dictionary. 3 is brute force
-m hash mode. 0 is md5
--show shows cracked hashes
```
buteforce options.
```
  l | abcdefghijklmnopqrstuvwxyz [a-z]
  u | ABCDEFGHIJKLMNOPQRSTUVWXYZ [A-Z]
  d | 0123456789                 [0-9]
  h | 0123456789abcdef           [0-9a-f]
  H | 0123456789ABCDEF           [0-9A-F]
  s |  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
  a | ?l?u?d?s
  b | 0x00 - 0xff
```

use is ```?d```. An example of trying to crack a 4 digit pin ```hashcat -a 3 -m 0 <hash> ?d?d?d?d```

### John

Rules allow us to add rules such as digits etc to password lists, useful when we know the password policy.

See rules ```cat /etc/john/john.conf|grep "List.Rules:" | cut -d"." -f3 | cut -d":" -f2 | cut -d"]" -f1 | awk NF```

Use john to set rules ```john --wordlist=<wordlist> --rules=<rules> --stdout```

Set custom rules by adding them to the end of the john.conf file. 

Custom rules
```
[List.Rules:Password-Attacks] - names rule Password-Attacks
Az - represents a single word from the original wordlist/dictionary using -p
"[0-9]" append a single digit (from 0 to 9) to the end of the word. For two digits, we can add "[0-9][0-9]"  and so on. 
^[!@#$] add a special character at the beginning of each word. $[!@#$] add to end of word.
```