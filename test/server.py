#import socket module

from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#prepare a server socket

serverSocket.bind(('127.0.0.1', 11001))
serverSocket.listen(1)

while True:

    #Establish the connection

    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print('connected from', addr)
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        print(filename)
        f = open(filename[1:])
        outputdata = f.read()

        #Send one HTTP header line into socket

        #connectionSocket.send('HTTP/1.1 200 OK')
        connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')

        #Send the content of the requested file to the client

        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        print('IOError')

        #Send response message for file not found

        connectionSocket.send(b'file not found')

        #Close Client socket

        connectionSocket.close()
serverSocket.close()
