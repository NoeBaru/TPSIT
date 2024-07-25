import socket
import random
import time
import uuid

SERVER_ADDRESS = ("localhost", 11000)
BUFF_SIZE = 4096
ID = str(uuid.uuid4()) #ID univoco diverso per ogni esecuzione del client

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
    s.connect(SERVER_ADDRESS)
    while True:
        temperature = random.gauss(50,15)
        s.sendall(f"{ID}:{temperature:.2f}".encode()) #invio temperatura al server
        time.sleep(2)
    s.close()

if __name__=="__main__":
    main()