import threading
import time

class myThread(Threading.Thread):
    def __init__ (self, threadID, name, counter):
        Threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run (self):
        print("starting" +self.name)
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        threadLock.release()
def print_time(ThreadName, delay, Counter)
    while counter:
        print(f"{threadName}:{time.ctime(time.time())}")
        counter -=1

threadLock = threading.Lock()
threads[]
Thread1 = myThread (1, "Thread -1", 1)
Thread2 = myThread (2, "Thread -2", 2)
thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print("Exiting Main Thread")
