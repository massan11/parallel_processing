from threading import Thread, Lock

class Foo:
    def __init__(self):
        self.lock2 = Lock()
        self.lock3 = Lock()
        self.lock2.acquire()
        self.lock3.acquire()
    
    def first(self, printFirst):
        printFirst()
        self.lock2.release()
        
    def second(self, printSecond):
        self.lock2.acquire()
        printSecond()
        self.lock3.release()
        
    def third(self, printThird):
        self.lock3.acquire()
        printThird()
        
        
def print1():
    print("1", end="")
    
def print2():
    print("2", end="")
    
def print3():
    print("3", end="")
    
foo = Foo()

th_1 =Thread(target=foo.first, args=(print1, ))
th_2 =Thread(target=foo.second, args=(print2, ))
th_3 =Thread(target=foo.third, args=(print3, ))

th_3.start()
th_1.start()
th_2.start()
