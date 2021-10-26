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
ffuf -w <wordlist> -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u <IP address> -mr "username already exists"

