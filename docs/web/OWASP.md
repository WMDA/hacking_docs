# OWASP top 10 web vunerabilities

## 1 Injection

- Occur because user input is interpreted as commands.
- Examples are SQL injection and command injection.
- Can be used to make a system call back to attacker machine to get a reverse shell.

## 2 Broken Authentication

- Finding flaws in the authentication of users
- Can be used to trick the web server into thinking we are a user.
- Common flaws include: Weak session cookies, weak credentials and brute force attacks.

## 3 Sensitive Data Exposure

- Webapps divulge sensitive data.
- Most common way to store large amounts of data are in database servers (SQL i.e) 
  or as a file (flat-file database).
- If a flat file database is accessable to non root users it can be downloaded and read.
- Commonest flat file database format is an sqlite database.

~~~
sqlite3 <database-name>

.table (view tables)
PRAGMA table_info(<table>); (this views table information)
SELECT * FROM <table>; (selects all inforamtion)
~~~

## 4 XML External Entity (XXE)

- Vulnerability that abuses XML parsers/data.
- Allows interaction with backend.
- Two types: in-band (recieves immediate response to XXE payload) and
  out-of-band/blind XXE (no immediate response and the output is put to another file).

### XML basics

eXtensible Markup Language:
- A markup language for transporting/storing data.
- Platform independent.
- XML can be changed without affecting presentation.
- Allows validation using Document Type Definition (DTD) and Schema (so free from syntax errors).
- No conversion require any conversion,


### XML syntax

- Mostly start with prolog.

~~~
<?xml version="1.0" encoding="UTF-8"?>
~~~

- XML must contain root element with child elements.

~~~
<root>
    <child></child>
</root>
~~~

- Similar to HTML (can use attributes such as <p></p>)

### XML DTD

Document Type Definition
- Defines structure and attributes in XML document.
- Can be in different file to the XML (.dtd).

Example note.dtd
~~~
<!DOCTYPE note [ <!ELEMENT note (to,from,heading,body)> 
<!ELEMENT to (#PCDATA)> <!ELEMENT from (#PCDATA)> 
<!ELEMENT heading (#PCDATA)> <!ELEMENT body (#PCDATA)>
<!ENTITY name "feast"> ]>
~~~

Key
- !DOCTYPE note (or root) defines the root element.
- !ELEMENT note (or root) defines what the root element must contain.
- !ELEMENT <child> defines the child element (and) to be #PCDATA (Parsed Character Data).
- !ENTITY defines a new entity. 


A XML file with the DTD defined.
~~~
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE note SYSTEM "note.dtd">
<note>
    <to>falcon</to>
    <from>feast</from>
    <heading>hacking</heading>
    <body>XXE attack</body>
</note>
~~~

### XEE payloads


~~~
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
<root>&read;</root>
~~~

- This payload displays the content of /etc/passwd file (can change to display any file in a system).

## 5 Broken access control

- When a non authorised user can access protected pages.
- Can be done through an application using unverfied SQL call.
- Or can be done through changing the URL. 
- Insecure Direct Object Reference is exploiting a misconfiguration in user input to access 
  priviledged resources

## 6 Security Misconfiguration

Security misconfiguration includes:
- poorly configured cloud services.
- Default accounts with default passwords
- Too explict error messages 
- No HTTP security headers or too much info in the Server:HTTP header.

## 7 Cross scripting.

- Allows injection of malicious code.
- Dependent on a webiste using unsanitized user input.
- Three types:
  1) Stored XSS. Where malicious code originates from website.
  2) Reflected XSS. Payload is given to the victim as part of the request.
  3) DOM-Based XSS (Document Object Model). Changes the Webpage.


### XSS Payloads.

- Popup's. (<script>alert(“Hello World”)</script>)
- Writing HTML (document.write). Overiddings the website's HTML to add own.
- XSS keylogger.
- Port Scanning.

http://www.xss-payloads.com/ has more payloads.   


## 8 Insecure Deserialization

- Insecure deserialization is replacing data processed by an application with malicious code.
- An object (such as a password) needs to be converted into to a compatible format for transporting 
  between systems/networks for processing. This is serialization. 
- Deserialization is converting the serialized (simple) object back to a complex object 
  so it can be understood.
- Insecure deserialization is when data from gets executed because there is no 
  filtering or input validation and the system assumes that the data is trustworthy.  
- We can hijack the serialization/deserialization process in badly config machines.
- Modifying cookies is one way of doing this.

## 9 Webpages with known vunerabilities


## 10 Insufficient logging and monitoring.

- Webpages where traffic isn't sufficiently logged and monitored.

