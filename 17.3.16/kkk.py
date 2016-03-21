import threading
import time

t4 = 7500


class FirstThread(threading.Thread):
    def run(self):
        t1 = 0
        for i in range(2500):
            t1 = t1 + 1
            print('t1 is ', t1)


class SecondThread(threading.Thread):
    def run(self):
        t2 = 2500
        for i in range(2500):
            t2 = t2 + 1
            print('t2 is ', t2)


class ThirdThread(threading.Thread):
    def run(self):
        t3 = 5000
        for i in range(2500):
            t3 = t3 + 1
            print('t3 is ', t3)


FirstThread().start()
SecondThread().start()
ThirdThread().start()
for i in range(2500):
    t4 = t4 + 1
    print('t4 is ', t4)

print(time.process_time())
