#Saldo diventa un valore scritto in un file
#Ogni volta che vi opero, apro il file, leggo il valore, lo aggiorno e chiudo il file
#Dentro al Thread implementa meccanismo che impedisca al saldo di diventare negativo
#Creiamo una lista di 10 Thread, ciascuno con percentuale differente, e li eseguiamo
#Dentro la classe Thread implementiamo il metodo kill
#Il main Thread lascia eseguire i Thread per un minuto, li killa e fa la join

import threading
import time

blocco = threading.Lock()
saldo = 1000

class Prelievo(threading.Thread):
    def __init__(self, perc, file):
        super().__init__()
        self.percentuale = perc
        self.file = file
        self.running = True
    
    def run(self):
        while self.running:
            with open(self.file, "r") as file:
                saldo = float(file.readline())
            if saldo > 0:
                cifra = self.percentuale * saldo / 100
                #il primo thread acquisisce la lock ed è l'unico che opera
                #BLOCCANTE, mutex = mutuamente esclusivo
                saldo -= cifra      #sezione critica
                blocco.acquire()
                with open(self.file, "w") as file:
                    file.write(f"{saldo}")
                blocco.release()
                print(f"il conto aggiornato è: {saldo}")
                time.sleep(1)
            else:
                print("saldo negativo")
                self.running = False

def main():

    luca = Prelievo(5, "saldo.txt")
    mario = Prelievo(-6, "saldo.txt")

    #la sezione critica di un thread è la porzione di codice 
    #in cui il thread opera sulla risorsa condivisa

    #race condition -> concorrono su una stessa variabile         
    mario.start()
    luca.start()

    mario.join()
    luca.join()

if __name__ == "__main__":
    main()