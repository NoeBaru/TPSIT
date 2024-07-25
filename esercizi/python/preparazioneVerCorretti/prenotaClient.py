#client invia nome
#server lo mette in coda e manda posizione 
#se client si prenota due volte lo avvisa e non si aggiunge
#una persona è in coda per 30 secondi

import socket
SERVER_ADDRESS = ("127.0.0.1", 9080)
BUFFER_SIZE = 4096

def main():
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    messaggio = input("nome: ")
    s.sendall(messaggio.encode())
    message = s.recv(BUFFER_SIZE)
    print(message.decode())

    s.close()

if __name__ == "__main__":
    main()