import turtle
import socket

MY_ADDRESS = ("127.0.0.1", 9090)
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
    s.bind(MY_ADDRESS)

    t = turtle.Turtle()
    window = turtle.Screen()

    movements = {"forward": t.forward, "backword": t.backward, "left": t.left, "right": t.right}
    
    while True:
        message, address = s.recvfrom(BUFFER_SIZE)
        message = message.decode()

        com, size = message.split('|')

        '''if(com == "forward"):
            t.forward(int(size))
        elif (com == "backward"):
            t.backward(int(size))
        elif (com == "left"):
            t.left(int(size))
        elif (com == "right"):
            t.right(int(size))
        else:
            s.sendto(f"Comando {com} non ricoosciuto".encode(), address)'''
        
        if com in movements:
            movements[com](int(size))
            s.sendto(f"Comando {com} eseguito".encode(), address)
        else:
            print(f"comando {com} non riconosciuto")
            s.sendto(f"Comando {com} non ricoosciuto".encode(), address)

if __name__ == '__main__':
    main()