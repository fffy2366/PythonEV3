import socket
 
HOST='localhost'

PORT=3000

BUFFER=4096  

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((HOST,PORT))
sock.send('hello, tcpServer!')
recv=sock.recv(BUFFER)
print('[tcpServer said]: %s' % recv)
sock.close()