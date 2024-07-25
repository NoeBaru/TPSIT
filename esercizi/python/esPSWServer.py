import socket
import threading

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
PASSWORD = "zya"

class Password(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.running = True
    def run(self):
        while self.running:
            attemp = self.connection.recv(BUFFER_SIZE).decode()

            if attemp == PASSWORD:
                self.connection.sendall("Correct password!".encode())
                self.kill()
            elif attemp == "":
                print("Empty attemp, please retry")
            else:
                self.connection.sendall("Incorrect password!".encode())

    def kill(self):
        self.connection.close()
        self.running = False

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. PSW
    text: fare un server TCP in cui è memorizzata una password segreta.
    Sviluppare un client TCP con tante istanze che provi ad indovinare la password.
    Le password di 3 lettere minuscole, alfabeto UK.
    Per provare le password in parallelo, creare un file di testo che contenga tutte le possibili combinazioni delle password
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    print(f"Server in ascolto (IP: {MY_ADDRESS})")
    
    while True:
        connection, _ = s.accept() #bloccante
        thread = Password(connection)
        thread.start()
if __name__ == '__main__':
    main()