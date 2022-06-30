#!/usr/bin/env python3

# Import "socket" package
import socket

# Define the server listening port
listening_port = 2222

# Create a server IPv4 UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind listening port to the server. Print the message.
server_socket.bind(('localhost', listening_port))
info = f"UDP DNS Server listening on port {listening_port}"
print(info)

# Write 'info' message to logs
with open("logs.txt", "a") as logs:
    logs.write(f"\n{info}")


# Function checks if the hostname can be resolved to the correct IPv4 address.
def hostname_resolved(hostname):
    try:
        socket.gethostbyname(hostname)
        return 1
    except socket.error:
        return 0


# Function checks if the ipv4 address is valid.
def validate_ip(ipv4):
    try:
        socket.inet_aton(ipv4)
        return 1
    except socket.error:
        return 0


# Additional dictionary for defined personal domains.
personal_domains = dict()

# Receive and read 1024 bytes from server socket. Decode and split data.
# If the word 'ADD' 'domain.name:ipv4_address' are sent and the IPv4 is valid, then add to dictionary
# 'personal domains' and print the result. After that, send a response message to the client.
# When there is a word ADD, we check the correctness of the entered data, using additional
# if, else statement.
# Else if the received hostname has been previously defined, then get the key value (IPv4 address) from
# dictionary, then print the result and sent the resolved from dictionary IPv4 address to a client.
# Else if the received hostname can be resolved, then print the result on server and send the result to
# a client.
# Otherwise, send an Error message.
# All results are added to 'logs.txt' file in local directory.
while True:
    data, address = server_socket.recvfrom(1024)
    data = data.decode("utf-8")
    split_data = data.split()
    if split_data[0] == 'ADD':
        if len(split_data) == 2 and len(split_data[1].split(':')) == 2 and validate_ip(split_data[1].split(':')[1]):
            record = split_data[1].split(':')
            personal_domains.update({record[0]: record[1]})
            res = f"Request: {data} received from {address}. Result: {record[0]}: {record[1]} added to personal domains."
            print(res)
            with open("logs.txt", "a") as logs:
                logs.write(f"\n{res}")
            response_message = str(f"You domain {record[0]}:{record[1]} has been added successfully.")
            server_socket.sendto(bytes(response_message, "utf-8"), address)
        else:
            response_message = str("Invalid command")
            with open("logs.txt", "a") as logs:
                logs.write(f"\n{response_message}: {data} from {address}")
            server_socket.sendto(bytes(response_message, "utf-8"), address)
    elif str(data) in personal_domains:
        res = f"Request: {data} received from {address}. Result: resolved IPv4 address from personal domain sent to {address}."
        print(res)
        with open("logs.txt", "a") as logs:
            logs.write(f"\n{res}")
        server_socket.sendto(bytes(personal_domains[str(data)], "utf-8"), address)
    elif hostname_resolved(data):
        resolved_name = socket.gethostbyname(data)
        res = f"Request: {data} received from {address}. Result: {resolved_name} sent to {address}"
        print(res)
        with open("logs.txt", "a") as logs:
            logs.write(f"\n{res}")
        server_socket.sendto(bytes(f"{resolved_name}", "utf-8"), address)
    else:
        res = f"Request: {data} received from {address}. Result: an error message sent to {address}."
        print(res)
        with open("logs.txt", "a") as logs:
            logs.write(f"\n{res}")
        message = f"Error: Cannot resolve your address {data}. Please, enter the correct domain name."
        server_socket.sendto(bytes(message, "utf-8"), address)
