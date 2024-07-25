import socket
SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def main():
    """
    Author: Noemi Baruffolo
    date: 09/05/2024
    es. conto bancario chat TCP
    text: Creare server e client TCP che implementano il meccanismo di prelievo e versamento sul saldo
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    while True:
        string = input("> ")
        s.sendall(string.encode())
        message = s.recv(BUFFER_SIZE)#bloccante
        print(f"saldo: {message.decode()}")
        if string == "0":
            break
    s.close()


if __name__ == '__main__':
    main()