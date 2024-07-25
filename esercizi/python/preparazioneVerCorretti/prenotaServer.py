import socket
import threading
import time
MY_ADDRESS = ("127.0.0.1", 9080)
BUFFER_SIZE = 4096
blocco = threading.Lock()
TIME = 3
lista = []

class Client_handler(threading.Thread):
    def __init__(self,connection):
        super().__init__()
        self.connection = connection
        self.connecting = True

    def run(self):
        message = self.connection.recv(BUFFER_SIZE) #bloccante
        if message != '':
            if message.decode() in lista:
                messaggio = "impossibile. nome già presente"
            else:
                lista.append(message.decode())
                messaggio = "sei in posizione" + str(len(lista))

            self.connection.sendall(messaggio.encode())

    def kill(self):
        self.connection.close()
        self.connecting = False

class Timer(threading.Thread):
    def __init__(self):
        super().__init__()
        global lista

    def run(self):
        while True:
            time.sleep(TIME)
            if len(lista) > 0:
                lista.pop(0)
                print(f"lista aggiornata: {lista}")
            else:
                print("lista vuota")
                

    
def main():
    t = Timer()
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    t.start()
    while True:
        connection, client_address= s.accept() #bloccante
        print(f"il client {client_address} si è connesso")
        thread = Client_handler(connection)
        thread.start()
    s.close()

if __name__ == "__main__":
    main()