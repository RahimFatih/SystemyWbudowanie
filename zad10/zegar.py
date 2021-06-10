import time
import threading
import msvcrt


t = time.time()
keyM = "a"


def thread1():
    global keyM
    global t
    
    lock = threading.Lock()
    while True:
        with lock:
            keyM = msvcrt.getch()
            if keyM == b"s":
                my_string = str(input('Enter date(yyyy-mm-dd hh:mm): '))
                t = time.mktime(time.strptime(my_string, "%Y-%m-%d %H:%M"))
                keyM="a"
            



threading.Thread(target = thread1).start()

while True:
    result = time.asctime(time.localtime(t))
    if(keyM!=b"s"):
        print("Time: ", result)
    time.sleep(1)
    t=t+1
