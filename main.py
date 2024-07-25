import threading
import time

class GestoreStagioni:
    def __init__(self):
        self.stagioni = ["Primavera", "Estate", "Autunno", "Inverno"]
        self.semaphore = threading.Semaphore(1) #inizzializzasione del semaforo con val 1, per l'accesso alla lista
        self.stop_event = threading.Event() # segnala ai tred di non esegure più il ciclo

    def gestisci_stagioni(self):
        while not self.stop_event.is_set():
            time.sleep(0.3)  # Attesa per un intervallo di tempo
            #  self.semaphore.acquire()  # Acquisisci il semaforo
            with self.semaphore: # fa si che il semaforo abbia l'accesso alla lista
                if self.stagioni:
                    stagione_rimossa = self.stagioni.pop(0)  # Rimuovi la prima stagione dalla lista
                    print(f"{stagione_rimossa} rimossa.")
                  #  if len(self.stagioni) < 2:  # Se ci sono meno di due stagioni nella lista, aggiungine una
                       #self.stagioni.append("Stagione Aggiunta")
                  #  print("Stagione Aggiunta.")
        else:
            print("La lista delle stagioni è vuota.")
            # self.semaphore.release()  # Rilascia il semaforo

    def start(self):
        thread1 = threading.Thread(target=self.gestisci_stagioni) # creazione 1^ thread
        thread2 = threading.Thread(target=self.gestisci_stagioni) # creazione 2^ thread

        thread1.start()  # avvio 1^ thread
        thread2.start()  # avvio 2^ thread

        time.sleep(2)  # pausa 2 secondi

        self.stop_event.set()  # evento di stop

        thread1.join()  # attesa 1^ thread
        thread2.join() # attesa 2^ thread

        print("Stagioni finali:", self.stagioni)
        print("Operazioni di gestione delle stagioni completate.")

# Utilizzo della classe GestoreStagioni, creando un'istanza della classe GS
gestore_stagioni = GestoreStagioni()
gestore_stagioni.start() # avvio programma
