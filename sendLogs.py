from socket import socket, AF_INET, SOCK_DGRAM
import random
import json

sock = socket(AF_INET, SOCK_DGRAM)
f = open("users.json","r")
data = json.load(f)
data_str = []
for i in range(100):
    data_str.append(json.dumps(data[i]))
    print(type(data_str[i]))


# for i in data:
    # print(i)
# for i in range (5):
#     sock.sendto()
