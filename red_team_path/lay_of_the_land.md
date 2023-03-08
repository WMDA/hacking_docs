# Lay of the land

Once initial access has been gained then recon on the machine/system can be done to see how the machine can be abused further

## Network infrastructure
The first step is to determine where we are and were we can get to. We need to know where we are in the network, what kind of network we are in and what the machine can offer. 

Network segreggration is an additional layer where networks are divided into multiple subnets, this provides secruity and management of the network. An example of this is Virtual Local Area Networks (VLANs) to control networking issues such as broadcasting issues and secruity as only hosts within a VLAN can communicate with each other.  

Internal networks are subnetworks that are segmented and seperated based on importance of the data.  The main purpose of the internal network(s) is to share information, faster and easier communications, collaboration tools, operational systems, and network services within an organization. In a corporate network, the network administrators intend to use network segmentation for various reasons, including controlling network traffic, optimizing network performance, and improving security posture.

A demilitarized Zone (DMZ) is an edge network that protects and adds extra secruity to a corporation's internal local-area network from untrusted traffic. A common DMZ is a subnetwork that sits between the public internet and internal networks. Depending on a companies need a DMZ network design might isolate and enable access control on the public network traffic, untrusted traffic. 

## Network enumeration

First check open TCP/UDP ports using ```netstat``` (works with powershell and linux)

```root@kali: netstat -na```

Next check the arp table which contains the IP address and the physical address of the computers that communicated with the target machines within the network (works with PS and linux).

```root@kali: arp -a```

## Active Directory

AD is a directory service that stores and provides data objects to an internal network enviornment. It allows for a centralized management of authentication and authorization, containing essential information for the enviornment/network (info for printer, computers, users details such as job, title, addresses etc).

Possible AD designs is a controlled network and servers network with the AD controller on the servers network and the AD clients on a seperate controlled network where they can join the domain and use the AD services via the firewall.

Components of an AD enviornement:

**Domain Controllers**
	- A Windows server that provides Active Directory services and controls the entire domain.
	- Centralized user management that provides encryption of user data
	-  Controls access to network
	- Provides encryption of user data 
	- Enables resource access and sharing
	- Contains high-value information.
  
**Organizational Units**
	- Containers within the AD domain with a hierarchical structure.

**AD objects**
	- Can be a single user or a group, or a hardware component, such as a computer or printer.
	- Each domain holds a database that contains object identity information that creates an AD environment, including:
		- Users - A security principal that is allowed to authenticate to machines in the domain
		- Computers - A special type of user accounts
        - GPOs - Collections of policies that are applied to other AD objects

**AD Domains**
	- A collection of Microsoft components within an AD network. 

**Forest**
	- A collection of domains that trust each other.

**AD Service Accounts**
    - Built-in local users, Domain users, Managed service accounts

**Domain Administrators**

Eumerating AD with:

```
PS C:\Users\thm> systeminfo | findstr Domain
OS Configuration:          Primary Domain Controller
Domain:                    thmdomain.com
```

From the above output, we can see that the computer name is an AD with thmdomain.com as a domain name which confirms that it is a part of the AD environment. 

Note that if we get WORKGROUP in the domain section, then it means that this machine is part of a local workgroup.

## AD users and groups
Account discovery is an important first step. An AD enviornment contains accounts with different permissions. Common AD service accounts include built-in local user accounts, domain user accounts, managed service accounts, and virtual accounts. 

AD service accounts include:
- Built in local users' accounts are used to manage the local system which is not part of the AD enviornment
- Domain user accounts which access the AD enviorment and access AD services.
- AD managed service accounts are limited domain user accounts with higher privileges to manage AD services.
- Domain Administrators, user accounts that manage information in AD enviornment including AD configurations, users, groups, permissions, roles, services, etc. One of the red team goals in engagement is to hunt for information that leads to a domain administrator having complete control over the AD environment.

The following are Active Directory Administrators accounts:


BUILTIN Administrator | Local admin access on a domain controller
Domain Admins |  Administrative access to all resources in the domain
Enterprise Admins | Available only in the forest root
Schema Admins | Capable of modifying domain/forest; useful for red teamers
Server Operators |  Can manage domain servers
Account Operators | Can manage users that are not in privileged groups


### Active Directory user enumeration.
Powershell commands
```Get-ADUser  -Filter * ```

Using the LDAP hierarchical tree structure.
```Get-ADUser -Filter * -SearchBase "CN=Users,DC=THMREDTEAM,DC=COM"```


Note that it needs to use  -Filter argument.

PowerShell

           
```
PS C:\Users\thm> Get-ADUser  -Filter * 

DistinguishedName : 
CN=Administrator,CN=Users,DC=thmredteam,DC=com 
Enabled           : True 
GivenName         : 
Name              : Administrator 
ObjectClass       : user 
ObjectGUID        : 4094d220-fb71-4de1-b5b2-ba18f6583c65 
SamAccountName    : Administrator 
SID               : S-1-5-21-1966530601-3185510712-10604624-500 
Surname           : 
UserPrincipalName :
```

	    

We can also use the [LDAP hierarchical tree structure](http://www.ietf.org/rfc/rfc2253.txt) to find a user within the AD environment. The Distinguished Name (DN) is a collection of comma-separated key and value pairs used to identify unique records within the directory. The DN consists of Domain Component (DC), OrganizationalUnitName (OU), Common Name (CN), and others. The following "CN=User1,CN=Users,DC=thmredteam,DC=com" is an example of DN, which can be visualized as follow:  

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5d617515c8cd8348d0b4e68f/room-content/764c72d40ec3d823b05d6473702e00f5.png)

Using the SearchBase option, we specify a specific Common-Name CN in the active directory. For example, we can specify to list any user(s) that part of Users.  

           
```
PS C:\Users\thm> Get-ADUser -Filter * -SearchBase "CN=Users,DC=THMREDTEAM,DC=COM"   DistinguishedName : CN=Administrator,CN=Users,DC=thmredteam,DC=com 
Enabled           : True 
GivenName         : 
Name              : Administrator 
ObjectClass       : user 
ObjectGUID        : 4094d220-fb71-4de1-b5b2-ba18f6583c65 
SamAccountName    : Administrator 
SID               : S-1-5-21-1966530601-3185510712-10604624-500 
Surname           : 
UserPrincipalName :
```
