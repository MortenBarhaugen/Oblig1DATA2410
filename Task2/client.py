from socket import *

# Getting input from the user and splitting them into individual words
clientInput = input('Write hostname, server-port, filename: ')
inputList = clientInput.split()

# Assigning the name and port of the server as well as the filename to variables
serverName = inputList[0]
serverPort = int(inputList[1])
filename = inputList[2]

# Creating a TCP socket and connecting to the server-name and port that was given at input
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send(filename.encode())

# Declaring a variable to store data from the server as a byte string
receivedData = b''
# Receiving data from server
while True:
    receivedLine = clientSocket.recv(1024)
    if not receivedLine:
        break
    receivedData += receivedLine

# Printing the data received from the server
print('From Server:', receivedData.decode())
# Closes the socket
clientSocket.close()
