from socket import socket, AF_INET, SOCK_DGRAM
import random
import json

def main():
    data_str = populateData()
    sendData(data_str)

def populateData():
    f = open("users.json","r")
    data = json.load(f)
    data_str = []
    for element in data:
        data_str.append(json.dumps({"message":element, "type":"users"}))
    return data_str

def sendData(data_str):
    sock = socket(AF_INET, SOCK_DGRAM)
    print(data_str[1])
    for i in range(5):
        sock.sendto(bytes(data_str[i],"utf8"), ('localhost', 5400))

if __name__ == "__main__":
    main()
    