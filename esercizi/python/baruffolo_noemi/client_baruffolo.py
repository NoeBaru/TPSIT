import socket

SERVER_ADDRESS = ("127.0.0.1", 9090) #indirizzo del server
BUFFER_SIZE = 4096

def main():
    """
    Author: Noemi Baruffolo
    date: 27/05/2024
    es. verifica TPSIT
    text: client della verifica di TPSIT
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #crea il socket
    s.connect(SERVER_ADDRESS)
    cerca = input("Inserisci l'azione (usa la '|' per seprare l'azione dal valore da cercare es.Cerca-nome|valore): ")   
    s.sendall(cerca.encode()) #invia tutti i dati presi in input
    message = s.recv(BUFFER_SIZE) #riceve il messaggio ricevuto dal server
    print(f"Ricevuto <{message.decode()}> dal server") #stampa il messaggio del server

    s.close()
    
if __name__ == '__main__':
    main()
