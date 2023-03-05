from socket import *

clientInput = input('Write hostname, server-port, filename: ')
inputList = clientInput.split()

serverName = inputList[0]
serverPort = int(inputList[1])
filename = inputList[2]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send(filename.encode())

receivedData = b''
while True:
    receivedLine = clientSocket.recv(1024)
    if not receivedLine:
        break
    receivedData += receivedLine

print('From Server:', receivedData.decode())
clientSocket.close()
