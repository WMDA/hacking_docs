# Recon

## DNS/Web look up

- whois (query who a domain name is registered to)
- traceroute (traces packet route)
- dig (manually query recursive DNS servers for information) 
- nslookup (get the A and AAAA records related to the domain)
- google dorking (see web_discovery md)

## Recon-ng

```recon-ng -w <workspace name>``` creates a new work space

```db schema``` to see the database 

```db insert domains``` insert domain name into db

```marketplace search``` search the marketplace for plugins

```market place info <module name>``` gets info on the module 

```marketplace install <module name>``` installs module (change install to remove)

modules with a * in the K column need a key while modules with a * in the D column have dependcies.

```modules search``` shows all installed modules

```modules load <module name>``` loads the module

```run``` runs module

```cntrl + c``` to unload module

```info``` on loaded module 

```options list``` to show loaded modules options

```options set <value>``` set an option in a loaded module

```keys list``` list all the keys


## Maletgo 

Graphs and mind maps OSINT. Each block on a Maltego graph is an entity which has values attached to it to describe it. In Maltego’s terminology, a transform is a piece of code that would query an API to retrieve information related to a specific entity. Information related to an entity goes via a transform to return zero or more entities. *WARNING* Maltego may directly connect to target host so be careful.

An example we have a hostname google.com. We can use an enity to transform this into an IP address. This then creates a mind map, and we can do more and more transformations. All information gathered (including names and email addresses) are presented in a mind map. *NOT ALL TRANSFORMS ARE FREE*
