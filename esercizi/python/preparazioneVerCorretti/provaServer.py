import socket
import threading
import random
MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

continua = True
blocco = threading.Lock()
numRand = random.randint(1,100)
numRand = 9

class Client_handler(threading.Thread):
    def __init__(self,connection):
        super().__init__()
        self.connection = connection
        self.connecting = True

    def run(self):
        global continua
        while self.connecting:
            message = self.connection.recv(BUFFER_SIZE) #bloccante
            print(message)
            num = int(message.decode())
            blocco.acquire()
            if continua == False:
                self.connection.sendall("HAI PERSO".encode())
                self.kill()
            else:
                if num == numRand:
                    self.connection.sendall("HAI VINTO".encode())
                    continua = False
                    self.kill()
                elif num > numRand:
                    self.connection.sendall("TROPPO ALTO".encode())
                else:
                    self.connection.sendall("TROPPO BASSO".encode())
            blocco.release()

    def kill(self):
        self.connection.close()
        self.connecting = False

def main():
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    listaT = []
    while continua:
        connection, client_address= s.accept() #bloccante
        print(f"il client {client_address} si è connesso")
        thread = Client_handler(connection)
        thread.start()
        listaT.append(thread)
        
    print("fine gioco")
    s.close()

if __name__ == "__main__":
    main()