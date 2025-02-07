from threading import Thread, Lock


class Greet:
    def __init__(self):
        self.lock_hello = Lock()
        self.lock_bye = Lock()
        self.lock_bye.acquire()

    def hello(self):
        self.lock_hello.acquire()
        print('hello', end=' ')
        self.lock_bye.release()
            
    def bye(self):
        self.lock_bye.acquire()
        print('bye', end=' ')
        self.lock_hello.release()

greet = Greet()

th_1 = Thread(target=greet.bye)
th_2 = Thread(target=greet.bye)
th_3 = Thread(target=greet.hello)
th_4 = Thread(target=greet.hello)


th_1.start()
th_2.start()
th_3.start()
th_4.start()