# I used this code as a base for this script: https://github.com/safiqul/2410/blob/main/thread/tcpserver-multi.py

import sys
import time
from socket import *
import _thread as thread

# A function that returns the current time
def now():
    return time.ctime(time.time())

# A client handler function
def handle_client(connectionSocket):
    while True:
        try:
            # Receives the message from the client
            message = connectionSocket.recv(1024).decode()
            # Finds the filename from the client-input
            filename = message.split()[0]
            # Opens the file with the filename
            f = open(filename[0:])
            # Reads the lines from the file
            outputdata = f.readlines()

            # Sends the HTTP header line to the client
            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

            # Loops through the file and sends all lines to client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            # Closes the socket
            connectionSocket.close()
            break

        # Handles exception (if file not found) and sends error-message to client
        except IOError:
            errormsg = 'file was not found'
            connectionSocket.send(errormsg.encode())
    # Closes the socket
    connectionSocket.close()

# Main-function that listens for new connections and creates new thread when new connection joins
def main():
    # Defining the server-port
    serverPort = 3005
    # Creating a TCP socket
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Exception handling if the address or port is already in use
    try:
        serverSocket.bind(('127.0.0.1', serverPort))
    except:
        print("Bind failed. Error : ")
        sys.exit()

    serverSocket.listen(1)
    print('Ready to receive')

    # Listens to incoming connections
    while True:
        # Accepts the connection
        connectionSocket, addr = serverSocket.accept()
        print('Server connected by ', addr)
        print('at ', now())
        # Creates new thread when new connection joins and calls the handle_client function
        # to send the content of the file to the client
        thread.start_new_thread(handle_client, (connectionSocket,))

    # Closes the socket
    serverSocket.close()

# If the script is the main program
if __name__ == '__main__':
    main()