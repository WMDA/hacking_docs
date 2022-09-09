# Web discovery

## Favicon

- Small icon displayed in the browser's address bar.
- Can be used to display what the framework stack is. 
- This can be done by 

~~~
curl <https address> | md5sum
~~~	

- Check the md5sum against https://wiki.owasp.org/index.php/OWASP_favicon_database

## Sitemap.xml

- Gives a list of every file the owner wishes us to see.

## HTTP Header

- Run to get http header

~~~
curl <http address> -v
~~~

## Google Dorking

```
Filter | Example | Description 
-------------------------------------------------------------------------------------
site   | site:tryhackme.com | returns results only from the specified website address
-------------------------------------------------------------------------------------
inurl  | inurl:admin | returns results that have the specified word in the URL
-------------------------------------------------------------------------------------
filetype| filetype:pdf | returns results which are a particular file extension
-------------------------------------------------------------------------------------
intitle | intitle:admin | returns results that contain the specified word in the title
-------------------------------------------------------------------------------------
```
