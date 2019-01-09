from socket import *
import time
import sys
clientSocket= socket(AF_INET, SOCK_DGRAM)
HOST=''#sys.argv[0]
port=12000#sys.argv[1]
ping='ping'

lstping=10
sequence_number=0
clientSocket.settimeout(1)
while sequence_number < lstping:
	sequence_number= sequence_number+1
	start=time.time()
	#message=[ping,`sequence_number`,`start`]
	#data=" ".join(message)
	print ('sequence number is:',sequence_number)
	clientSocket.sendto(ping, (HOST,port))
	#count=count+1
	try:
		d=clientSocket.recvfrom(1024)
		reply=d[0]
		addr=d[1]
	
		RTT=((time.time())-start)
		#print (RTT)
		print ('Reply from:',reply,' ',RTT)
	except:
		print("Request timeout")
clientSocket.close()	