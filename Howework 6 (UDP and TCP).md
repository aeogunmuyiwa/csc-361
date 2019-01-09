# Homework 6 (UDP and TCP)

Please complete following questions in the space provided. Submit a modified version to Connex in the submission box. Consult the files **Wireshark_UDP_v7.0.pdf** if needed.

# Concepts
  - Connectionless vs Connection-oriented communication
  - What is inside a UDP datagram?
  - What is TCP?
  - How TCP connection is set up and taken down?


## UDP
- Make a copy of your solution to the online solutions of [UDP Socket Programming in Python (HTML)]( https://www.binarytides.com/programming-udp-sockets-in-python/) the two files, `udpclient.py` and `udpserver.py`, here in this folder.
- If you are running the Python code on your laptop using `localhost`, then start Wireshark with a capture filter `host 127.0.0.1`. Just capture the packets going between the `udpclient.py` and `udpserver.py`.
- Stop Wireshark when the Python scripts terminated.

Answer the following questions in the space provided:

Q1. Examine the first UDP packet, how many fields in the UDP datagram?
>
>5 fields
>

Q2. How many bytes are in the UDP **payload**? Check it against your `udpclient.py` code.
>
>9 bytes
>

Q3. What is the **protocol number** of UDP?
>
>UDP 17
>

Q4. Examine two UDP packets, one from the client and one from the server. What are the port numbers used in the client and in the server packets?
>client 57010
server ddi-udp-1 8888
>
>

## TCP
- Make a copy of your solution to [TCP Socket Programming in Python (HTML)]( https://www.binarytides.com/python-socket-programming-tutorial/) the two files, `tcpclient.py` and `tcpserver.py`, here in this folder.
- If you are running the Python code on your laptop using `localhost`, then start Wireshark with a capture filter `host 127.0.0.1`. Just capture the packets going between the `tcpclient.py` and `tcpserver.py`.

Answer the following questions in the space provided:

Q5. What are the packet numbers correspond to `connect` request?
>
>19
>

Q6. What are being exchanged between the client and server after a TCP connection is established?
>An Okay hello messege
>
>

Q7. What is the **source** port number of the client when the **client** is sending?
>
>Source port 37235
>

Q8. What is the **source** port number of the server when the **server** is responding?
>
>ddi-tcp2- 8889
>

Q9. What is the total number of bytes are received by the server when the connection is closed?
>66bytes
>
>

Q10. What is the total number of bytes are received by the client when the connection is closed?
>
>66 bytes
>

Q11. How many packets are exchanged when the connection is closed? What are being exchanged?
>
>none
>