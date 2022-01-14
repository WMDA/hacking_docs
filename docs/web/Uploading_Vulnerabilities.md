# Uploading vulns

## Bypassing client side filtering

This is where files are being filtered (usually by javascript) before being uploaded to the server.

Bypassed in a number of ways:

1) Turn off javascript in browser
2) curl the request straight to the webpage so no javascript is loaded in the browser
3) modify the request

Modifying the request:

- Comment out javascript in the request
	1) open burp
	2) intercept the upload request
	3) Intercept the servers response
	4) modify the servers response by commenting out the javascript

- Change file the type.
	1) upload a file with a vaild extension
	2) intercept the upload request
	3) change the MIME (i.e change to txt/php from image/jpeg) and the file extension (i.e from .jpg to .php) in the request.
	4) forward the request

