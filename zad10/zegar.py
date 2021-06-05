import time
import threading


t = time.time()



def zegar(t):
    i=0
    while True:
        result = time.asctime(time.localtime(t))
        print("Result:", result)
        time.sleep(1)
        t=t+1
        i=i+1
        if i>15:
            break


x = threading.Thread(target=zegar,args=(t,))


x.start()
time.sleep(10)
print("minelo10selk")
x.join()
print("koniec")
quit()
# x.join()
