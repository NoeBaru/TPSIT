import socket
import threading

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

class ClientHandler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
    def run(self):
        message = self.connection.recv(BUFFER_SIZE)
        print(message.decode())
        self.connection.sendall(message)
    def kill(self):
        self.connection.close()

def main():
    """
    Author: Noemi Baruffolo
    date: 09/05/2024
    es. 68 echo server TCP
    text: riceve, stampa, risponde, stampa
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    while True:
        connection, clientAddress =  s.accept() #bloccante
        print(f"Il client {clientAddress} si è connesso")
        thread = ClientHandler(connection)
        thread.start()

if __name__ == '__main__':
    main()