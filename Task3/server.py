import sys
import time
from socket import *
import _thread as thread

def now():
    return time.ctime(time.time())

def handle_client(connectionSocket):
    while True:
        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[0]
            f = open(filename[0:])
            outputdata = f.readlines()

            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.close
            break

        except IOError:
            errormsg = 'file was not found'
            connectionSocket.send(errormsg.encode())
    connectionSocket.close()

def main():
    serverPort = 3005
    serverSocket = socket(AF_INET, SOCK_STREAM)
    try:
        serverSocket.bind(('127.0.0.1', serverPort))
    except:
        print("Bind failed. Error : ")
        sys.exit()
    serverSocket.listen(1)

    print('Ready to receive')

    while True:
        connectionSocket, addr = serverSocket.accept()
        print('Server connected by ', addr)
        print('at ', now())
        thread.start_new_thread(handle_client, (connectionSocket,))
    serverSocket.close()

if __name__ == '__main__':
    main()