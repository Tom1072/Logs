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
    for i in range(100):
        data_str.append(json.dumps(data[i]))
    return data_str

def sendData(data_str):
    sock = socket(AF_INET, SOCK_DGRAM)
    for i in range(5):
        sock.sendto(bytes(data_str[i],"utf-8"), ('localhost', 5400))

if __name__ == "__main__":
    main()