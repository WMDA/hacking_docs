# Python commands

## URL enocde

~~~
import urllib.parse
string_to_encode= urlparse.quote_plus("<script>alert('THM');</script>"))
~~~

## Base64

~~~
import base64

string=sring_to_be_encoded or decoded

print(base64.b64encode(string))
print(base64.b64decode(string))
~~~

## Hex code

~~~
import binascii

binascii.hexlify(b'') 
~~~

