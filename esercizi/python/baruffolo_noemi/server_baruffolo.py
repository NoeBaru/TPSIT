import socket
import threading

MY_ADDRESS = ("127.0.0.1", 9090) #indirizzo del server di loopback
BUFFER_SIZE = 4096
rubricaTelefonica = { # "nome e cognome del contatto" : "numero di telefono"
    "Mario Rossi": "123-456-7890",
    "Luca Bianchi": "234-567-8901",
    "Giulia Verdi": "345-678-9012",
    "Elena Neri": "456-789-0123",
    "Roberto Russo": "567-890-1234"
    }

class ClientHandler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.running = True
    def run(self):
        while self.running:
            message = self.connection.recv(BUFFER_SIZE)
            print(message.decode())
            elementMessage = message.decode().split("|") #separo l'azione richiesta dal valore 
            message, richiesta = elementMessage #inserisco in due variabili diverse il messaggio e il valore ricevuti
            #contorollo quale valore mi viene inviato, se numero o nome o un nuovo contatto da inserire
            if message == "Cerca-numero": 
                numero = richiesta
                print(numero)
            elif message == "Cerca-nome":
                nome = richiesta
                print(nome)
            elif elementMessage == "Aggiungi-contatto":
                nuovoContatto = message.decode().split(";")
                print(nuovoContatto)
                nomeNuovo, numeroNuovo = nuovoContatto
                rubricaTelefonica[nomeNuovo] = [numeroNuovo]
                self.connection.sendall("Ok")

            for chiave in rubricaTelefonica: #scorro sui contatti
                for valore in rubricaTelefonica[chiave]: #scorro sul numero di telefono
                    if numero == valore:
                        self.connection.sendall(f"Trovato! Contatto: {chiave} - numero: {valore}")
                        print(f"Trovato! Contatto: {chiave} - numero: {valore}")
                    else:
                        self.connection.sendall("Numero non trovato")
                        print("Numero non trovato")

                if nome == chiave:
                    self.connection.sendall(f"Trovato! Contatto: {chiave} - numero: {valore}")
                    print(f"Trovato! Contatto: {chiave} - numero: {valore}")
                else:
                    self.connection.sendall("Nome non trovato")
                    print("Nome non trovato")

    def kill(self): #non serve
        self.connection.close()
        self.running = False

def main():
    """
    Author: Noemi Baruffolo
    date: 27/05/2024
    es. verifica TPSIT
    text: server della verifica di TPSIT
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creazione del socket
    s.bind(MY_ADDRESS)
    s.listen() #mette il server in ascolto per ricevere messaggi

    while True:
        connection, clientAddress =  s.accept() #bloccante
        print(f"Il client {clientAddress} si è connesso")
        thread = ClientHandler(connection) #crea il thread
        thread.start()
    
if __name__ == '__main__':
    main()
