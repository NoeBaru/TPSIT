#cercare di capire una password di N lettere minuscolo dell'alfabeto italiano

from threading import Thread
import time
password = "hbea"
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 'm', 'n','o','p','q','r','s','t','u','v','z']

class MioThread(Thread):
    def __init__(self, lettera):
        super().__init__()
        self.lettera = lettera

    def run(self):#qua ci sta il codice del thread
        print(f"sono il thread {self.lettera}")
        
        for l in alfabeto:
            for l2 in alfabeto:
                for l3 in alfabeto:
                    parola = self.lettera + l + l2 + l3
                    if parola == password:
                        print(f"trovata {parola}")  

def main():
    lista_thread = [MioThread(l) for l in alfabeto]
    for t in lista_thread:
         t.start()
    
    for t in lista_thread:
         t.join()
    
if __name__ == "__main__":
    main()