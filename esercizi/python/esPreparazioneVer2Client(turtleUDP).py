import socket

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def main():
    """
    Author: Noemi Baruffolo
    date: 13/05/2024
    es. turtle UDP
    text: creare una chat client-server UDP in modo che il client comandi la turtle del server tramite comandi
    comandi: direzione e di quanto
    """
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        com = input("Inserisci il comando: ")
        size = input("Inserisci lo spostamento/angolo: ")

        message = f"{com}|{size}"

        s.sendto(message.encode(), SERVER_ADDRESS)
        serverMessage, _ = s.recvfrom(BUFFER_SIZE)
        print(serverMessage.decode())

    s.close()

if __name__ == '__main__':
    main()