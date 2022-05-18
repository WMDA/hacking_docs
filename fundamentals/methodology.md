# Methodology

## Web page

1) View web page
2) Run gobuster on base web page (with common and a longer worlist)
3) View Gobuster results
4) Vist gobuster result s websites 
5) view source code of EACH webpage provided by gobuster
6) gobuster other directories provided (with common and longer word lists)
7) Check URL for injectable (sqli or LFI) vulnerabilities.
9) Check technologies used for webpage.
10) Check for known vulnerabilities in technologies
11) Check for specialised scanners for web technologies (WPSCAN, metasploit)

### Login forms

1) Check default credentials (admin, root, password, password1)
2) Check for sql bypass. 
   - First try payloads into the username part.
   - Intercept request and save. Provide to sqlmap via -r

