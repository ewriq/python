import threading
import time

semaphore = threading.Semaphore(2)

def work(number):
    with semaphore:
        print(number, "start")

        time.sleep(2)

        print(number, "Worker finished")

threads = []

for i in range(5):
    t = threading.Thread(target=work, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()