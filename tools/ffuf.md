# ffuf 

## Dir discovery

~~~
ffuf -w <wordlist> -u <IP>
~~~

## Sub-domain discovery

~~~
ffuf -w <wordlist>  -H "Host: FUZZ.domain name" -u <IP address> -fs {size}

-H adds/edits a header
- FUZZ keyword is the space where a sub-domain would go and is where the brute force happens
-fs filters out results as will always produce a valid result. So put the most common size here and 
    it filters out these results which are false positives.
~~~

## Username enumeration

~~~
ffuf -w <wordlist> -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u <IP address> -mr <string, error message when user already exists>
~~~

The command takes advantage of error message given when a user is created with a pre existing username.

~~~
-w wordlist of common users
-X request method
-d data that is going to be sent to the form (we are only FUZZ the username).
-H used for adding additional info given to the HTTP header. Content-Type is used so the website knows we are sending form data
-u URL
-mr string of error message.
~~~

## Brute Force

~~~
ffuf -w <wordlist of valid users from earlier step>:W1,<wordlist of passwords>:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u <URL> -fc <HTTP code to exclude>
~~~

Brute force passwords for valid users

~~~
W1 and W2 indicate that two wordlists are used.
-fc HTTP status to exclude in the checking. i.e 200 means it will exlcude HTTP 200 and check for other responses.
~~~

 
~~~