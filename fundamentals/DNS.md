# DNS

Domain name system.

## Domain hierarchy

TLD (Top-Level Domain)
- Two types of TLD: 
- gTLD (Generic Top Level) Has .com, .edu etc
- ccTLD (Country Code Top Level Domain). Has .co.uk .ca etc/ 

Second-Level Domain
- Limited to 63 characters + the TLD (253 characters). 
- It is the web name before the TLD (.com etc ) and after the protocol (google, facebook etc)

Subdomain
- 253 characters or less. i.e google.com/admin (admin is sub domain).

## DNS Record Types

DNS isn't just for websites though, multiple types of DNS record exist. 

A Record
- Resolve to IPv4 addresses.

AAAA Record
- Resolve to IPv6 addresses.

CNAME Record
- Resolve to another domain name,
- For example, TryHackMe's online shop has the subdomain name store.tryhackme.com which returns a CNAME record shops.shopify.com. 

MX Record
- These records resolve to the address of the servers that handle the email for the domain you are querying 
- i.e MX record response for tryhackme.com would look something like alt1.aspmx.l.google.com). 
- These records also come with a priority flag.

TXT Record
- Multiple uses
- list servers that have the authority to send an email on behalf of the domain
- verify ownership of the domain name when signing up for third party services.


## When a DNS request is made.

1) Recursive DNS Server request. Computer first checks its local cache to see if address exits. Usually provided by your ISP. If found request ends.
2) Root DNS servers. Redirect you to the correct Top Level Domain Server, depending on request.
3) TLD server holds records for where to find the authoritative server to answer the DNS request.
4) Authoritative DNS server is the server that is responsible for storing the DNS records. 
5) DNS record is then sent back to the Recursive DNS Server, where a local copy will be cached for future requests and then relayed back to the original client that made the request. 
6) DNS records all come with a TTL (Time To Live) value. This value is a number represented in seconds that the response should be saved for locally until you have to look it up again.
