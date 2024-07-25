import threading
import time

saldo = 1000 #variabile globale(accessibile da tutte le classi e funzioni che facciamo, può essere solo letta e non modificata)
blocco = threading.Lock()

class Prelievo(threading.Thread):
    def __init__(self, percentuale):
        super().__init__()
        self.percentuale = percentuale
    def run(self):
        global saldo #così possiamo modificare saldo che era già globale nel metodo
        while True: #esegue simultaneamente su più thread, l'ordine dipende dalla CPU del computer
            cifra = self.percentuale * (saldo /100)
            time.sleep(1)
            #BLOCCANTE
            #MUTEX: mutuamente esclusivo cioè che lo esegue un thread alla volta, non tutti i thread insieme
            blocco.acquire() #acquisisce la lock
            saldo -= cifra #zona critica
            blocco.release() #rilascia la lock
            print(f"Il saldo aggiornato è {saldo}")
            time.sleep(5)
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

    """
    luca = Prelievo(5)
    mario = Prelievo(-6)

    luca.start()
    mario.start()
if __name__ == '__main__':
    main()