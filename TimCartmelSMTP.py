####
# Timothy Cartmel
# This program is a simple SMTP mail client, and connects with a mail server using
# the SMTP protocol. Sends email message to mail server.
# It is assumed that the server is running from the same machine the client is. To run it use this from
# the command line:   python3 -m smtpd -c DebuggingServer -n 127.0.0.1:2000
# Development Computer: Dell XPS13
####
from socket import *

# Choose a mail server (e.g. Google mail server) and call it mail server
mailServer = '127.0.0.1'
mailPort = 2000

# Create socket called clientSocket and establish a TCP connection with mail server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))
# receive and decode response from the socket
recv = clientSocket.recv(1024).decode()
print('Server:' + recv)
# 220 gives the green light for the next step in the process
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO 127.0.0.1\r\n'
print('Client:' + heloCommand)
clientSocket.send(heloCommand.encode('utf-8'))
recv1 = clientSocket.recv(1024).decode()
print('Server:' + recv1)
# 250 gives the green light for the next step in the process
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# command = "STARTTLS\r\n"
# clientSocket.send(command)
# recva = clientSocket.recv(1024)
# print(recva)

mailfromCommand = 'MAIL FROM:<timcartmel@gmail.com>\r\n'
print('Client:' + mailfromCommand)
clientSocket.send(mailfromCommand.encode('utf-8'))
recv2 = clientSocket.recv(1024).decode()
print('Server:' + recv2)
# 250 gives the green light for the next step in the process
if recv2[:3] != '250':
    print('mail from 250 reply not received from server.')

# Send RCPT TO command and print server response.
rcpttoCommand = 'RCPT TO:<timcartmel@gmail.com>\r\n'
print('Client:' + rcpttoCommand)
clientSocket.send(rcpttoCommand.encode('utf-8'))
recv3 = clientSocket.recv(1024).decode()
print('Server:' + recv3)
# 250 gives the green light for the next step in the process
if recv3[:3] != '250':
    print('rcpt to 250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
print('Client:' + dataCommand)
clientSocket.send(dataCommand.encode('utf-8'))
recv4 = clientSocket.recv(1024).decode()
print('Server:' + recv4)
if recv4[:3] != '354':
    print('data 354 reply not received from server.')

# Send message data.
message = '\r\n I love computer networks!\r\n.\r\n'
print('Client:' + message)
# Message ends with a single period.
# mailMessageEnd = '\r\n.\r\n'
clientSocket.send(message.encode('utf-8'))
recv5 = clientSocket.recv(1024).decode()
print('Server:' + recv5)
if recv5[:3] != '250':
    print('end msg 250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'Quit\r\n'
print('Client:' + quitCommand)
clientSocket.send(quitCommand.encode('utf-8'))
recv6 = clientSocket.recv(1024).decode()
print('Server:' + recv6)
if recv6[:3] != '221':
    print('quit 221 reply not received from server.')

clientSocket.close()
