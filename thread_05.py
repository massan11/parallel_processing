import threading
import time

def invite(clean_event):
    print("inviting is waiting for cleaning finished")
    waiting = clean_event.wait(2)
    if waiting:
        print("inviting started after cleaning")
    else:
        print("inviting started before cleaning")
    time.sleep(2)
    print("inviting finished")
    print(waiting)
    
def clean(clean_event):
    print("cleaning is starting")
    time.sleep(3)
    print("cleaning finished")
    clean_event.set()
    
event = threading.Event()
    
th_invite = threading.Thread(target=invite, args=(event, ))
th_clean = threading.Thread(target=clean, args=(event, ))

th_invite.start()
th_clean.start()
