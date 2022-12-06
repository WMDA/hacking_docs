# No SQL injections

## Basic overview

Nosql databases are databases like sql databases except that information is stored in documents not tables (basically like json or python dictionaries). They have a key/value pair and nosql databases allow multiple documents (json files/python dictionary type things) to be stored together into collections (a collection is like a table in sql terms). Collections are basically  nested associative arrays.

A mongo db document object

```
{"_id" : ObjectId("5f077332de2cdf808d26cd74")"username" : "lphillips", "first_name" : "Logan", "last_name" : "Phillips", "age" : "65", "email" : "lphillips@example.com" }
```

lots of these objects are stored in a collection (in this example we will call the object people as all the documents are about people) and multiple collections make up a database. 

### Querying a database

If we wanted to filter for documents were the last name was sandler (continuing with the example above) we would write ```['last_name' => 'Sandler']```. More complex filters can be done as well ```['gender' => 'male', 'last_name' => 'Phillips']``` and we can use keywords such as ```$lt``` to filter for values less that ```['age' => ['$lt'=>'50']]```

**NOTE SO FAR EVERYTHING HAS BEEN ABOUT MONGO DB**


### A side note on Mongo db

mongo db is a nosql database on port 27017 as default. MongoDB uses JSON-like documents with optional schemas

Use mongo (cli tool) to connect to database.
S
basic mongo db commands
```
show dbs - shows databases in the servers
use <db name> - connection to database
show collections
db.<insert collection here>.find().pretty() - shows content  
```

## No sql injections

Unlike SQL injections which are built using string concatenation no sql queries require nested associative arrays (the collections) so to attack a no-sql database we have to inject arrays into the application.

This can be done using special syntax on the query string of an HTTP Request.

An example using php

![Web app](https://i.imgur.com/MTWIydx.png)

This web app is making a query to a mongodb database using the myapp database and login collection requesting any document that passes the filter ```['username'=>$user, 'password'=>$pass]``` where both $user and $pass are obtained directly from HTTP POST parameters. If we could inject 

```
$user = ['$ne'=>'xxxx'] 

$pass = ['$ne'=>'yyyy'] 
```

then all documents not equal to xxxx and yyyy will be returned (so all documents) and this might trick the appplication that a correct login was performed, giving us access to the first document returned (as all the documents are returned so all the users are returned). 

With php we can return the arrays required by using the following notation in a post request ```user[$ne]=xxxx&pass[$ne]=yyyy```

Using $ne we login as the first user returned. But what about if we want to login as other users? We can use the ```$nin``` operator to create a filter by specifying we only want documents without a certain value.

```user[$nin][]=admin&pass[$ne]=aweasdf``` would equate to this query ```['username'=>['$nin'=>['admin'] ], 'password'=>['$ne'=>'aweasdf']]``` whohc is basically saying I want to logon as any user except for admin.

This is also useful as we can see how many users there are by keep filtering out users in the database. We do this by ```user[$nin][]=admin&user[$nin][]=jude&pass[$ne]=aweasdf``` for example

### Getting passwords 

We can get passwords by abusing the $regex opertator. 

By using ```^.{7}$``` in the password parameter along with a username of admin we are asking the server for the password length of the admin. If we keep keep changing the 7 in the query to a another number we can found out the length of the password.

Once we have found the length we need to find the content. We can do this by using ```^c....$``` (change the number of . depending on the length of the password) and changing the c until we find the actual leter at the begining of the password.

## Partical task

1) First find length of password (use burp suite intruder). How to do this (in the exercise it is to find password of john) ```user=john&pass[$regex]=.{§0§}$&remember=on```

What we wnat to see is a location in the response. Once the location is no longer in the header then we have the length of the password.

2) To get password

```user=john&pass[$regex]=^§0§.......$&remember=on``` using burp suite intruder see when the location is in the header. (if you have time can use the cluster bomb setting as this needs to be done to get each character for the password )

## Other payloads

To bypass login ```admin '|| '1==1```
This also works when put in to url parameters
