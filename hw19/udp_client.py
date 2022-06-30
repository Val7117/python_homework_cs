#!/usr/bin/env python3

# Import "socket" package
import socket

# Define the server port
server_port = 2222

# Create a client IPv4 UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ask for domain name. Send the domain name to the server and receive from the server resolved IPv4
# address. Print the received result (resolved IPv4 address).
while True:
    domain_name = input("Enter your domain name: ")
    # Type 'quit' to close UDP client
    if domain_name == "quit":
        exit(1)
    client_socket.sendto(bytes(domain_name, 'utf-8'), ("localhost", server_port))
    data, address = client_socket.recvfrom(1024)
    print(data.decode('utf-8'))
