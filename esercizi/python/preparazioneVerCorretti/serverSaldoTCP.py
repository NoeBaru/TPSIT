import socket
import threading
MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
blocco = threading.Lock()

class Client_handler(threading.Thread):
    def __init__(self,connection,file):
        super().__init__()
        self.connection = connection
        self.connecting = True
        self.file = file

    def run(self):
        while self.connecting:
            message = self.connection.recv(BUFFER_SIZE) #bloccante
            print(message)
            with open(self.file, "r") as file:
                saldo = float(file.readline())
            if saldo > 0 and (float(message.decode())!=0 and float(message.decode())>0):
                cifra = float(message.decode()) * saldo / 100
                saldo += cifra
                blocco.acquire()
                with open(self.file, "w") as file:  #sezione critica
                    file.write(f"{saldo}")
                blocco.release()
                messageSaldo = "il conto aggiornato è: " + str(saldo)
                self.connection.sendall(messageSaldo.encode())
            elif float(message.decode()) == 0:
                self.kill()
            else:
                self.connection.sendall("saldo negativo, non puoi prelevare".encode())
            print(messageSaldo)

            

    def kill(self):
        self.connection.close()
        self.connecting = False

def main():
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    listaT = []
    while True:
        connection, client_address= s.accept() #bloccante
        print(f"il client {client_address} si è connesso")
        thread = Client_handler(connection, "saldo.txt")
        thread.start()
        listaT.append(thread)
    
    s.close()

if __name__ == "__main__":
    main()