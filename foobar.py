from threading import Thread, Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lockFoo = Lock()
        self.lockBar = Lock()
        self.lockBar.acquire()
        
    def foo(self, printFoo):
        for i in range(self.n):
            self.lockFoo.acquire()
            printFoo()
            self.lockBar.release()
            
    def bar(self, printBar):
        for i in range(self.n):
            self.lockBar.acquire()
            printBar()
            self.lockFoo.release()
            
def printFoo():
    print("foo", end="")
def printBar():
    print("bar", end="")
    
foobar = FooBar(2)

th_1 =Thread(target=foobar.foo, args=(printFoo, ))
th_2 =Thread(target=foobar.bar, args=(printBar, ))

th_1.start()
th_2.start()