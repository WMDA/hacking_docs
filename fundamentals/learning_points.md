# Generic HTB Learning points

```
X-Xss-Protection headers stop browsers from loading when they detect xss.



0 
  Disables XSS filtering.
1
    Enables XSS filtering (usually default in browsers). If a cross-site scripting attack is detected, the browser will sanitize the page (remove the unsafe parts).
1; mode=block
    Enables XSS filtering. Rather than sanitizing the page, the browser will prevent rendering of the page if an attack is detected.
1; report=<reporting-URI> (Chromium only)
    Enables XSS filtering. If a cross-site scripting attack is detected, the browser will sanitize the page and report the violation. This uses the functionality of the CSP report-uri directive to send a report.
```

nginx 1.18 - April 21st 2020 latest version is 1.20

Sinatra doesn’t know this ditty: error from the sinatra project that is about making webpages in ruby

'WWW-Authenticate: Basic realm="My Realm"' username and password should be the same on all the site

check the js files. Update weapy to get .js files

REMEMBER COMMAND INJECTION!!!!

Kepp trying diiferent payloads as some may work

PATH injection with sudo script

create a file with the name of the binary to hijack. chmod +x then sudo PATH=/tmp:$PATH <path to script>