import socket
import threading
import time

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

SEC_SMALTIMENTO = 30
lista = []
ticket = 0

class Smaltimento(threading.Thread):
    def __init__(self, connection, prenotato):
        super().__init__()
        self.connection = connection
        self.running = True
    def run(self):
        while self.running:
            time.sleep(SEC_SMALTIMENTO)

            self.kill()

    def kill(self):
        self.connection.close()
        self.running = False

class Client_handler(threading.Thread):
    def __init__(self, connection, prenotato, ticket):
        super().__init__()
        self.connection = connection
        self.running = True
        self.prenotato = prenotato
        self.numero = 0

    def run(self):
        while self.running:
            message = self.connection.recv(BUFFER_SIZE)#bloccante
            if message.decode() != "0":
                for indice, valore in enumerate(lista):
                    if lista == prenotato[]
                pass
            else:
                self.connection.sendall("chiusura in corso".encode())
                self.kill()

    def kill(self):
        self.connection.close()
        self.running = False

def main():
    """
    Author: Noemi Baruffolo
    date: 13/05/2024
    es. sportello - preparazione ver 
    text: prenotazione ad uno sportello, ogni utente che vuole prenotarsi attiva il client, ci si prenota tramite nome (ipotizzando non
    possano esistere al mondo persone con lo stesso nome per non stare a usare il codice fiscale o altro),
    bisogna controllare che non si siano già prenotati e dire a che numero si è in coda, ogni 30sec il server smaltiasce una persona
    tramite un secondo thread andando in ordine FIFO
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    while True:
        connection, lista[ticket], client_address = s.accept()#bloccante
        
        thread = Client_handler(connection, lista[ticket])
        thread.start()
        ticket += 1
    s.close()
if __name__ == '__main__':
    main()