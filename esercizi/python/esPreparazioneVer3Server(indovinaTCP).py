import socket
import threading
import time
import random

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
number = int(random.randrange(1,101))
print(f"Il numero casuale è: {number}")
clientConnessi = {}

class Number(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.running = False
    def run(self):
        while self.running: #esegue simultaneamente su più thread, l'ordine dipende dalla CPU del computer
            data = self.connection.recv(BUFFER_SIZE)
            if int(data.decode()) == number:
                message =  "HAI VINTO"
                self.connection.sendall(message.encode())
                self.kill()
            elif int(data.decode()) < number:
                message =  "TROPPO BASSO"
                self.connection.sendall(message.encode())
            elif int(data.decode()) > number:
                message =  "TROPPO alTO"
                self.connection.sendall(message.encode())
            else:
                message = "errore!"
                self.connection.sendall(message.encode())

    
    def kill(self):
        self.connection.close()
        self.running = False

def main():
    """
    Author: Noemi Baruffolo
    date: 20/05/2024
    es. indovina il numero
    text:
    -creare un server TCP che quando viene eseguito sorteggia un numero intero casuale tra 1 e 100
    -al server si connettono almeno due client
    -gli utenti tramite i client inviano al server un numero tentando di indovinare il numero casuale scelto dal server
    - il server risponde ai client nei seguenti modi:
        * "HAI VINTO" se il client ha indovinato il numero
        * "TROPPO BASSO" se il numero del client è minore
        * "TROPPO ALTO" se il numero del client è maggiore
    -quando un client vince, agli altri viene inviato "HAI PERSO"
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    while True:
        connection, client_address = s.accept()#bloccante
        thread = Number(connection)
        '''if vinto:
            print("HAI PERSO")'''
        thread.start()
    s.close()
if __name__ == '__main__':
    main()