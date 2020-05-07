import socket 
socket.setdefaulttimeout(2)
s = socket.socket()
#s.connect(("192.168.1.91",22))
s.connect(("172.21.113.61",22))
ans = s.recv(1024)

print ans 

