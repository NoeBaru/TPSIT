import threading

# Numero di connessioni socket attive
num_connessioni_socket = 0

# Semafori per sincronizzare l'apertura e la chiusura delle connessioni socket
semaforo_apertura = threading.Semaphore(1)  # Inizializzato a 1 per garantire l'accesso esclusivo
semaforo_chiusura = threading.Semaphore(1)  # Inizializzato a 1 inizialmente, nessuna chiusura è possibile

# Si può usare Lock per sincronizzare l'accesso al numero di connessioni socket al posto dei semafori
# Il lock acquisisce una risorsa e la rilascia esclusivamente, quindi assicura che solo un thread alla volta possa accedere alla sezione critica.
# se si usa Lock si deve agiungere la chiusura di: with lock
# lock = threading.Lock()

# Funzione per simulare l'apertura di una nuova connessione socket
def apri_connessione_socket():
    global num_connessioni_socket
    #  Il lock è  acquisito e viene rilasciato automaticamente alla fine del blocco
    # with lock:
    with semaforo_apertura:
        num_connessioni_socket += 1
    print("Nuova connessione socket aperta")

# Funzione per simulare la chiusura di una connessione socket
def chiudi_connessione_socket():
    global num_connessioni_socket
   # with lock:
    with semaforo_chiusura:
        num_connessioni_socket -= 1
    print("Connessione socket chiusa")

# Creazione di due thread per simulare l'apertura e la chiusura di connessioni socket
thread_apertura = threading.Thread(target=apri_connessione_socket)
thread_chiusura = threading.Thread(target=chiudi_connessione_socket)

# Avvio dei thread
thread_apertura.start()
thread_chiusura.start()

# Attendi il completamento dei thread
thread_apertura.join()
thread_chiusura.join()

# Stampare il numero finale di connessioni socket
print("Numero finale di connessioni socket:", num_connessioni_socket)
