# I used this code as a base for this script: https://github.com/safiqul/2410/blob/main/thread/tcpclient-multi.py

import sys
from socket import *

# Continually prompt the client for input until the program is terminated
while True:
    # Getting input from the user and splitting them into individual words
    clientInput = input('Write hostname, server-port, filename: ')
    inputList = clientInput.split()

    # Assigning the name and port of the server as well as the filename to variables
    serverName = inputList[0]
    serverPort = int(inputList[1])
    filename = inputList[2]

    # Creating a TCP socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Try to connect to the server with the given serverName and serverPort
    try:
        clientSocket.connect((serverName, serverPort))
    except:
        print("Connection error!")
        sys.exit()

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

# Terminates the program
sys.exit()
