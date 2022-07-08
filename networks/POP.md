# POP3

Post Office Protocol (POP) is a type of computer networking and Internet standard protocol that extracts and retrieves email from a remote mail server for access by the host machine. POP is an application layer protocol in the OSI model that provides end users the ability to fetch and receive email

PORT 110

## enumerating

banner grab:```nc -nv <IP> 110```

Sensitive info:```nmap --script "pop3-capabilities or pop3-ntlm-info" -sV -port <PORT> <IP>```

brute force password ```msfconsole auxillary/scanner.pop3/pop3_login```
connect:```telnet $ip 110```


commands

```
POP commands:
  USER uid           Log in as "uid"
  PASS password      Substitue "password" for your actual password
  STAT               List number of messages, total mailbox size
  LIST               List messages and sizes
  RETR n             Show message n
  DELE n             Mark message n for deletion
  RSET               Undo any changes
  QUIT               Logout (expunges messages if no RSET)
  TOP msg n          Show first n lines of message number msg
  CAPA               Get capabilities
```