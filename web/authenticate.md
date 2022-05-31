# Authenticate

## dictionary attack

Using owasp zap

1) Find the post request
2) Right click attack then fuzz
3) Put cursor where want to fuzz
4) Click add
5) File, rockyou
6) start fuzzer

## Re-registration

Re-registering an existing user but adding in a space before the users name.

Logging in as this new user will (remember the space in front of the username) will give us access to the existing users account that  we re-registered.

## JWT

JWT tokens

- A kind of cookie that is generated using HMAC hashing or public/private keys.
- unlike any other kind of cookie, it lets the website know what kind of access the currently logged in user has. 
- Consists of a header, payload and signature (all seperated by a .)
- Usually base64 decoded (apart from signature)

JWT header 
- This consists of the algorithm used to sign the token and the type of the token.
```{  "alg": "HS256", "typ": "JWT"}```

Payload
- Contains user details, ID and access rights

Signature
- The part that is used to make sure that the integrity of the data was maintained while transferring it from a user's computer to the server and back.
- Encrypted with whatever algorithm or alg that was passed in the header's value.
- Decrypted with a predefined secret

Exploitation
- can do Brute force/dictionary to find the secret or Get a low level user then change the alg value to none, so there is no encryption

Level level user exploit
- Get JWT token from low level user
- encode into base64
```{"typ":"JWT","alg":"NONE"}```
- encode what payload
-

eyJ0eXAiOiJKV1QiLCJhbGciOiJOT05FIn0K.eyJleHAiOjE1ODY2MjA5MjksImlhdCI6MTU4NjYyMDYyOSwibmJmIjoxNTg2NjIwNjI5LCJpZGVu.

