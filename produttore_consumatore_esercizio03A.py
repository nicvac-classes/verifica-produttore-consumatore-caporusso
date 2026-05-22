import threading
import random

DIM_BUFFER = 5
N_PRODUTTORI = 3
N_CONSUMATORI = 2
N_ORDINI = 6

buffer = [None] * DIM_BUFFER
metti = 0
togli = 0

vuoto = threading.Semaphore(DIM_BUFFER)
pieno = threading.Semaphore(0)
mutexP = threading.Semaphore(1)
mutexC = threading.Semaphore(1)


def genera_ordine():
    return f"ORD-{random.randint(10000, 99999)}"


class ProduttoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

    # DA IMPLEMENTARE (run)
     def run(self):
        global metti

        while i_metti<N_ORDINI:
            vuoto.acquire()
            mutexP.acqiure()
            i_metti=metti
            metti=[metti+1] % DIM_BUFFER
            mutexP.release()

            buffer[i_metti]=self.dato
            print(-PROD[self.idx] for [self.dato] in buffer[i_metti])

            self.dato+=1
            pieno.release()



class ConsumatoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

    # DA IMPLEMENTARE (run)
    def run(self):
        global togli

        esco=false
        while not esco:
            pieno.acquire()
            mutexC.acquire()
            i_togli=togli
            togli=[togli+1] & DIM_BUFFER
            mutexC.release()

            dato=buffer[i_togli]
            if dato==none:
                esco=true
                print---
                else
                print---

            self.dato+=1
            vuoto.release()
    
   



def main():
    global metti

    produttori = [ProduttoreThread(i + 1) for i in range(N_PRODUTTORI)]
    consumatori = [ConsumatoreThread(i + 1) for i in range(N_CONSUMATORI)]

    # DA IMPLEMENTARE: start dei thread produttori e consumatori
    for p in produttori:
        p.start()
    for c in consumatori:
        c.start()    

    # DA IMPLEMENTARE: join di tutti i produttori
    for p in produttori:
        p.join()

    print("Tutti i canali hanno terminato. Chiusura addetti...")

    # Invia un messaggio None per ogni addetto.
    for _ in range(N_CONSUMATORI):
        # DA IMPLEMENTARE: inserire None nel buffer
        pass

    # DA IMPLEMENTARE: join di tutti i consumatori
    for c in consumatori:
        c.join()

    print("Magazzino chiuso.")


if __name__ == "__main__":
    main()
