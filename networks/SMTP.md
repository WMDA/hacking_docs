# SMTP

Simple Mail Transfer Protocol:
- A TCP/IP protocol Involved in sending emails.
- SMTP verfies who is sending the email (through the SMTP server), sends outgoing mail and if it fails let the user know.
- Part of a protocol pair with Post Office Protocol (POP)/Internet Message Access Protocol (IMAP).
- Ports 25,465,587 
- Runs on linux/windows.
- It is limited in its ability to queue messages at the receiving end, it is usually used with one of two other protocols, POP3 or IMAP

## POP v IMAP

- POP downloads the servers inbox directly.
- IMAP synchorises with the servers inbox and only downloads new emails.
- IMAP allows for changes on a machine to persist unlike POP.


## How SMTP works

1. The sender connects to the SMTP server of your domain, e.g. smtp.google.com. 
2. This initiates the SMTP handshake and the SMTP session starts.
3. The sender then submits the email to the SMTP server.
4. The SMTP server then checks whether the domain name of the recipient and the sender is the same.
5. The SMTP server of the sender will make a connection to the recipient's SMTP server before relaying the email. 
6. If the recipient's server can't be accessed, or is not available- the Email gets put into an SMTP queue.
7. The recipient's SMTP server verifies the incoming email, by checking if the domain and user name have been recognised. 
8. The recipient's server will then forward the email to the POP or IMAP server.
9. The E-Mail will then show up in the recipient's inbox.

## Enumeration SMTP

### Grab SMTP Banner
  ```nc -vn {IP} 25```

### SMTP Vuln Scan
```nmap --script=smtp-commands,smtp-enum-users,smtp-vuln-cve2010-4344,smtp-vuln-cve2011-1720,smtp-vuln-cve2011-1764 -p 25 {IP}```

### SMTP User Enum
```smtp-user-enum -M VRFY -U {Big_Userlist} -t {IP}```

or run the nmap vuln scan

### SMTPS Connect

Attempt to connect to SMTPS two different ways

```openssl s_client -crlf -connect {IP}:465 &&&& openssl s_client -starttls smtp -crlf -connect {IP}:587```

### Find MX Servers

```dig +short mx {Domain_Name}```

### Hydra Brute Force

```hydra -P {Big_Passwordlist} {IP} smtp -V```

### metasploit

metasploit smtp_enum with USER_FILE /usr/share/wordlists/SecLists/Usernames/top-usernames-shortlist.txt to return users.

``` msfconsole -q -x 'use auxiliary/scanner/smtp/smtp_version; set RHOSTS {IP}; set RPORT 25; run; exit'```
``` msfconsole -q -x 'use auxiliary/scanner/smtp/smtp_ntlm_domain; set RHOSTS {IP}; set RPORT 25; run; exit ```
``` msfconsole -q -x 'use auxiliary/scanner/smtp/smtp_relay; set RHOSTS {IP}; set RPORT 25; run; exit ```


### SMTP internal commands
SMTP service has two internal commands that allow the enumeration:
- VRFY (confirming the names of users). 
- EXPN (reveals address of user’s aliases and lists of e-mail).
