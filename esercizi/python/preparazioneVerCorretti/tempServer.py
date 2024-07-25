import socket
import threading
import random
MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

TEMPMAX = 50

class Client_handler(threading.Thread):
    def __init__(self,connection):
        super().__init__()
        self.connection = connection
        self.connecting = True
        self.allarme = False

    def run(self):
        while self.connecting:
            message = self.connection.recv(BUFFER_SIZE) #bloccante
            print(message)
            id, t = message.decode().split(":")
            temp = float(t)
            if temp >= TEMPMAX and self.allarme == False:
                print(f"{id} ALLARME TEMPERATURA ALTA".encode())
                self.allarme = True
            elif self.allarme == True:
                self.allarme = False
                print(f"{id} VALORE TEMPERATURA RIENTRATO".encode())


    def kill(self):
        self.connection.close()
        self.connecting = False

def main():
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    while True:
        connection, client_address= s.accept() #bloccante
        print(f"il client {client_address} si è connesso")
        thread = Client_handler(connection)
        thread.start()
    
    s.close()

if __name__ == "__main__":
    main()