#Script to prepare Kali machine, after fresh install 
#Assumes running as root (I know I shouldn't but old habits)

#Update System.
apt-get update
apt-get upgrade -y

#Install go for metasploit 
apt install -y golang

