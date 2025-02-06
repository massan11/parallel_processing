import threading

count = 0

def increase():
    global count
    for _ in range(500000):
        count += 1
        
def count_money():
    global count
    count = 0
    
    th_1 = threading.Thread(target=increase)
    th_2 = threading.Thread(target=increase)
    th_3 = threading.Thread(target=increase)
    th_4 = threading.Thread(target=increase)
    
    th_1.start()
    th_2.start()
    th_3.start()
    th_4.start()
    
    # th_1.join()
    th_2.join()
    th_3.join()
    th_4.join()

for index in range(1, 6):
    count_money()
    print(f"count must be {4*500000} but it is {count}" )