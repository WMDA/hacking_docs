# HTTP in detail


## HTTP methods

- GET (Used for getting information from a web server).

- POST (Submitting data to the web server/creating new records)

- PUT (Updating information)

- DELETE (Deleting information/records from a web server).


## HTTP headers


Common Request Headers


- Host: 

The host headers tells the server which website we want (web servers can host multiple websites). 


- User-Agent: 

This is your browser software and version number (helps format website correctly).


- Content-Length: 
How much data to expect in the web request, ensures no missing any data.


- Accept-Encoding: 
Types of compression methods the browser supports so the data can be made smaller for transmitting.


- Cookie: 
Data sent to the server to help remember information (HTTP is stateless).


Common Response Headers


- Set-Cookie: 
Information to store which gets sent back to the web server on each request.

- Cache-Control: 
How long to store the content of the response in the browser's cache before it requests it again.

- Content-Type: 
What type of data is being returned, browser knows how to process the data.

- Content-Encoding: 
Method used to compress the data.



