from socket import *
import sys  # In order to terminate the program with sys.exit()

# Creating a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
serverPort = 15000
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)

#Keeps the connection open for a client to connect to
while True:
    # Establising the connection
    print('Ready to serve...')
    # Accepting incoming connections
    connectionSocket, addr = serverSocket.accept()

    # Try to run this code block when looking for file
    try:
        # Receiving the file-name from client
        message = connectionSocket.recv(1024)
        # Splitting the request message into words
        filename = message.split()[1]
        # Opening the file for reading. The [1:] removes the first character of the filename (/)
        f = open(filename[1:])
        # Reads the file
        outputdata = f.read()
        # Sending HTTP header line into socket
        connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')

        # Sending the content of the requested file to the client
        # Loops through the file and sends all the encoded lines to client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        # Sending blank line to client that represents the end of the response headers
        connectionSocket.send("\r\n".encode())
        # Closing the socket
        connectionSocket.close()

    # Handles exceptions (if file not found)
    except IOError:
        # Sending an error message if the file is not found
        errormsg = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(errormsg.encode())
        connectionSocket.close()
    # Closes the client socket
    connectionSocket.close()

# Terminating the program
sys.exit()
