import threading

def sum100():
    sum = 0
    for i in range(1, 101):
        sum += i
    print("sum100", threading.current_thread().getName())
    print(sum)
    
def sum200():
    sum = 0
    for i in range(1, 201):
        sum += i
    print("sum200", threading.current_thread().getName())
    print(sum)
    
sum_1 = threading.Thread(target=sum100, name="sum_100")
sum_2 = threading.Thread(target=sum200, name="sum_200")

sum_1.start()
sum_2.start()
    
# sum100()