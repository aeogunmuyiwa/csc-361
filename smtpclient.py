from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver =("smtp.uvic.ca",25)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket=socket(AF_INET,SOCK_STREAM)

host=mailserver
port=25

clientSocket.connect(mailserver) 

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Send MAIL FROM command and print server response.
#email_from=input("MAIL FROM: ")
mailCommand="Mail From: <tashingaz@uvic.ca>\r\n"
clientSocket.send(mailCommand.encode())
recv2=clientSocket.recv(1024)
recv2=recv2.decode()
print("After Mail From command: "+recv2)
if recv1[:3]!='250':
	print('250 reply not received from server.')

	
# Send RCPT TO command and print server response. 
#recipient=input("RCPT TO: ")
rcptCommand="RCPT TO: <tashingaz@uvic.ca>\r\n"
clientSocket.send(rcptCommand.encode())
rcptRecv=clientSocket.recv(1024)
rcptRecv=rcptRecv.decode()
print("After RCPT TO command: "+rcptRecv)
if recv1[:3]!='250':
	print('250 reply not received from server.')



# Send DATA command and print server response. 
dataCommand="DATA\r\n"
clientSocket.send(dataCommand.encode())
dataRecv=clientSocket.recv(1024)
dataRecv=dataRecv.decode()
print ("After DATA command: "+dataRecv)
if recv1[:3]!='250':
	print('250 reply not received from server.')


# Send message data.
message=input("Enter your message :")
clientSocket.send(message.encode())
clientSocket.send(endmsg.encode())
recv_msg=clientSocket.recv(1024)
print("Response:"+recv_msg.decode())
if recv1[:3]!='250':
	print('250 reply not received from server.')

# Message ends with a single period.


# Send QUIT command and get server response.
clientSocket.send("Quit\r\n".encode())
message=clientSocket.recv(1024)
print(message)
if recv1[:3]!='250':
	print('250 reply not received from server.')

clientSocket.close()

