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
Will work if the email address is correct (we don't need the 1=1 as the email address is true.

## Brute force with Burp

- Send post request to intruder.
- This time highlight the password.
- Turn off URL encoding.
- run the attack.
