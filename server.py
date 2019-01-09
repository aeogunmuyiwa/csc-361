#import socket module
from socket import *
import sys # In order to terminate the program
import datetime
today=datetime.date.today()

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
#?????????????????
host=''
port=8887
serverSocket.bind((host,port))

serverSocket.listen(5)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #??????????????? 
            
    try:
        message = connectionSocket.recv(1024)#?????????????????               
        filename = message.split()[1]                 
        f = open(filename[1:]) 

        outputdata = f.read()#???????????????                  
        #Send one HTTP header line into socket
        #?????????????
	connectionSocket.send('HTTP/1.1 200 OK\r\n')
	connectionSocket.send('Date:%s\r\n'%today)
	

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #????????????
	 
	connectionSocket.send('404 Not Found\n')

        #Close client socket
        #????????????
	connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
