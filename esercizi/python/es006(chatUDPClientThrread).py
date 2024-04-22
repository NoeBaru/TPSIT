from threading import Thread
import time
import socket


class MioThread(Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        self.running = True
    def run(self): #codice del thread
        while self.running:
            SERVER_ADDRESS = ("127.0.0.1", 9000) #(in questo caso di LoopBack) indirizzo che identifica il processo server
            BUFFER_SIZE = 4096 #byte
            
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #ho creato il socket
            while True:
                string = input("-> ")
                binaryString = string.encode()
                s.sendto(binaryString, SERVER_ADDRESS) #lega s al mio indirizzo
                data, senderAddress = s.recvfrom(BUFFER_SIZE) #riceve dei dati e dice chi li ha mandati
                string = data.decode()
                print(f"Ricevuto {string} da {senderAddress}")
                if string == "EXIT":
                    self.nome.kill()
                    self.nome.join()
                    break    
    def kill(self):
        self.running = False

def main():
    """
    Author: Noemi Baruffolo
    date: 22/04/2024
    es. 067
    text: fare una chat UDP client-server con thread principale che permette di ricevere ed inviare e l'altro solo di inviare
    """
    ricevitore =  MioThread("ricevitore")
    emittente = MioThread("emittente")
    ricevitore.start()
    emittente.start()
if __name__ == '__main__':
    main()