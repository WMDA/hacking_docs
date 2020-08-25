#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>


int main() {
	int socket, client_socket;
	char buffer[1024];
	char total_response[18384];
	struct sockaddr_in server_address, client_address;
	int i=0;
	int optval =1;
	socklen_t client_length;

	sock= socket(AF_INET, SOCK_STREAM, 0 );

	if (setsockopt(sock, SOL_SOCKET, SOL_REUSEADDR, &optval, sizeof(optval) < 0){
			printf("Error setting TCP Socket Options:\n");
			return 1;
			}
	server_address.sin_family=AF_INET;
	server_address.sin_addr.s_addr=inet_addr("192.168.100.4");
	server_address.sin_port = htons(50004);

	bind((struct sockaddr *) &server_address, sizeof(server_address));
	listen(sock, 5);
	client_length = sizeof(client_address);
	client_socket= accept(sock, (struct sockaddr *) &client_address, &client_length);
	}

