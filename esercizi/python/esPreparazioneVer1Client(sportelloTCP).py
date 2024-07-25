import socket
SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def main():
    """
    Author: Noemi Baruffolo
    date: 13/05/2024
    es. sportello - preparazione ver
    text: prenotazione ad uno sportello, ogni utente che vuole prenotarsi attiva il client, ci si prenota tramite nome,
    bisogna controllare che non si siano già prenotati, ogni 30sec il server smaltiasce una persona
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    while True:
        string = input("Inserisci il nome della prenotazione: ")
        s.sendall(string.encode())
        message = s.recv(BUFFER_SIZE)#bloccante

        '''print(f"STOP: {message.decode()}")
        if string == "0":
            break'''
    s.close()
if __name__ == '__main__':
    main()