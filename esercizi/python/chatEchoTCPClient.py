import socket

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096


def main():
    """
    Author: Noemi Baruffolo
    date: 09/05/2024
    es. 68 echo CLIENT TCP
    text: si connette, manda, riceve e stampa
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    s.sendall("Messaggio del client".encode())
    message = s.recv(BUFFER_SIZE)
    print(f"Ricevuto <{message.decode()}> dal server")

    s.close()
if __name__ == '__main__':
    main()