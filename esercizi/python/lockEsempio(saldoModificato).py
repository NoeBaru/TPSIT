import threading
import time

saldo = 1000 #variabile globale(accessibile da tutte le classi e funzioni che facciamo, può essere solo letta e non modificata)
blocco = threading.Lock()

class Prelievo(threading.Thread):
    def __init__(self, file, percentuale):
        super().__init__()
        self.file = file
        self.percentuale = percentuale
        self.running = True
    def run(self):
        while self.running: #esegue simultaneamente su più thread, l'ordine dipende dalla CPU del computer
            with open(self.file, "r") as file: #si potrebbero usare due lock, uno per scrittura e uno per lettura
                saldoStr = file.readline()
            saldo = float(saldoStr)

            if saldo > 0:
                cifra = self.percentuale * (saldo /100)
                time.sleep(1)
                blocco.acquire() #acquisisce la lock
                saldo -= cifra #zona critica

                with open(self.file, "w") as file:
                    file.write(str(saldo))

                blocco.release() #rilascia la lock
                print(f"Il saldo aggiornato è {saldo}")
                time.sleep(5)
            else:
                print("Saldo in negativo")
                self.running = False
    def kill(self):
        self.running = False
def main():
    """
    Author: Noemi Baruffolo
    date: 06/05/2024
    es. lock
    text: lock, conto bancario saldo, prelievo e versamento di soldi

    race condition: si genera quando due o più thread concorrono ad usare la stessa risorsa.
    sezione critica di un thread: è la porzione di codice in cui il thread opera in scirttura sulla risorsa condivisa

    per lock:
    1.creo oggetto di tipo lock, che è un blocco.
    2.individuo l'area critica
    3.inserisco blocco.acquire(), in mezzo la riga critica, poi blocco.release() per acquisire e rilasciarela lock

    ////////MODIFICARE//////////
    modifico l'esercizio in modo che:
    - il saldo diventi un valore scritto in un file
    - ogni volta che vi opero, apro il file, leggo il valore, lo aggiorno e chiudo il file

    - dentro al Thread implementa un meccanismo che impedisca al saldo di diventare negativo
    - creiamo una lista di 10 thread con ciascuno una percentuale diversa dagli altri e li eseguiamo
    - nella classe thread implementiamo il metodo kill
    - il metodo Thread lascia eseguire i Thread per un minuto, poi li killa e fa la join
    """
    file = "saldo.txt"
    listaPrelievi = [5, -6]
    lista_thread = [Prelievo(file, n) for n in listaPrelievi]
    for t in lista_thread:
        t.start()
    time.sleep(60)
    for t in lista_thread:
        t.kill()
    for t in lista_thread:
        t.join()
if __name__ == '__main__':
    main()