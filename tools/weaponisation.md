# Cyber kill chain


The cyberkill chain (in () is the MITRE ATT&CK)
1) Recon (recon) 
	- Obtain information on the target 	Harvesting emails, OSINT

2) Weaponization (Execution)
	- Creating payloads etc. Exploit with backdoor, malicious office document

3) Delivery (intial access)
	- How the payload will be delievered. Email, web, USB

4) Explotation (initial access)
	- Exploit the target's system to execute code 	MS17-010, Zero-Logon, etc.

5) Installation (persistence)
	- Install malware or other tooling 	Mimikatz, Rubeus, etc.

6) Command & control (C2)
	- Control the compromised asset from a remote central controller 	Empire, Cobalt Strike, etc.

7) Action on objectives (Exfiltration/impact)
	- Any end objectives: ransomware, data exfiltration, etc. 	Conti, LockBit2.0, etc.

## Weaponization

This involves creating payloads to be run on the target machine to get initial access.

### Windows Scripting Host

Windows scripting host is a built-in Windows administration tool that runs batch files to automate and manage tasks within the operating system. It is a windows native engine cscript.exe for command line scripts and wscript.exe for GUI which are responsbile for executing various windows basic scripts including vbe and vbs. Scripts are ran at the same permission level as the compromised user.

To create a simple payload using VBscript

```
Dim message
message ="hello"
MsgBox message
```

Dim declares a variable. The variable is then assigned a value and then the MsgBox function called with the variable.

THe code can be saved to a file with a .vbs extension and run using wscript.

```wscript payload.vbs``` 

Using VBscript to run exe files

```
Set shell = WScript.CreateObject("Wscript.Shell")
shell.Run("C:\Windows\System32\calc.exe " & WScript.ScriptFullName),0,True
```

this runs the windows calculator.

If wscript is not allowed then can use ```cscript.exe <filename>.vbs```
Also can also name the file as .txt and use an argument in wscript ```/e:VBScript``` to make it run as an vbs script.

```wscript /e:VBScript payload.txt```