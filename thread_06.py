import threading

class Counter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()
        
    def increase(self):
        self._lock.acquire()
        self.value += 1
        self._lock.release()
            
            
def increase(count):
    for _ in range(500000):
        count.increase()
            
    
        
def count_money():
    
    count = Counter()
    
    th_1 = threading.Thread(target=increase, args=(count, ))
    th_2 = threading.Thread(target=increase, args=(count, ))
    
    th_1.start()
    th_2.start()
    
    th_1.join()
    th_2.join()
       
    return count

for index in range(1, 6):
    count = count_money()
    print(f"count must be {500000*2} but it is {count.value}" )