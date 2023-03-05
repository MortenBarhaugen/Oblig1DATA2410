# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Write your code here
serverPort = 15000
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)
# End of your code
while True:
    # Establish the connection print('Ready to serve...') connectionSocket, addr =
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        # Write your code here
        print('test')
        # End of your code
        message = connectionSocket.recv(1024)  # Write your code here #End of your code
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()  # Write your code here #End of your code
        # Send one HTTP header line into socket
        # Write your code here
        connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')
        # End of your code
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Write your code here
        errormsg = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(errormsg.encode())
        connectionSocket.close()
    # End of your code
    # Close client socket
    # Write your code here
    connectionSocket.close()
    # End of your code


sys.exit()  # Terminate the program after sending the corresponding data
