import socket
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_num = '141.223.140.16'

server_socket.bind((ip_num, 12345))
print(ip_num, "binded")
server_socket.listen(0)
print("listened")

client_socket, addr = server_socket.accept()

while True:
    data = client_socket.recv(65535)
    print(data.decode())

