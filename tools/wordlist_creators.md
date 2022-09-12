# Wordlist creators

This is a very brief overview of tools available to create wordlists

## Usernames

```python username_generator.py -w wordlist_of_potential_users```
This will create different combintations of usernames to use in brute force attacks.

## Passwords

```crunch <min_length_of_word> <max_length_of_word> <string_to_use_to_create_wordlists> -o <save_to_file```

```crunch 6 6 -t pass%% -o wordlist``` this will create a wordlist file with all the words begining with pass and going from 00 to 99 as a suffix.

In the example replace % with any of the following for different results
```
@ - lower case alpha characters
, - upper case alpha characters
% - numeric characters
^ - special characters including space
```

```python cupp.py``` interactively builds wordlist based on information regarding the target.