import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print('my ip address is : '+IPAddr)