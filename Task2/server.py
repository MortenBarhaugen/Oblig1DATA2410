import sys
from socket import *
# Creating a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Defining the port and IP the server will listen to
serverPort = 5005
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)

print('Ready to receive')
# Listens to connections while the socket is open
while True:
    # Accepts incoming connections
    connectionSocket, addr = serverSocket.accept()

    # Try to run the code in this block
    try:
        # Receiving message from client
        message = connectionSocket.recv(1024).decode()
        # Finds the filename from the client and opens that file
        filename = message.split()[0]
        f = open(filename[0:])

        # Reads the lines from the file
        outputdata = f.readlines()

        # Sending the HTTP header line to client
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

        # Loops through the file and sends each line to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        # Closes the socket
        connectionSocket.close()

    # Handles exceptions (if file not found) and sends error message to client
    except IOError:
        errormsg = 'file was not found'
        connectionSocket.send(errormsg.encode())
        # Closes the socket
        connectionSocket.close()

# Terminating the program
sys.exit()
