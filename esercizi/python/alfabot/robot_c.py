import socket

SERVER_ADDRESS = ("192.168.1.146", 8000)
BUFFER_SIZE = 4096

def main():
    """
    Author: Noemi Baruffolo
    date: 03/06/2024
    es. robot CLIENT TCP
    text: si connette, manda, riceve e stampa
    """
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    while True:
        string = input("Inserisci il comando (es.f;5 va avanti di 5 secondi o scrivi 'help' per vedere i comandi possibili o 'EXIT' per uscire): ")
        s.sendall(string.encode())
        message = s.recv(BUFFER_SIZE)
        print(f"Ricevuto <{message.decode()}> dal server")
    s.close()

    s.close()
if __name__ == '__main__':
    main()