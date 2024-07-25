import socket
import threading
import time

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
PASSWORD_FILE = "passwords.txt"
blocco = threading.Lock()
correct = False

class PasswordGuesser(threading.Thread):
    def __init__(self, response):
        super().__init__()
        self.response = response

    def run(self):
        with open(PASSWORD_FILE, 'r') as file: #legge dal file delle combinazioni
            passwords = file.readlines()
            partOfPasswords = passwords[:3]
        
        if self.reponse == "Correct password!":
            correct = True

        if correct:
            print(f"Password trovata: {self.passwords}")

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. PSW
    text: fare un server TCP in cui è memorizzata una password segreta.
    Sviluppare un client TCP con tante istanze che provi ad indovinare la password.
    Le password di 3 lettere minuscole, alfabeto UK.
    Per provare le password in parallelo, creare un file di testo che contenga tutte le possibili combinazioni delle password
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)

    file = "passwords.txt"
    nTentativi = 3
    lista_thread = [PasswordGuesser(file) for n in nTentativi]

    for t in lista_thread:
        t.start()
    time.sleep(60)
    for t in lista_thread:
        t.kill()
    for t in lista_thread:
        t.join()

    s.close()
if __name__ == "__main__":
    main()
