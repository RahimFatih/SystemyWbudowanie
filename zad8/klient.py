import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('127.0.0.1', 5050))
name = input("Podaj wyrazenia arytmetyczne w ONP\nDostępne operatory: +,-,*,/,%,^\n")
my_socket.send(name.encode())
data = my_socket.recv(1024)
print(data.decode())
my_socket.close()