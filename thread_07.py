from threading import Thread, Lock

def synchronized(f):
    lock = Lock()
    def func(*args, **kwargs):
        with lock:
            f(*args, **kwargs)
    return func

counter = 0

@synchronized
def increase():
    global counter
    for _ in range(500000):
        counter += 1

def main():
    global counter
    counter = 0
    th_1 = Thread(target=increase)
    th_2 = Thread(target=increase)
    
    th_1.start()
    th_2.start()
    
    th_1.join()
    th_2.join()
    
main()
print(counter)