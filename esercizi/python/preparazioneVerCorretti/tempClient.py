import socket
import random
import time
import uuid

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFF_SIZE = 4096
ID = str(uuid.uuid4()) #ID univoco diverso per ogni esecuzione del client

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    while True:
        temperature = random.gauss(50,15)
        s.sendall(f"{ID}:{temperature:.2f}".encode()) #invio temperatura al server
        time.sleep(2)
    s.close()

if __name__=="__main__":
    main()