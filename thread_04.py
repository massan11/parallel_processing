import threading
import time

def clean_home():
    time.sleep(4)
    print("home finished")
    
def clean_yard():
    time.sleep(3)
    print("yard finished")
    
def invite_people():
    time.sleep(1.5)
    print("invite finished")
    
home_th = threading.Thread( target=clean_home, name="home")
yard_th = threading.Thread( target=clean_yard, name="yard")
invite_th = threading.Thread( target=invite_people, name="invite")

home_th.start()
yard_th.start()
home_th.join()
yard_th.join()

invite_th.start()