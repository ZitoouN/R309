import socket

def Client():
    server_host = '127.0.0.1'
    port = 8080

    client_server = socket.socket()
    client_server.connect((server_host, port))

    msg = ""

    while msg != 'arret' and msg != 'bye':
        message = str(input("Moi : "))
        client_server.send(message.encode())
        msg = client_server.recv(1024).decode()

    client_server.close()


if __name__ == '__main__':
    print("---Bienvenue sur le serveur---")
    Client()