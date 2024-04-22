from threading import Thread
import time

class MioThread(Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        self.running = True
    def run(self): #codice del thread
        while self.running:
            print(f"Sono il thread {self.nome}")
            time.sleep(1)
    def kill(self):
        self.running = False

def main():
    """
    Author: Noemi Baruffolo
    date: 8/04/2024
    es. 
    text: threading
    """
    listaNomi = {"Alice", "Bob", "Trudy"}
    listaThread = [MioThread(n) for n in listaNomi]
    for t in listaThread:
         t.start()

    for _ in range(4):
        print("Sono il main thread")
        time.sleep(1)
    
    for t in listaThread:
        t.kill()
        t.join()
    print("Sono il main thread e ho chiuso tutti gli altri")
if __name__ == '__main__':
    main()