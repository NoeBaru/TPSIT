import socket
import time
import threading

MY_ADDRESS = ("127.0.0.1", 11000)
BUFFER_SIZE = 4096

class Temperatura(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        self.temp = -1
        self.tempPrec = -1

    def run(self):
        while True: #esegue simultaneamente su più thread, l'ordine dipende dalla CPU del computer
            string = self.connection.recv(BUFFER_SIZE)
            message = string.decode()
            listaMessaggi = message.split(":")
            self.temp = float(listaMessaggi[1])
            uid = listaMessaggi[0]
            if self.temp >= 70 and self.tempPrec < 70:
                print(f"ALLARME per {uid}")
            if self.temp < 70 and self.tempPrec >= 70:
                print(f"ALLARME per {uid} rientrato")
            self.tempPrec = self.temp
    
    def kill(self):
        self.connection.close()

def main():
    """
    Author: Noemi Baruffolo
    date: 20/05/2024
    es. CPU
    text: Il seguente client invia a un server di controllo la temperatura della CPU  (simulata con un numero pseudocasuale) e
    il suo ID univoco. Il server deve ricevere ID e temperatura da tutti i
    client che si connettono. Inoltre il server deve stampare un allarme per
    quei client con temperatura >=70°C. L'allarme deve essere stampato
    soltanto al superamento della temperatura di 70°C, per cui quando la
    temperatura scende nuovamente sotto i 70°C, il server stampa che
    l'allarme è rientrato. In tutte le stampe deve essere  presente l'ID
    univoco del client.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    while True:
        connection, _ = s.accept()#bloccante
        thread = Temperatura(connection)
        thread.start()
    s.close()
if __name__ == '__main__':
    main()