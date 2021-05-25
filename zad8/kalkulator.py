import socket
def Oblicz(tablicaONP, stos):
    for znak in tablicaONP:
        stos.append(znak) if znak.isnumeric() else stos.append(SprDzialanie(int(stos.pop(-1)), int(stos.pop(-1)), znak))
    return stos[-1]


def SprDzialanie(p, l, znak):
    return {'+': l + p, '-': l - p, '*': l * p, '/': l / p, '%': l % p, '^': l ** p}.get(znak)

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 5050))
while True:
    server_socket.listen(1)
    (client_socket, client_address) = server_socket.accept()
    client_equation = client_socket.recv(1024)
    client_socket.send(('Twoje równianie: ' + client_equation.decode()+"\nTwój wynik: "+str(Oblicz((client_equation.decode()).split(), []))).encode())
    client_socket.close()
