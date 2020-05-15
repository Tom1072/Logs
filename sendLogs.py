from socket import socket, AF_INET, SOCK_DGRAM
sock = socket(AF_INET, SOCK_DGRAM)
sock.sendto(b'{"message":{"someField":"someValue"}}', ('localhost', 5400))