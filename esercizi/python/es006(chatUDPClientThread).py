import socket
from threading import Thread

SERVER_ADDRESS = ("192.168.1.124", 43210)
BUFFER_SIZE = 4096
MY_ADDRESS = ("0.0.0.0", 43210)
NICKNAME = "noe"

class Receiver(Thread):
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

def main():
    """
    Author: Noemi Baruffolo
    date: 22/04/2024
    es. 067
    text: fare una chat UDP client-server con thread principale che permette di ricevere ed inviare e l'altro solo di inviare
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(MY_ADDRESS)
    ready= True
    receiver = Receiver(s)
    while True:
        message = input("-> ")
        dest = input("Inserisci il nickname del destinatario: ")
        packet = f"{message}|{NICKNAME}|{dest}"
        s.sendto(packet.encode(), SERVER_ADDRESS)
        if ready:
            receiver.start()
            ready= False

if __name__ == "__main__":
    main()