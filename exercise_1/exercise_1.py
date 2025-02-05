import threading
from tasks import clean, invite, drink

clean_th = threading.Thread(target=clean, name="clean")
drink_th = threading.Thread(target=drink, name="drink")
invite_th = threading.Thread(target=invite, name="invite")

clean_th.start()
drink_th.start()

clean_th.join()
drink_th.join()

invite_th.start()

