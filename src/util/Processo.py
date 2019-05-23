import threading
from queue import Queue
import time


def exampleJob(self, worker):
    for i in range(500001):
        print(i)
        p = i / 5000
        self.progressBar.setValue(p)

    with self.print_lock:
        print("EEE")
        print(threading.current_thread().name, worker)
        print("EEE")


def threader(self):
    while True:
        print("C")
        worker = self.q.get()
        print("T")
        self.exampleJob(worker)
        print("TT")
        self.q.task_done()
        print("D")


def processo(self):
    print("Diii")
    self.print_lock = threading.Lock()
    print("Diii")

    print("DIII")
    self.q = Queue()
    print("DIII")

    print("a")
    t = threading.Thread(target=self.threader)
    print("aa")
    t.daemon = True
    print("aaa")
    t.start()
    print("A")

    self.q.put(0)
    print("B")

    # self.q.join()


processo(self)

#print("Trabalho todo levou ",time.time()-start," segundos")

def exampleJob(self, worker):
    for i in range(500001):
        print(i)
        p = i / 5000
        self.progressBar.setValue(p)

    with self.print_lock:
        print(threading.current_thread().name, worker)


def threader(self):
    while True:
        worker = self.q.get()
        self.exampleJob(worker)
        self.q.task_done()


def processo(self):
    self.print_lock = threading.Lock()
    self.q = Queue()

    t = threading.Thread(target=self.threader)
    t.daemon = True
    t.start()

    self.q.put(0)

    # self.q.join()