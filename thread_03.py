import threading
import time

def greetings():
    time.sleep(5)
    print("Hello")
    
    
daemon = threading.Thread( target=greetings, name="greet")
daemon.setDaemon(True)
daemon.start()
print("finished")
time.sleep(5.4)
print(daemon.is_alive())