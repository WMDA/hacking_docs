# OWAS con

## How to do SQL injection attacks with burpsuite.

- First send post request to intruder. 
- Then highlight email section (it has to be inside the "").
- Turn url encoding off.
- Run attack.

### Why this works

Example of SQL statement 

~~~
a' or 1=1--
~~~

- The characters such as ' will close the SQL query
- 'OR' in a SQL statement returns true if either side of it is true. 
- 1=1 is always true, so it tells the server that the email is valid and log us into user id 0 (admin).
- The -- character is used in SQL to comment out data, any restrictions on the login will no longer work as they are interpreted as a comment.

The
~~~
'--
~~~
Will work if the email address is correct (we don't need the 1=1 as the email address is true).

## Brute force with Burp

- Send post request to intruder.
- This time highlight the password.
- Turn off URL encoding.
- run the attack.

## Poison Null Byte

- NULL terminator
- Placing a NULL character at certain points in the string nullifies the rest of the string at that point.
- Can be used to change URL (by ignoring sections of it) or to download files that aren't allowed.

NULL terminator is:
~~~
%00
~~~

But if it is put in a URL it needs to be encoded. Can be done by:

~~~
python -c "import urllib.parse;print(urllib.parse.quote(''))"
~~~

So the URL encoded NULL terminator is:

~~~
%2500
~~~

## Checking other users.

- Check the javascript files for administrator pages.
- Change the request with burp

Example
~~~
GET /rest/basket/1 HTTP/1.1
~~

Change the /basket/1 to /basket/2 to view other users.

## XSS

- Allows attackers to run javascript in web applications.

Three type:
1) DOM. Uses HTML to execute (<script></script> tags).


Example

~~~
<iframe src="javascript:alert(`xss`)"> 
~~~

into input box box


This is an XFS (cross frame scripting) and websites that allow users to modify the iframe or other DOM
  are vunlerable. The site should sanitise the user input but sometimes doesn't.

2) Persistent. 

Server side, uses code injected into the server that is loaded and run when the server is active.
Occurs when user input isn't sanitised.

Example
- If a part of the website remembers login details etc this can be changed.
- Add a new header to the request sent to the server using burpsuite inspector heading.
- True-Client-IP (used to determine the IP address of a client connecting to a web server)
  then adding in the payload is an example. 


3) Reflected. 
Client-side, occurs when server doesn't sanitise search data. 

Example
- Adding javascript payload to the id= in the url bar.