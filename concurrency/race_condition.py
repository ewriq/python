import threading

counter = 0
lock = threading.Lock()

def increase():
    global counter

    for i in range(100):
        with lock:
            counter += 1

threads = []

for i in range(2):
    t = threading.Thread(target=increase)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(counter)