# Basics

This is a document of very basic web from HTB academy. 

## URL

Resources over HTTP are accessed via a URL

### URl anatomy

Scheme: http:// or https:// Used to identify the protocol being accessed by the client, and ends with a colon and a double slash (://)

User Info: 	admin:password@ Optional component that contains the credentials (separated by a colon :) used to authenticate to the host, and is separated from the host with an at sign (@)

Host: inlanefreight.com	The host signifies the resource location. This can be a hostname or an IP address

Port: :80 The Port is separated from the Host by a colon (:). If no port is specified, http schemes default to port 80 and https default to port 443

Path: /dashboard.php The resource being accessed, which can be a file or a folder. If there is no specified, the server returns the default index (e.g. index.html).

Query String 	?login=true The query string starts with a question mark (?), and consists of a parameter (e.g. login) and a value (e.g. true). Multiple parameters can be separated 
by an ampersand (&).

Fragments #status Fragments are processed by the browsers on the client-side to locate sections within the primary resource (e.g. a header or section on the page).

## cURL

```
 -d, --data <data>   HTTP POST data. (If using JSON data has to be '{"search":"london"}' along with appropriate header -H 'Content-Type: application/json')
 -h, --help <category> Get help for commands
 -i, --include       Include protocol response headers in the output
 -I                  Send HEAD request (only prints response headers)
 -o, --output <file> Write to file instead of stdout
 -O, --remote-name   Write output to a file named as the remote file
 -s, --silent        Silent mode
 -u, --user <user:password> Server user and password
 -A, --user-agent <name> Send User-Agent <name> to server
 -v, --verbose  
 -k Skip HTTPS (SSL) certificate validation
 -H Set request header
 -X change request type
 -L --location follow redirects
 ```
## HTTP flow

1) Enter in url
2) Browser checks local DNS record (/etc/hosts)
3) If DNS record not found it communciates with DNS server to get IP address
4) Makes request to web server

## HTTPS flow

1) Request to web server
2) Client hello
3) Server hello with server key exchange
4) Client key exchange with encrypted handshake
5) Server encrypted handshake
6) Encrypted communication

Use -K in curl to skip ssl certification if a website has an invalid SSL certificate

## HTTP request

Conists of:

- Method (GET,POST etc)
- Path 	(/users/login.html) The path to the resource being accessed. This field can also be suffixed with a query string (e.g. ?username=user).
- HTTP version (HTTP/ 1.1)

### Header values: 

Headers can be divided into multiple categories: 

1) General Headers
	These headers describe the message rather than its content. General headers:

	- *Date*: Holds the date and time at which the message originated. 
	- *Connection*: Should the connection stay alive after the request finishes. Options a re closed or keep-alive

2) Enity Headers
	These are headers to describe the content.

	- *Content-type*: Used to describe the resource, being tranfered, i.e text/html etc. Charset field denotes the encoding standard, such as UTF-8.
	- *Media-Type*: Describes the data being transfered, i.e pdf/jpeg. 
	- *Boundary*: Acts as a maker to separate content when there is more than one in the same message. I.e boundary="b4e4fbd93540"
	- *Content-Length*: Length of entity being passed.
	- *Content-Encoding*: Data can undergo multiple transformations before being passed, i.e compressed. The type of encoding being used should be specified using this header.

3) Request Headers
	These are used in http(s) requests. Not related to message content.

	- *Host*: The host being queried for the resource (name of website, ip address etc)
	- *User-Agent*: Describes the client. Information about the client such as browser, os and versions.
	- *Referer*: Says where the current request is coming from. Can be easily manipulated.
	- *Accept*: Describes which media types the client can understand. ```*/*``` means that all media can be accepted.
	- *cookie*
	- *Authorization*: Another identification method. After successful authentication a unique token is given to the client. Tokens are stored on the client side (unlike cookies) and sent in each request. 


4) Response Headers.
	These are headers sent back in the response.

	- *Server*: Information about the HTTP server, version etc.
	- *Set-Cookie*: Contains the cookie. Browsers store the cookie.
	- *WWW-Authenticate*: Notifies the client about the type of authentication required to access the requested resource.

5) Secruity Headers
	These headers define certain rules and policies to be followed to enhance secruity.

	- *Content-Security-Policy*: Dictates the website's policy towards externally injected resources such as Javascript/scripting resources. Instructs the browser to only trust domains, prevents XSS.
	- *Strict-Transport-Security*: Forces all communication to use HTTPS and not HTTP.
	- *Referrer-Policy*: Dictates whether browser should include the value specified in the referer.
	- *Upgrade-Insecure-Requests*: expressing the client's preference for an encrypted and authenticated response, and that it can successfully handle the upgrade-insecure-requests

## APIs

Many APIs are used to interact with a database by requesting data and then using HTTP methods to perform the needed operations.

### CRUD 

Access data then using HTTP methods to manipulate perform different operations on it. 

HTTP methods:
	- CREATE (POST method equivalent) add data
	- READ (GET method equivalent) read data
	- Update (PUT method equivalent) updates data.
	- Delete (DELETE method equivalent) delete data.

Using CURL to do CREATE and READ it is identical. (curl -X POST for create and curl normally for read).

For UPDATE method with curl use -X PUT

For the DELETE method with curl -X DELETE