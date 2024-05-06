import socket
import csv
from threading import Thread

MY_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096

class Receive(Thread):
    def __init__(self, s):
        super().__init__()
        self.s = s
        self.running = True
        self.sender_address= None
    def run(self):
        while self.running:
            data, self.sender_address = self.s.recvfrom(BUFFER_SIZE)
            string = data.decode()
            print(f"{self.sender_address}: {string}")
            
    def kill(self):
        self.running = False

def loadRubrica(nomeFIle):
    rubrica = {}
    with open(nomeFIle, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            nome, ip, porta =  row
            rubrica[nome] = (ip, int(porta))
    return rubrica

def main():
    """
    Author: Noemi Baruffolo
    date: 22/04/2024
    es. 067
    text: fare una chat UDP client-server con thread principale che permette di ricevere ed inviare e l'altro solo di inviare
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(MY_ADDRESS)
    rubrica = loadRubrica("rubrica.csv")
    
    # Starting thread
    receiver = Receive(s)
    receiver.start()

    while True:
        # Send message
        if receiver.sender_address != None:
            string = input("-> ")
            binary_string = string.encode()
            s.sendto(binary_string, receiver.sender_address)

if __name__ == '__main__':
    main()