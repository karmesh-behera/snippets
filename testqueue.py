import logging
import queue
import threading 
import concurrent 
import time
import os
import sys
sys.path.append(os.path.abspath(r"C:\Users\Karmesh\Code Snippets\queueconcurrency.py"))
from queueconcurrency import *


def main():
    #exec(open('C:\Users\Karmesh\Code Snippets\oddsevensagain.py').read())
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()
    

if __name__ == "__main__":
    main()