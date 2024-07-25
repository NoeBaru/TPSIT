import threading
import time

#lock = threading.Lock() #variabile globale, se ce ne fossero di più, si mettono nel main e si passano nella classe
semaforo = threading.Semaphore(1) #(1) n di thread per volta che possono esegire la sezione critica

class StampaNome(threading.Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    def run(self):
        for _ in range(5):
            semaforo.acquire()#lock.acquire() #oppure with lock: \n contenuto del for per evitare di fare acquire e release
            print("Ciao ", end = "") #inizio sezione critica
            time.sleep(1)
            print(self.nome) #fine sezione critica
            semaforo.release()#lock.release()
    def kill(self):
        pass

def main():
    """
    Author: Noemi Baruffolo
    date: 10/05/2024
    es. semafori
    text: semafori

    la lock permette di far passare un solo thread alla volta 

    threading.Semaphore(n)
    n thread alla volta possono eseguire la sezione critica, in questo caso uno, quindi è come la lock
    """

    '''thread = StampaNome("Mario")
    thread.start()
    thread.join()'''
    nomi = ["Mario", "Luca", "Alice", "Bob"]
    listaThread = [StampaNome(nome) for nome in nomi]
    for thread in listaThread:
        thread.start()
    for thread in listaThread:
        thread.join()

if __name__ == '__main__':
    main()