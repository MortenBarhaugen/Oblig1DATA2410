from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 5005
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)

print('Ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[0]
        f = open(filename[0:])
        outputdata = f.readlines()

        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()

    except IOError:
        errormsg = 'file was not found'
        connectionSocket.send(errormsg.encode())
