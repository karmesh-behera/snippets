import threading 
import logging 
odd_event = threading.Event()
even_event = threading.Event()
TIMEOUT = 0.1

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)

def evens(n):
    for i in range(0, n, 2):
        print(i)
        odd_event.set()
        even_event.clear()
        even_event.wait()
        even_event.wait(timeout=TIMEOUT)

def odds(n):
    odd_event.wait()
    for i in range(1, n, 2):
        print(i)
        even_event.set()
        odd_event.clear()
        odd_event.wait()
        odd_event.wait(timeout=TIMEOUT)

def main():
    n = 20
    x = threading.Thread(target=evens, args=(n,), daemon=False)
    y = threading.Thread(target=odds, args=(n,), daemon=False)

    x.start()
    y.start()

    #x.join()
    #y.join()

if __name__ == "__main__":
    main()
