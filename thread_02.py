import threading
import time

def get_info(name, age, job):
    time.sleep(4)
    thread_name = threading.currentThread().getName()
    print(f"{name} | {age} | {job} --> {thread_name}")
    
def get_info_0(name, job):
    time.sleep(1)
    thread_name = threading.currentThread().getName()
    print(f"{name} | {job} --> {thread_name}")

th_1 = threading.Thread(target=get_info, args=("mohammad", 19, "developer"))   
th_2 = threading.Thread(target=get_info_0, kwargs={"name":"ali", "job": "cio"}) 

th_1.start()
th_2.start()
    
# get_info("mohammad", "12", "developer")
# get_info_0("ali", "cio")