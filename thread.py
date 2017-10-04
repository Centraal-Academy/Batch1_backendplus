import threading
import time

lock= threading.Lock()

def cuadrado(lista):
    print("--------------lo voy a parar------------")
    lock.acquire()
    for x in lista:
        print("square:" + str(x*x))
    print("-----------------lo libero----------------")
    lock.release()

def cubo(lista):
    for x in lista:
        print("cube:" + str(x*x*x))


lista = range(1,10)

t = time.time()
print(threading.active_count())
# cuadrado(lista)
# cubo(lista)
hilo1 = threading.Thread(target=cuadrado, args=(lista,))
hilo2 = threading.Thread(target=cubo, args=(lista,))
hilo3 = threading.Thread(target=cuadrado, args=(lista,))
hilo4 = threading.Thread(target=cuadrado, args=(lista,))

hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
print("corriendo ----------->" + str(threading.active_count()))
hilo1.join()
hilo2.join()
print("done : " + str(time.time() - t))