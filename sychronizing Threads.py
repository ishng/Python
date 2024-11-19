import threading
import time

class myThread(threading.Thread):
    def __init__ (self, threadID, name, Counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.Counter = Counter
    def run (self):
        print("starting" +self.name)
        threadLock.acquire()
        print_time(self.name, self.Counter, 3)
        threadLock.release()
def print_time(threadName, delay, Counter):
    while Counter:
        time.sleep(delay)
        print(f"{threadName}:{time.ctime(time.time())}")
        Counter -=1

threadLock = threading.Lock()
threads=[]
thread1 = myThread (1, "Thread -1", 1)
thread2 = myThread (2, "Thread -2", 2)
thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print("Exiting Main Thread")
