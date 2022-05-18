# Active Directory

## What is Active Directory?

An Active Directory Directory network is a forest of domains (collection) with the domains being used used to manage/group objects such as servers and other machines.

Made up of:

- Domain controllers. 

A domain controller is a windows server that has Active Directory Domain Services (AD DS) and has been promoted to a domain controller in the the forest of domains. They are the centre of the AD and control the rest of the domain. 

Domain controllers:
    - Hold AD DS data
    - Handle authentication and authroization services
    - Replicate updates from other domain controllers in the forest
    - Allows Admin access to other domain resources

- Active Directory Data Store (AD DS Data Store)

Holds information of users, groups, services etc in databases and process that are needed to manage the domain. Contains the NTDS.dit which is a database that contains all information of an Active Directory domain controller and password hashes for domain users. It is stored in %SystemRoot%\NTDS and is only accesable by the domain controller.


## Software and Infrastructure of an Active Directory.

- Forest Overview.

A forest is a collection of domains and domain trees. 
Consists of:
	- Trees, a hierachy of domains in the Active Directory Domain Services
	- Domains, used to manage/group objects.
	- Organizational Units, a container for groups, computers, users, printers and other Organizational Units.
	- Trusts, allows users to access resources in other domains.
	- Objects, users,computers,shares,
	- Domain Services, DNS servers, IPv6 etc.
	- Domain Schema, rules for object creation.

https://i.imgur.com/EZawnqU.png


- Domain Service Overview

Services that a domain controller provides to the rest of the tree/domain. 

Default Domain Service:
	- Lightweight Directory Access Protocol (LDAP), provides communication between applications and directory services.
	- Certification Services, allows domain controllers to create, validate and revoke public key certifications.
	- DNS, LLMNR (Link-Local Multicast Name Resolution), NBT-NS (Netbios Name Service)- Domain Name Services for identifying IP hostnames.


- Domain Authentication Overview

Most vunerable and important part of the AD. It is the authentication protocols set in place. 

Two main types:and Kerberos.

	- Kerberos, the default authentication service for Active Directory uses ticket-granting tickets and service tickets to authenticate and give users access to other resources across the domain.
	- NTLM, default Windows authentication protocol uses an encrypted challenge/response protocol .




