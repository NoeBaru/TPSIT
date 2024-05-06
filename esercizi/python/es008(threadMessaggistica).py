import socket
from threading import Thread

MY_ADDRESS = ("0.0.0.0", 9000) #prende l'ip del mio pc e funziona solo con il server
SERVER_ADDRESS = ("192.168.1.117", 9000)
BUFFER_SIZE = 4096

class ricevi_messaggio(Thread):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket
        self.running = True
    def run(self):
        while self.running:
            data, sender_address = self.socket.recvfrom(BUFFER_SIZE)
            string = data.decode()
            print(f"{sender_address}: {string}")
    def kill(self):
        self.running = False

class invia_messaggio(Thread):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket
        self.running = True
    def run(self):
        while True:
            data, sender_address = s.recvfrom(BUFFER_SIZE)
            print("Messaggio ricevuto da:", sender_address)
            elementMessage = data.decode().split("|")
            if len(elementMessage) == 3:
                message, destinatario_address, porta_destinatario = elementMessage
                try:
                    s.sendto(message.encode(), (destinatario_address, int(porta_destinatario)))
                    print(f"mando a {destinatario_address} : {porta_destinatario} message: {message} da parte di {sender_address}")
                except:
                    print(f"errore causato da {sender_address}")
            else:
                print("errore indirizzo ip destinatario")
                print(data.decode())

def main():
    """
    Author: Noemi Baruffolo
    date: 03/05/2024
    es. 
    text:
    Creare un sistema di messaggistica che permetta a due entità di comunicare tramite socket utilizzando thread separati per l'invio e
    la ricezione dei messaggi, usando:  
    - thread_invio
    - thread_ricezione

    Suggerimento:
    thread_invio = threading.Thread(target=invia_messaggio, args=("127.0.0.1", "Ciao!")) 
    thread_ricezione = threading.Thread(target=ricevi_messaggio) 
    """
    thread_invio = Thread.Thread(target = invia_messaggio, args=("127.0.0.1", "Ciao!")) 
    thread_ricezione = Thread.Thread(target = ricevi_messaggio)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ready = True
    receiver = ricevi_messaggio(s)

    while True:
        message = input("-> ")
        dest = input("Inserisci l'ip del destinatario: ")
        packet = f"{message}|{MY_ADDRESS}!{dest}"
        s.sendto(packet.encode(), SERVER_ADDRESS)
        if ready:
            receiver.start()
            ready= False
if __name__ == '__main__':
    main()