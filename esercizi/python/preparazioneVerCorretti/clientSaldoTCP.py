import socket
SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def main():
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    messaggio = "1"
    while messaggio != "0":
        messaggio = input("cifra: ")
        s.sendall(messaggio.encode())
        message = s.recv(BUFFER_SIZE)
        print(message.decode())

    s.close()

if __name__ == "__main__":
    main()